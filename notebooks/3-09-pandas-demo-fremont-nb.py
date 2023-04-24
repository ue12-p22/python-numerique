# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: "Les v\xE9los sur le pont de Fremont"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %% [markdown]
# # Les vélos sur le pont de Fremont

# %% [markdown]
# voir la version originale de ce TP - par Jake Vanderplas - sur Youtube
#
# <https://www.youtube.com/watch?v=_ZEWDGpM-vM&list=PLYCpMb24GpOC704uO9svUrihl-HY1tTJJ>

# %% [markdown]
# ## propos - niveau avancé

# %% [markdown] tags=["level_intermediate"]
# cet exercice est destiné aux élèves rapides
#
# c'est une démonstration de ce qu'on peut faire comme analyse sur des **données réelles**, en partant des **données brutes**, et en allant jusqu'à une classification des jours en 'travaillé/repos' en se basant uniquement sur les données du trafic des vélos sur un pont
#
# on utilise brièvement des techniques classiques de **classification** (ACP et gaussian-mixture en l'occurrence), qui ne sont utilisées ici comme des **boites noires**, elle ne sont pas du tout explicitées à ce stade (vous les étudierez dans d'autres cours)

# %%
import pandas as pd

# %%
# # %pip install seaborn

# %%
# pour les visus
import matplotlib.pyplot as plt
# uniquement pour le look des figures mpl
import seaborn as sns

# %% [markdown]
# ## récupération

# %% [markdown]
# on part des données publiques qui décrivent le trafic des vélos [sur 
# le pont de Fremont (à Portland - Oregon)](https://www.google.com/maps/place/Fremont+Bridge/@45.5166602,-122.7147124,12.31z/data=!4m5!3m4!1s0x0:0x9014fe26b76a82db!8m2!3d45.5379639!4d-122.6830729)

# %%
URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

# %% [markdown]
# le fichier de données est distribué avec le notebook
#
# toutefois pour votre information, voici le code qu'on a utilisé pour aller chercher la donnée  
# l'idée est d'aller sur le réseau seulement quand le fichier n'est pas là (notion de *mise en cache*)

# %%
# où chercher/ranger le fichier en local
local_file = "fremont.csv"

# %% tags=["level_intermediate"]
# ceci nécessite alors
# # %pip install requests

# %% tags=["level_intermediate"]
from pathlib import Path

if Path(local_file).exists():
    print(f"le fichier {local_file} est déjà là")
else:
    print(f"allons chercher le fichier {local_file}")

    import requests
    req = requests.get(URL)

    # doit afficher 200
    print(req.status_code)

    # on sauve tel quel dans le fichier local
    with open(local_file, 'w') as writer:
        writer.write(req.text)

# %% scrolled=false
# si windows: ouvrez le fichier dans vscode pour voir le début

# !head $local_file

# %% [markdown]
# ## chargement

# %% [markdown]
# on en fait une dataframe

# %%
# version naïve
data = pd.read_csv(local_file); data.shape

# %%
data.head()

# %% [markdown]
# ## doublons

# %% [markdown]
# en fait ce qu'il se passe c'est que c'est un peu le bazar ce dataset, et que les données sont principalement présentes en deux exemplaires !

# %%
# sur une plateforme Unix (i.e. linux ou macos) on pourrait faire 
# !grep '01/01/2014 12:00:00 AM' $local_file

# %%
# si ça ne fonctionne pas vous pouvez exécuter ce code Python à la place
with open(local_file) as feed:
    for line in feed:
        if '01/01/2014 12:00:00 AM' in line:
            print(line, end="")

# %% [markdown] tags=["level_basic"]
# **exercice**
#
# cherchez dans les méthodes de la dataframe pour
#
# * compter le nombre de lignes dupliquées
# * éliminer les doublons de la dataframe
# * afficher la taille de départ et la taille finale, vérifier que la taille finale correspond à la taille de départ moins les doublons
#
# **indice** le mot clé c'est `duplicate` 

# %%
# votre code

# %% [markdown]
# ***
# ***
# ***

# %% [markdown]
# ## parser les dates

# %%
# intéressant aussi, pour voir notamment les points manquants
data.info();

# %%
# ou tout simplement
data.dtypes

# %% [markdown]
# bref le point ici c'est que les dates sont **des chaines**, alors qu'**on veut des dates**
#
# question subsidiaire: pourquoi les décomptes sont des flottants ?

# %% [markdown]
# ### la version lente
#
# pour traduire les dates, la première idée aurait été de demander à parser les dates *directement au chargement*
#
# ```python
# data = pd.read_csv(local_file, index_col='Date', parse_dates=True); data.head()
# ```
#
# sauf que, vous pouvez essayer, c'est effroyablement lent, car `read_csv` doit faire plein d'essais inutiles (il y a 1001 façons d'écrire une date dans un fichier)

# %% [markdown]
# ### la bonne façon
#
# une façon de faire bien plus efficace, même si elles demande un peu plus de soin de la part du programmeur, 
# consiste à indiquer le format qui a été utilisé pour stocker les dates
#
# pour cette étape on peut utiliser `pd.to_datetime()` qui se comporte un peu comme `pd.as_type()`

# %%
data.Date.head(2)

# %% [markdown] tags=["level_basic"]
# **exercice**
#
# * premier travail, déterminez si les dates sont `jj/mm` ou `mm/jj`
# * traduisez la colonne `Date` dans le type adéquat
# * adoptez cette colonne comme index

# %%
# à vous

# commencez par rechercher la page web qui donne le détail des formats possibles
# avec par exemple les mots-clé 'python datetime string format'

# %% [markdown]
# ***
# ***
# ***

# %% [markdown]
# ## tri

# %% [markdown] tags=["level_basic"]
# **exercice**
#
# c'est le moment de trier les données dans l'ordre chronologique

# %%
# à vous

# %% [markdown]
# ## renommons les colonnes

# %% [markdown] tags=["level_basic"]
# **exercice**
#
# on va se simplifier la vie et renommer les colonnes avec les noms suivants

# %%
# les noms de colonne ne sont pas pratiques du tout
new_names = ['Total',  'East', 'West',]


# %%
# à vous

# %% [markdown]
# ## données manquantes et extension types

# %% [markdown]
# de manière totalement optionnelle, mais on remarque que les nombres ont été convertis en flottants
#
# et ça c'est parce qu'il y a eu quelques interruptions de service, apparemment, avec le système de récolte de l'information
#
# en effet dans ces cas-là, la table contient un 'NaN'; et par défaut `pandas` choisit de représenter la colonne avec des *flottants* parce que dans le type flottant il y a une valeur `nan`
#
# **note** dans les versions récentes de pandas, il y a des *extension types* qui permettraient de manipuler des colonnes contenant des entiers et des *nan*, mais dans le cas présent on préfère purement et simplement ignorer ces lignes

# %% [markdown] tags=["level_basic"]
# **exercice**
#
# * trouvez le nombre de lignes de la table qui contiennent au moins une donnée manquante
# * trouvez la phrase qui permet d'enlever de la table toutes ces lignes
# * en repartant des donnnées du départ, remplacez les valeurs manquantes par des 0
#
# **indices**
#
# les méthodes `isna`, `dropna` et `fillna`
#

# %%
# votre code pour enlever les données manquantes

# %%
# votre code pour recharger la dataframe
# lire, enlever les doublons, indexer par la date
# trier, renommer les colonnes

# %%
# votre code pour remplir les données manquantes

# %% [markdown]
# ***
# ***
# ***

# %% [markdown]
# ***

# %% [markdown]
# ## à quoi ça ressemble

# %% [markdown]
# maintenant qu'on a des données raisonnablement propres, on peut regarder un peu ce qu'il y a dedans
#
# on va utiliser seaborn pour faire les affichages, et on fixe une taille de figure par défaut

# %%
# %matplotlib notebook

# %%
plt.style.use('seaborn-v0_8')
sns.set(rc={'figure.figsize': (8, 4)})
#plt.rcParams["figure.figsize"] = (12, 4)

# %% [markdown]
# bon la première version est naïve, on ne voit pas encore trop grand-chose

# %%
data[['East', 'West']].plot();

# %% [markdown]
# ### ajustement

# %% [markdown]
# pour y voir plus clair, on va montrer seulement un point par semaine
#
# ici on choisit de construire un point par semaine, qui est la moyenne  
# on aurait pu choisir la somme aussi bien sûr, qui est en général 7 fois plus importante, 
# sauf dans le cas des données manquantes (mais c'est un détail ici)

# %% [markdown] tags=["level_basic"]
# question: quelle méthode utiliser pour cela ?

# %% [markdown]
# ***

# %% [markdown]
# ***

# %% [markdown]
# ***

# %%
# c'est plus lisible avec seulement un point par semaine
# on pourrait faire la moyenne aussi bien sûr,
# ça donnerait le même dessin mais avec les Y divisés par 7

# le point c'est qu'on a quelques années de plus que sur la vidéo

data.resample('W').mean().plot();

# %% [markdown]
# juste pour être en phase (pouvoir vérifier nos résultats par rapport à ceux de la vidéo), on va s'arrêter à la fin de 2017
#
# (un détail à noter aussi, les données de la vidéo ne contenaient pas la colonne 'total' à l'époque...)

# %% [markdown] tags=["level_basic"]
# **exercice**
#
# ne conserver que les données jusqu'à fin 2017

# %% [markdown]
# ce qui nous donne ce graphique

# %%
data.resample('W').sum().plot();

# %% [markdown]
# ## `resample()` ?

# %% [markdown]
# petite digression, mais décortiquons un peu cette histoire de `resample()`, pour vérifier notre intuition concernant le nombre d'entrées dans le résultat du `resample`

# %%
data.shape

# %%
# la forme du resample() est de:
data.resample('1W').mean().shape

# %%
# on vérifie que la version resamplée a bien 
# 7 * 24 = 168 fois moins d'entrées que la version brute
# puisqu'on a une mesure par heure et qu'on ré-échatillonne sur une semaine

(full, _), (resampled, _) = data.shape, data.resample('1W').mean().shape

full / resampled , 7 * 24

# %% [markdown]
# ## reprenons

# %% [markdown]
# un aperçu de l'importance du trafic hebdomadaire dans les deux sens

# %%
data.resample('1W').mean().plot();

# %% [markdown]
# ### fenêtre glissante

# %% [markdown]
# si maintenant on veut voir les évolutions sur le temps plus long, on peut avoir recours à une **fenêtre glissante**

# %%
# la somme sur une fenêtre glissante d'un an

# mais : méfiez-vous de l'échelle des Y

data.resample('1D').mean().rolling(365).sum().plot();

# %% [markdown] tags=["level_basic"]
# **exercice**: 
#
# * cherchez la documentation de `rolling` - par défaut, la valeur d'une corbeille est affectée à quel point (début, milieu, fin ?)
# * comparez la date du premier point dans les données, avec la date du premier point dans le graphe

# %% [markdown]
# ici on va afficher la somme sur un an du trafic moyen journalier
#
# si bien que si on regarde, dans cette table, la différence entre deux jours consécutifs, ce qu'on obtient c'est en réalité la différence d'une année sur l'autre

# %% [markdown]
# ### attention aux Y

# %% [markdown]
# remarquons que dans la visu précédente, l'axe des Y ne commence pas à 0  
# ceci parce que, sans indication, `plot()` tient compte des valeurs min et max pour ajuster l'échelle des Y
#
# on le remarque si on se souvient que la courbe du dessus correspond à la somme des deux courbes au dessous
#
# et pour corriger ça on fixe l'échelle des Y à être `0` (le minimum) et `None` (le maximum),  
# indiquant à matplotlib de se baser sur le maximum trouvé dans la donnée

# %%
# on fait en sorte que le bas de l'échelle des Y soit bien 0
# pour eviter l'effet de loupe

ax = data.resample('1D').sum().rolling(365).sum().plot()
ax.set_ylim(0, None);


# %% [markdown]
# ## les profils journaliers

# %% [markdown]
# changeons de sujet; on veut voir maintenant les tendances de l'évolution du trafic **à l'échelle de la journée**

# %% [markdown]
# pour cela on calcule et affiche la moyenne, sur toute la période, mais par heure de la journée

# %%
# regardons la tendance des profils journaliers en moyenne

data.groupby(data.index.time).mean().plot();

# %% [markdown]
# en fait notre objectif est de voir si on peut **classifier**  
# en utilisant uniquement cette information de trafic  
# **les jours entre jour travaillé ou non**
#
# du coup pour y voir un peu mieux, on veut afficher les jours 
# **individuellement** les uns des autres 
#
# on veut donc dessiner 
#
# * *autant de courbes que de jours*
# * et chaque courbe va avoir, en X l'heure de la journée, et en Y le nombre total de passages  
#  (on est obligé de simplifier un peu car si on garde nos 3 valeurs on n'y voit plus rien)

# %% [markdown]
# pour faire ça on calcule grâce à `pivot_table` une table P dont
#
# * comme on veut une courbe par jour: les colonnes de P sont les jours
# * on veut en X les heures: l'index des lignes de P correspond aux heures de la journée

# %%
pivoted = data.pivot_table(
    'Total',                  # ce qu'on veut voir à la fin (en Y)
    index=data.index.time,    # sur quelle dimension (en X)
    columns=data.index.date,  # autant que de courbes
)

# %%
# pour vérifer notre géométrie
# regardons le coin en haut à gauche

pivoted.iloc[:5, :5]

# %%
# on confirme les dimensions 

pivoted.shape

# %%
# du coup on n'a plus qu'à dessiner
# l'astuce qui tue c'est alpha=0.01 pour éviter les gros patés

pivoted.plot(legend=False, alpha=0.01);

# %% [markdown]
# ou on distingue bien deux sortes de jours:
#
# * une grosse majorité qui ont 2 bosses bien marquées, le matin et le soir,  
#   on se dit que ce sont des **jours travaillés**
# * une deuxième classe, minoritaire mais bien présente, avec un trafic moindre,  
#   et une unique bosse en milieu de journée, on se dit que ce sont les **jours de repos**

# %% [markdown]
# ## classification

# %% [markdown]
# ici il s'agit de classifier les jours en deux familles, qu'on voit très distinctement sur la figure
#
# et donc on va faire une ACP sur un tableau qui aurait 
#
# * 24 colonnes correspondant aux heures de la journée
# * autant de lignes que de jours
#
# et donc c'est presque exactement `pivoted`, sauf que c'est sa transposée !

# %%
pivoted.T.shape

# %%
# en 2018 il fallait passer à sklearn un tableau numpy
# il semble que depuis sklearn est mieux intégré à pandas
# et il y aurait donc aussi la possibilité
# de travailler directement à partir d'une dataframe pandas
# mais pour nous ceci est 'good enough'

pca_in = pivoted.fillna(0).T.to_numpy()
pca_in.shape

# %%
# #%pip install scikit_learn
from sklearn.decomposition import PCA

# %%
# on lance l'ACP pour obtenir les coordonnées de chaque jour
# dans un repère réduit aux 2 vecteurs propres les plus importants
coords = PCA(2, svd_solver='full').fit_transform(pca_in)
#            ^ le 2 est ici

# %%
# toujours autant de jours, mais 
# on a gardé seulement 2 vecteurs propres
coords.shape

# %%
# on voit effectivement que cet ACP semble bien séparer deux clusters

plt.figure()
plt.scatter(coords[:, 0], coords[:, 1]);

# %%
# pour trouver ces deux clusters, Jake utilise une GaussianMixture

from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(2)

# c'est ici que tout se passe
labels = gmm.fit(pca_in).predict(pca_in)


# la sortie est une association jour -> type
# sachant qu'on a trouvé deux types
# logiquement repérés par 0 et 1
labels.shape, labels

# %%
# on raffiche en couleurs pour bien voir
# les deux familles trouvées par cette classification
#
# comme on le voir sur le coté
# label=0 correspond aux points en bleu
# label=1 correspond aux points en rouge et 

plt.figure()
plt.scatter(coords[:, 0], coords[:, 1], c=labels, cmap='rainbow')
plt.colorbar();

# %% [markdown]
# ### `label==0` (en bleu): les weekends

# %%
# pour vérifier notre classification on peut redessiner
# les jours classés label==0 

# on voit que ça correspond aux jours de repos

pivoted.T.loc[labels==0].T.plot(legend=False, alpha=0.01);

# %% [markdown]
# ### `label==1` (en rouge) : les jours de semaine

# %%
# et les jours classés label==1

pivoted.T[labels==1].T.plot(legend=False, alpha=0.01);

# %% [markdown]
# ### les deux clusters avec le jour de la semaine

# %% [markdown]
# essayons de vérifier que les deux clusters correspondent bien à l'intuition de départ
#
# pour ça on redessine les deux clusters avec une couleur qui indique le jour de la semaine

# %%
# notre index horizontal n'est pas de type DatetimeIndex
pivoted.columns

# %%
# un index qui contient toutes nos dates et de type DatetimeIndex
dates = pd.DatetimeIndex(pivoted.columns)

# %%
# ceci nous calcule un index sur les jours
# mais avec comme valeur 0 pour le lundi, ... et 6 pour le dimanche

dayofweek = pd.DatetimeIndex(pivoted.columns).dayofweek

# on a bien une valeur par jour dans l'échantillon
dayofweek

# %%
# qu'on va utiliser pour mettre les jours en couleur
# les jours de weekend sont en orange et rouge

plt.figure()
plt.scatter(coords[:, 0], coords[:, 1], c=dayofweek, cmap='rainbow')
# pour la légende
plt.colorbar();

# %% [markdown]
# **CQFD**: majoritairement, les jours de la semaine (bleu/vert/jaune) sont bien dans le nuage inférieur, ils correspondent donc bien à `label==1` tel que produit par le mélange de gaussiennes

# %% [markdown]
# ### les moutons noirs

# %% [markdown]
# enfin pas complétement tout à fait non plus, il y a quelques exceptions  
# on remarque des jours de la semaine (bleu/vert/jaune) dans le nuage de gauche
#
# vérifions qu'il s'agit de jours fériés au milieu de la semaine

# %%
# on remarque dans le cluster rouge-orange
# des jours d'une couleur qui jure

# pour comprendre à quoi ils correspondent 

odd_index = (labels == 0) & (dayofweek < 5)
odd_index.shape, odd_index

# %%
sum(odd_index)

# %%
# afficher les 48 jours qui sont dans cette catégorie

# comme on peut s'y attendre
# on y retrouve les jours fériés (4 juillet, Noel, jour de l'an, ...)

odd_dates = dates[odd_index]
odd_dates, len(odd_dates)

# %%
# pour rafficher seulement ces jours-là

pivoted[odd_dates].plot(legend=False, alpha=0.3);

# %% [markdown]
# ## épilogue

# %% [markdown]
# on espère avoir convaincu le lecteur de la puissance de `pandas` au travers de cet exemple où,
# si on met à part les techniques purement issues du machine-learning (ACP et mixtures de gaussiennes), on n'utilise ici finalement que des fonctions relativement basiques des dataframes.
