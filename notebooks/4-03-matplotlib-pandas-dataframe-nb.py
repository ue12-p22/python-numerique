# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     cell_metadata_json: true
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
#     title: '`matplotlib` et `pandas`'
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")

# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import IPython

# %% [markdown]
# # `matplotlib` et `pandas`

# %% [markdown] {"tags": ["framed_cell"]}
# ## introduction
#
# <br>
#
# Les fonctionnalités de `matplotlib` ont été intégrées avec la librairie `pandas`  
# afin de faciliter leur utilisation à partir de dataframe et de séries
#
# <br>
#
# nous allons illustrer les quelques fonctions sur un petit exemple  
# *(référez-vous à la documentation pour aller plus loin dans les réglages -nous resterons ici très simples)*
#
# <br>
#
# une `pandas.DataFrame` est une table de données en dimension 2  
# `matplotlib` lui apporte des facilités de visualisations
# 1. de données des `pandas.Series`  
# e.g plot, boxplots (boîtes à moustaches), histogrammes, barcharts...
# 1. de nuages de points 2D ou 3D impliquant plusieurs colonnes
#
# <br>
#
# nous allons voir quelques plots intéressants sur l'exemple des iris

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell"]}
# ## la dataframe des `iris`
#
# <br>
#
# lisons le `csv` des `iris`  avec `pandas`  
# affichons les 2 premières lignes
#
# ```python
# df = pd.read_csv('iris.csv')
# df.head(2)
# ->
#      SepalLength    SepalWidth    PetalLength    PetalWidth    Name
# 0    5.1            3.5           1.4            0.2           Iris-setosa
# 1    4.9            3.0           1.4            0.2           Iris-setosa
# ```
#
# <br>
#
# affichons les petites statistiques  
# elles donnent une bonne première idée des données, de leur répartition...
#
# ```python
# df.head(2)
# df.describe()
# ->       SepalLength SepalWidth PetalLength PetalWidth
# count    150.000000  150.000000 150.000000  150.000000
# mean     5.843333    3.054000   3.758667    1.198667
# std      0.828066    0.433594   1.764420    0.763161
# min      4.300000    2.000000   1.000000    0.100000
# 25%      5.100000    2.800000   1.600000    0.300000
# 50%      5.800000    3.000000   4.350000    1.300000
# 75%      6.400000    3.300000   5.100000    1.800000
# max      7.900000    4.400000   6.900000    2.500000
# ```
#
# <br>
#
# remarquez que `describe` par défaut  
# n'affiche que les 4 colonnes numériques
#
# <br>
#
# (*dans le code ci-dessous, pour plus de lisibilité  
# nous utilisons l'affichage `html` avec `IPython.display.display`*)

# %%
# le code
df = pd.read_csv('iris.csv')
IPython.display.display(   df.head(2)      )

IPython.display.display(   df.describe()   )

# %% [markdown] {"tags": ["framed_cell"]}
# ## visualisation de la dataframe - `df.plot()`
#
# <br>
#
# la méthode `plot`  des objets de type `pandas.DataFrame` i.e. `pandas.DataFrame.plot`  
# permet une première visualisation simple, rapide et informative **des colonnes numériques**  
# qui apporte beaucoup d'informations sur ces données
#
# <br>
#
# la fonction `pandas.DataFrame.plot` possède les mêmes paramètres que la fonction `matplotlib.pyplot.plot`  
# elle permet les mêmes réglages  
# (en fait elles utilisent toutes les deux la même fonction)
#
# <br>
#
# ```python
# df.plot()
# ```
#
# <img src='media/iris-plot.png'>

# %%
# le code
df.plot();

# %% [markdown] {"tags": ["framed_cell"]}
# ## boxplots des colonnes `df.boxplot`
#
# <br>
#
# un `boxplot` montre:  
# le minimun, le maximum, la médiane, le premier et le troisième quartile  
# les (éventuels) outliers
#
# <br>
#
# les **outliers**  
# sont les points en dehors de *bornes* décidées par `boxplot`  
# ces points sont potentiellement aberrants ou simplement des extrêmes  
# (lire la doc pour connaître les bornes considérées)  
#
# <br>
#
# nous pouvons dessiner les boxplots ensemble  
# ils sont alors mis à la même échelle  
#
# ```python
# df.boxplot()
# ```
#
# <img src='media/iris-boxplot.png'>
#
# <br>
#
# on remarque des outliers dans la colonne des `SepalWidth`  
#
# <br>
#
# nous pouvons dessiner les boxplots des colonnes indiquées par une liste
#
# ```python
# df.boxplot(['SepalWidth', 'PetalWidth'])
# ```
#
# <br>
#
# nous pouvons regrouper les boxplots suivant les valeurs d'une colonne  
# (cela nous rappelle `groupby`, c'est très utile)
#
# ```python
# df.boxplot(['PetalLength'], by='Name')
# ```
#
# <img src='media/iris-boxplot-by.png'>
#
# nous remarquons  
# que les iris *Setosa* ont des `PetalLength` bien plus petits que ceux des autres types d'iris  
# ce qui permet de les discriminer des deux autres types d'iris

# %%
# le code

df.boxplot()

plt.show() # afin de ne pas superposer les plots

df.boxplot(['SepalWidth', 'PetalWidth']);

plt.show()

df.boxplot(['PetalLength'], by='Name')

plt.tight_layout() # le padding

# %% [markdown] {"tags": ["framed_cell"]}
# ## histogrammes `df.hist`
#
# <br>
#
# un histogramme donne la distribution des valeurs d'une colonne
#
# <br>
#
# les valeurs de la colonne sont rangées dans des intervalles - ou *bins*  
# les nombres de valeurs par intervalle sont affichés
#
# ```python
# df.hist()
# ```
# <img src='media/iris-hist.png'>
#
# <br>
#
# on remarque 3 pics dans `SepalLength`  
# correspondent-ils aux 3 types d'iris ?
#
# <br>
#
# on peut dessiner l'histogramme d'une seule colonne  
# on peut changer des paramètres comme le nombre d'intervalles `bins=`, la couleur `color=`...
#
# ```python
# df.hist('SepalLength', bins=10, color='lightblue')
# ```

# %% {"cell_style": "center", "scrolled": true}
# le code
df.hist()
df.hist('SepalLength', bins = 10, color='lightblue')
plt.title('histogramme de la colonne SepalLength');

# %% [markdown] {"tags": ["framed_cell"]}
# ## barchart `df.plot.bar()`
#
# <br>
#
# prenons un exemple pour illustrer le dessin des barres  
# la dataframe `df_animals` des animaux, leur vitesse et leur durée de vie
#
# <br>
#
# barres verticales
#
# ```python
# df_animals.plot.bar()
# ```
#
# <br>
#
# barres horizontales
#
# ```python
# df_animals.plot.hbar()
# ```
#
# <br>
#
# une seule colonne
#
# ```python
# df_animals.plot.barh(x='lifespan')
# ```
#
# <br>
#
# une colonne
#
# ```python
# df_animals.plot.barh(x='lifespan')
# ```
#
# <br>
#
# une colonne en fonction d'une autre
#
# ```python
# df_animals.plot.barh(x='lifespan')
# ```
#
# <br>
#
# utilisez le `help`

# %%
# le code
df_animals = pd.DataFrame({'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
                   'lifespan' : [2, 8, 70, 1.5, 25, 12, 28]},
                  index = ['snail', 'pig', 'elephant',
                           'rabbit', 'giraffe', 'coyote', 'horse'])

df_animals.plot.bar()

df_animals.plot.barh()

df_animals.plot.bar(x='lifespan', y='speed');

# %% [markdown] {"tags": ["framed_cell"]}
# ## la colonne des `'Name'`
#
# <br>
#
# revenons à nos `iris`
#
# <br>
#
# affichons la description de la colonne des types de fleurs `'Name'`
#
# ```python
# df[['Name']].describe()
# ->
# Name
# count	150
# unique	3
# top	Iris-versicolor
# freq	50
# ```
#  
# <br>
#
# nous avons 3 noms uniques donc 3 types différents d'iris
#
# <br>
#
# comptons le nombre d'observations  
# par valeurs dans cette colonne
#
# ```python
# df['Name'].value_counts()
# ->
# Iris-versicolor    50
# Iris-virginica     50
# Iris-setosa        50
# Name: Name, dtype: int64
# ```
#
# <br>
#
# on remarque que les 3 types sont bien répartis dans les données (1/3)
#
# <br>
#
# affichons le type des éléments de la colonne `Name`
#
# ```python
# df['Name'].dtype
# -> 'O'
# ```
#
# `O` signifie `object`
#
# <br>
#
# ce type est `object` ici ce sont des objets de type chaînes de caractères
#
# <br>
#
# pourtant ...  
# la colonne des noms des `iris` est plutôt une colonne de type catégorie  
# avec ses 3 valeurs `Iris-versicolor`, `Iris-virginica` et `Iris-setosa`
#
# <br>
#
# nous allons changer le type des éléments de la série `df['Name']`  
# par un exercice

# %%
# le code
IPython.display.display(   df[['Name']].describe()   )
df['Name'].value_counts()

# %% {"scrolled": false}
#le code
df['Name'].dtype

# %% [markdown]
# ## exercice: encodage la colonne des noms en catégorie

# %% [markdown]
# **exercice** encodage la colonne des noms en catégorie
#
# 1. Afficher le type de la colonne `df['Name']`  
# (pas le type des éléments de la colonne mais de la colonne elle même)
# <br>
#
# 1. utiliser la méthode `astype` des `pandas.Series` - donc la méthode `pandas.Series.astype`  
# sur cette colonne, pour créer une nouvelle colonne avec le type `'category'`
# <br>
#
# 1. afficher le type des éléments de cette colonne  
# vérifier que c'est bien un type catégorie
# <br>
#
# Nous allons maintenant extraire de cette nouvelle colonne, les codes générés par `pandas` pour les trois catégories d'`iris`
#
# **à savoir:** sur une colonne de type `category`  
# `cat` permet d'accéder aux méthodes et attributs des objets de type catégorie  
# (comme `str` le permet sur les colonnes d'éléments de type `str`)<br>
# et l'attribut `codes` est le code donné par `pandas` aux 3 catégories
#
# 1. accéder aux codes de la nouvelle colonne  
# Quels sont-ils ? Quel est leur type ?
# <br>
#
# 1. et ajouter cette colonne de codes à la dataframe, en l'appelant avec comme nom: `'Name-code'`
#
# -------------------------
#
# À quoi cela va-t-il nous servir ?  
# par exemple à améliorer nos visualisations  
# ces codes peuvent servir, par exemple, de code-couleur pour afficher des points  
# on verra cela plus tard

# %%
df

# %%
# on vous montre comment faire pas à pas

col = df['Name'].astype('category')
print(col.dtype)
df['Name-code'] = col.cat.codes
df['Name-code'].value_counts()

# %%
# comment on pourrait faire à en une seul ligne ?

# %% [markdown]
# ## nuages de points `df.plot.scatter`

# %% [markdown]
# <br>
#
# pour mettre en valeur des informations sur nos données  
# on peut dessiner en 2D les colonnes les unes par rapport aux autres  
# avec `pandas.DataFrame.plot.scatter`
#
# <br>
#
# dessinons les `'SepalLength'` en fonction des `'SepalWidth'`
#
# ```python
# df.plot.scatter(x='SepalLength', y='SepalWidth')
# ```
#
# <br>
#
# on peut le faire directement en `matplotlib.pyplot.plot`  
# mais il faut alors préciser tous les paramètres (noms des axes...)
#
# ```python
# plt.scatter(df['SepalLength'], df['SepalWidth'])
# ```
#
# <br>
#
# avec le paramètre `c=`  
#
# * on peut changer la couleur  
# * mais on peut aussi, indiquer une **couleur par point**  
# * une idée du code couleur intéressant à utiliser ?
#
# <br>
#
# oui, on peut représenter ainsi la catégorie des points  
#
# * chacun des 3 types d'iris, est une valeur entière différente  
# * on va considérer cette valeur comme un code dans une table de couleurs
# * attention au code `0` (il peut être très peu coloré dans certaines tables)
#
# ```python
# df.plot.scatter(x='SepalLength', y='SepalWidth', c='Name-code', cmap='viridis');
# ```
#
# <br>
#
# avec `matplotlib.pyplot.plot`  
# mais vous n'avez alors les paramètres par défaut
#
# ```python
# plt.scatter(df['SepalLength'], df['SepalWidth'], c=df['Name-code'], cmap='viridis')
# plt.colorbar() # sinon pas de jolie barre de couleur
# ```
#
# <br>
#
# avec le paramètre `s=` on peut changer la taille des points  
# ou la taille de chaque point  
# par exemple, donnons leur une taille proportionnelle à la largeur des pétales  
#
# ```python
# plt.scatter(df['SepalLength'], df['SepalWidth'], c=df['Name-code'], s=df['PetalWidth']);
# ```
#
# <br>
#
# ainsi sur un même dessin on peut voir 4 informations  
# le nuage, la couleur et la taille des points
#
# <br>
#
# il faut travailler un peu les paramètres pour que ce soit visible  
# (là la taille est trop peu différenciée, multipliez la)

# %%
# le code
df.plot.scatter(x='SepalLength', y='SepalWidth');

# %%
# le code
plt.scatter(df['SepalLength'], df['SepalWidth']);

# %%
# le code
df.plot.scatter(x='SepalLength', y='SepalWidth', c='Name-code', cmap='viridis');

# %%
# le code
plt.scatter(df['SepalLength'], df['SepalWidth'], c=df['Name-code'], cmap='viridis')
plt.colorbar();

# %%
# le code
plt.scatter(df['SepalLength'], df['SepalWidth'], c=df['Name-code'], s=df['PetalWidth']*50);

# %% [markdown]
# ## exercice sur des vins italiens

# %% [markdown]
# le fichier `wine.csv` contient
#
# * les résultats d'analyses chimiques de vins, cultivés dans une même région d'Italie  
# (13 mesures) par trois cultivateurs différents 1, 2 et 3
#
# la première ligne du `csv` contient les noms des colonnes

# %% [markdown]
# cultivator,alcohol,malic-acid,ash,alcalinity-of-ash,magnesium,total-phenols,flavanoids,nonflavanoid-phenols,proanthocyanins,color-intensity,hue,od280/od315-of-diluted wines,proline

# %% [markdown]
# **exercice de visualisatin de vins**
#
# 1. lisez le fichier en ne gardant que les colonnes suivantes
# ```python
# cols = ['cultivator', 'alcohol', 'malic-acid', 'ash', 'total-phenols',
#            'flavanoids','color-intensity', 'hue' ]
# ```
# (indice: paramètre `use_cols` de `pandas.read_csv`)
# <br>
#
# 1. afficher le header de la dataframe
# <br>
#
# 1. afficher les types déterminés par `pandas`
# <br>
#
# 1. afficher les statistiques simples
# <br>
#
# 1. plottez la dataframe en lui passant le paramètre *figsize=(10, 10)*
# <br>
#
# 1. plottez la dataframe restreinte aux deux colonnes `['flavanoids', 'cultivator']`  
# que constatez-vous ?
# <br>
#
# 1. visualisez les boxplots de la dataframe  
# utilisez la fonction `plt.xticks(rotation=90)` pour mieux voir les labels des abscisses
# <br>
#
# 1. visualisez des histogrammes avec des regroupements de 20 éléments  
# pensez à `plt.tight_layout()` qui ajoute des paddings intéressants
# <br>
#
# 1. afficher l'alcool en fonction de l'acide malique avec comme couleur les numéros des cultivateurs  
# pensez à utiliser une `cmap`
