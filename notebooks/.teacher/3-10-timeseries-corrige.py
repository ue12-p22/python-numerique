# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -jupytext.custom_cell_magics,
#       -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
#       -language_info.file_extension, -language_info.mimetype, -toc, -vscode
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


# %%
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# # timeseries en pandas

# %% [markdown]
# il est très fréquent d'avoir dans ses données des grandeurs qui représentent le temps; voyons un peu ce que `pandas` peut faire pour nous aider avec ce genre de traitements
#
# <br>
# <div class=note>
#
# le sujet est **extrêmement** vaste:  
# dualité date et heure, fuseaux horaires, formats `yy/mm/dd` vs `yy/dd/mm`, jours fériés, années bissextiles, *leap seconds*, abandon du calendrier julien en 1582 mais pas partout, …  
# bref on n'en donne ici qu'une version **très** édulcorée
#
# </div>

# %% [markdown]
# ## les types de base

# %% [markdown]
# ### `datetime`

# %% [markdown]
# pour commencer, parlons un peu des types de base; en Python pur, on trouve dans la librairie standard [(`import datetime`)](https://docs.python.org/3/library/datetime.html) deux types de données principaux
# * `datetime` qui permet de modéliser un instant (par exemple, le 10 octobre 1954 à 10h 32' 15'' - et même plus précis encore si nécessaire)
# * `timedelta` qui permet de modéliser une durée (par exemple 2 heures 15 minutes, ou 3 ans)
#
# **note** on **n'utilise pas directement** ces deux types en pandas, mais c'est tout de même la fondation du modèle, donc attardons-nous un tout petit peu

# %%
# pour rester cohérent dans le nommage des classes
# je préfère les importer avec un nom conforme à la PEP008
from datetime import (
    datetime as DateTime, 
    timedelta as TimeDelta)


# %%
# pour modéliser un instant
t1 = DateTime.fromisoformat('2021-12-31T22:30:00')
t1

# %%
# et une durée
d1 = TimeDelta(hours=4)
d1

# %% [markdown]
# #### un peu d'arithmétique

# %%
# on peut faire de l'arithmétique
# avec ces deux types

# 4 heures après t1
t2 = t1 + d1
t2

# %%
# ajouter, soustraire, multiplier, diviser ...

# 8 haures avant ça, i.e. 4 heures avant d1
t2 - 2 * d1

# %%
# combien de fois 10 minutes dans 4 heures

d1 // TimeDelta(minutes=10)

# %% [markdown]
# #### décomposer

# %% [markdown]
# pour accéder aux différents éléments d'une date (année, mois, ..), c'est facile

# %%
t1.year, t1.hour

# %%
d1.days, d1.seconds

# %% [markdown]
# à titre plus anecdotique, on peut aussi appliquer directement un format à un instant dans une f-string  

# %%
# # %H c'est pour extraire l'heure
# il y a toute une série de codes de format...
f"{t1:%H==%M}"

# %% [markdown]
# par contre ces formats sont **très utiles** lorsqu'on va vouloir traduire nos fichiers d'entrée en date/heure
#
# pour une liste complète des formats, voir
# <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>

# %% [markdown]
# ### la version `numpy`

# %% [markdown]
# ces deux types fournissent la bonne abstraction; malheureusement l'implémentation est sous-optimale pour les applications scientifiques, car notamment :
# * ils ne couvrent pas les échelles infiniment grandes (temps astronomique)  
#   ou infiniment petites (physique des particules)
# * ils ne supportent pas la notion de valeur indéfinie, comme le `nan` pour les nombres
#
# du coup on trouve [dans numpy](https://numpy.org/doc/stable/reference/arrays.datetime.html)
# des versions plus flexibles et plus modernes de ces deux classes, qui s'appellent `np.datetime64` et `np.timedelta64`, qui n'ont pas ces lacunes
#
# bref, ce sont **ces types qui seront utilisés** sous le capot, lorsqu'on aura à manipuler des grandeurs temporelles

# %% [markdown]
# ### la version `pandas`

# %% [markdown]
# **mais** ici encore les types `numpy`, malgré leurs qualités, ont le gros défaut d'être très peu *user-friendly*, aussi `pandas` nous expose sa propre version de essentiellement les mêmes concepts, plus un:
#
# * `Timestamp` pour un instant (ça aurait pu/dû s'appeler `Datetime`, mais bon...)
# * `Timedelta` pour une durée
# * `Period` pour un intervalle de temps, représenté par un début **et** une durée
#
# ces types sont fabriqués *au dessus* des 2 types de base fournis par `numpy`, et visent donc principalement à les rendre plus faciles à utiliser

# %% [markdown]
# ## **exercice**: le cours de l'action amazon

# %% [markdown]
# vous avez peut-être remarqué que `read_csv` propose des (tas d') options pour la gestion des instants (notamment le paramètre `parse_dates`); toutefois j'ai envie de vous conseiller de rester loin de ce genre de features, au moins pour commencer

# %%
# # pd.read_csv?

# %% [markdown]
# il est sans doute préférable de procéder en deux temps, en combinant `pd.read_csv` et `pd.to_datetime`, ce que vous êtes invité à faire dans cet exercice

# %%
# # pd.to_datetime?

# %% [markdown] tags=["level_basic"]
# 1. lire le fichier de données `Amazon.csv` avec `read_csv()`  
#    attention, le fichier contient 3 premières lignes de commentaires
#    qu'il convient d'ignorer complètement  
#    affichez les types des colonnes  
#    que penser du type de la colonne `Date` ?

# %%
# prune-cell
# cols = ['Date', 'High', 'Low']

# %%
# à vous

# %%
# prune-cell
df = pd.read_csv('Amazon.csv', skiprows=3)
df.head()

# %%
# prune-cell
df.dtypes

# %% [markdown]
# ## **exercice**: `pd.to_datetime()`

# %% [markdown] tags=["level_basic"]
# 2. traduisez la colonne `Date` dans le type adéquat  
# affichez le nouveau type de la colonne  
# ça peut être intéressant de regarder à la fois `dtypes` sur la dataframe et `dtype` sur la série
#
# en option pour les forts: sauriez-vous passer à `to_datetime` le paramètre `format` qui va bien ?

# %%
# à vous

# %%
# prune-begin

# %%
df['Date'] = pd.to_datetime(df.Date)

# %%
# ou encore pour être explicite
df['Date'] = pd.to_datetime(df.Date, "%Y-%m-%d")

# %%
# ici pandas nous montre que c'est un objet numpy
# np.datetime64[ns] et le [ns] indique l'unité
# (voir le tableau en fin de notebook)
df.dtypes

# %%
# ici c'est l'a même information
# mais en version numpy
# le M signifie datetime
# le 8 signifie 8 octets
# le [ns] indique l'unité su timestamp
df.Date.dtype

# %% tags=["level_basic"]
# prune-end

# %% [markdown]
# ## **exercice**: `NaT`

# %% [markdown] tags=["level_basic"]
# 3. comparez l'affichage de la première ligne avec celui d'avant la conversion  
#    que remarquez-vous ?  
#    supprimer les lignes pour lesquelles le champ `Date` est inconnu
#    
#   il y a au moins deux façons évidentes de s'y prendre  
#   essayez de les trouver toutes les deux pour vérifier vos résultats  
#   le nombre de lignes doit passer de 5852 à 5828

# %%
# à vous

# %%
# prune-begin

# %%
df.head(3)

# %% [markdown]
# le premier timestamp est passé de `NaN` à `NaT`  
# cela signifie que le type `Timestamp` supporte la notion de valeur indéfinie

# %% [markdown]
# v1 - à la main

# %%
# on recharge pour être sûr
df = pd.read_csv('Amazon.csv', skiprows=3)
df['Date'] = pd.to_datetime(df.Date)

# %%
print(f"avant {df.shape=}")
df = df[df.Date.notna()]
print(f"après {df.shape=}")

# %% [markdown]
# v2 - avec `dropna()`
#
# ici il n'y a des valeurs manquantes que dans la colonne `Date`

# %%
# # df.dropna?

# %%
# on recharge pour être sûr
df = pd.read_csv('Amazon.csv', skiprows=3)
df['Date'] = pd.to_datetime(df.Date)

# %%
print(f"avant {df.shape=}")
df.dropna(subset=['Date'], inplace=True)
print(f"après {df.shape=}")

# %% tags=["level_basic"]
# prune-end

# %% [markdown]
# ## **exercice**: l'accessor `.dt`

# %% [markdown]
# comme on l'a déjà vu avec `.str` et `.cat`, il existe un accesseur `.dt` pour appliquer sur une série de type `Timestamp` des attributs qui lui sont spécifiques

# %% [markdown] tags=["level_basic"]
# 4. en utilisant cet accesseur, ajoutez à la dataframe une colonne qui contient le jour de la semaine, codé comme:
#
# | jour | code |
# |-|-|
# | lundi | 0 |
# | mardi | 1 |
# | mercredi | 2 |
# | jeudi | 3 |
# | vendredi | 4 |
# | samedi | 5 |
# | dimanche | 6 |
#

# %%
# prune-begin

# %%
# on peut utiliser dayofweek ou weekday
df['week-day'] = df.Date.dt.dayofweek

# %%
# également dispo:
s = df. Date
pd.DataFrame({'original': s,
              'year': s.dt.year,
              'dayofyear': s.dt.dayofyear,
              'month': s.dt.month,
              'hour': s.dt.hour,
              'second': s.dt.second}).head()

# %%
df.head(5)

# %%
# prune-end

# %% [markdown]
# ## **exercice**: plotting

# %% [markdown] tags=["level_basic"]
# 5. utilisez la colonne `Date` comme index  
#    et triez la dataframe selon cet index
#    (ça semble être déjà le cas, mais en est-on bien sûr ?)
#    
# question subsidiaire (pas de code):  
# est-ce que le fait de trier va changer quelque chose à l'affichage (scatter plot) ?  
# est-ce que ça va changer quelque chose lorsqu'on va vouloir sélectionner des plages de temps à base de slicing ?

# %%
# à vous

# %%
# prune-cell
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

# %% [markdown]
# prune-cell
#
# imaginons que les données soient toutes mélangées
#
# * le plotting avec scatter plot ne sera pas affecté (les points (x, y) sont élaborés à partir de l'index, qui est le bon instant)
# * le plotting avec un vrai 'plot' sera affecté, car en plus des points, on va tracer les traits qui joignent deux entrées successives dans la dataframe
# * le slicing à base de `loc` bien sûr va être affecté également

# %%
# df.tail()

# %% [markdown] tags=["level_basic"]
# 6. plottez la valeur de l'action au cours du temps
#
# * sur un même diagramme, les deux cours `High` et `Low`
# * ensuite sur deux diagrammes séparés

# %% [markdown]
# pour dessiner, en tous cas avec `jupyter notebook`, le mieux c'est de choisir le driver `notebook` (dans vs-code il y a un remplacement possible qui est `pyimpl`)
#
# **indice**
# on pourrait bien sûr utiliser `plt.plot()`  
# mais ici on vous invite à utiliser directement la méthode `plot` sur une DataFrame, vous verrez que c'est beaucoup plus simple !

# %%
# %matplotlib notebook

# pour changer la taille des figures par défaut
plt.rcParams["figure.figsize"] = (7, 2)

# %%
cols = ['High', 'Low']

# %%
# à vous

# %%
# prune-begin

# %% [markdown]
# (1) les deux en même temps

# %%
# si on met la création de figure, ça fait double emploi
# avec df.plot() qui de toute évidence le fait aussi
# plt.figure()
df[cols].plot();

# %% [markdown]
# (2) séparément
#
# il y a l'option d'utiliser `.plot()` directement sur une série; toutefois c'est moins pratique (essayez !); on n'a pas de légende, et aussi il faut appeler `plt.figure()` explicitement
#
# bref, c'est plus simple de fabriquer une dataframe avec seulement une colonne  
#
# il faut donc se souvenir que 
#
# * `df[col]` est une série
# * `df[[col]]` est une dataframe
#

# %%
for col in cols:
    df[[col]].plot()

# %%
# prune-end

# %% [markdown]
# ## slicing

# %% [markdown]
# c'est très pratique de slicer un index qui contient des `Timestamp`
#
# ici par exemple nous avons une granularité de la journée (sauf accident il y a une entrée par jour de la semaine)  
# mais on peut slicer de manière assez naturelle, voici quelques exemples:

# %% tags=["raises-exception"]
# on recharge pour être sûr
df = pd.read_csv('Amazon.csv', skiprows=3)
df['Date'] = pd.to_datetime(df.Date)
df.set_index('Date', inplace=True)
df.tail()

# %% tags=["raises-exception"]
# première commodité: on peut utiliser des chaines
# pas besoin de mettre des objet Timestamp dans le slice

# les entrées entre le 1er avril 2020 et le 30 juin 2020
# rappel: comme on utilise .loc c'est INCLUS
df.loc['2020-04-01' : '2020-06-30']

# %% tags=["raises-exception"]
# mais en fait c'est encore plus simple d'écrire
# qui signifie, de avril à juin, toujours inclusivement
df.loc['2020-04' : '2020-06']

# %% [markdown] tags=["level_basic"]
# 7. si bien que, comment feriez-vous pour filtrer par exemple 
#    à partir du 1er janvier 2019 jusqu'à la fin des données

# %%
# à vous

# %%
# prune-cell
df.loc['2019':]

# %% [markdown]
# ## aggrégations avec `resample()` et `rolling()`

# %% [markdown]
# ces deux fonctions travaillent de la même façon: elles regroupent les données dans des *bins* (des corbeilles), et toutes les données qui tombent dans une corbeille peuvent ensuite être agrégées (comme d'habitude avec `mean()`, `sum()`, `min()`,…)

# %% [markdown]
# voyons pour commencer comment les corbeilles sont construites par ces deux fonctions

# %% [markdown]
# ### `resample()`

# %% [markdown]
# l'idée ici c'est de découper le temps en une partition, chaque corbeille ayant la même durée (sauf éventuellement celles aux extrémités)
# dans ce modèle:
# * chaque donnée de départ appartient à exactement une corbeille
# * le nombre de corbeilles dépend, aux arrondis près, du rapport entre la durée totale et la durée de chaque corbeille

# %% [markdown]
# ![](media/timeseries-resample.svg)

# %% [markdown]
# <div class=note>
#
# dans l'illustration ci-dessus, chaque point bleu illustre **la moyenne** de chaque corbeille  
# on a choisi d'attacher chaque point bleu au moment correspondant **au début** de chaque corbeille (et bien sûr c'est réglable..)
#
# </div>  

# %% [markdown]
# **exemple d'application**  
# vous avez un signal échantillonné à 44.100 kHz et vous voulez le ré-échantillonner (littéralement: *resample*) à une fréquence 4 fois plus basse: il suffit de faire un resample avec un durée de corbeille égale à exactement 4 x la période de la fréquence originale

# %% [markdown]
# ### `rolling()`

# %% [markdown]
# la fonction `rolling()` fonctionne aussi sur le modèle de corbeilles; 
# sauf que cette fois-ci, il ne s'agit plus d'une partition, mais de *fenêtre glissante*, comme illustré ci-dessous

# %% [markdown]
# ![](media/timeseries-rolling.svg)

# %% [markdown]
# donc cette fois-ci:
#
# * une donnée appartient en général à plusieurs corbeilles
# * on produit un nombre de corbeilles qui est de l'ordre de grandeur  
#   du nombre de points de départ  
#   spécifiquement, lorsque la fenêtre est exprimée en temps, le rolling a **la même taille** que l'échantillon de départ
#
# <div class=note>
#
# note` que ce n'est pas le cas si on indique une fenêtre en nombre d'échantillons, ce qui est possible également
#
# ce point va être illustré plus bas    
# </div>

# %% [markdown]
# **exemple 1**  
# vous voulez visualiser l'évolution d'une grandeur "d'une année sur l'autre"  
#
#
# on va faire un rolling avec une période d'un an  
# si on appelle $f$ la fonction de départ, et $F$ le rolling sur un an  
# (avec la somme comme agrégation pour simplifier les équations), on va avoir
#
# $$
# F(01/01/2021) = \sum_{j=01/01/2021}^{31/12/2021} f(j) \\
# \;et\; \\
# F(02/01/2022) = \sum_{j=02/01/2021}^{01/01/2022} f(j)
# $$
#
# et donc 
#
# $$
# F(02/01/2021) - F(01/01/2021) = f(02/01/20\textbf{22}) - f(01/01/20\textbf{21})
# $$
#
# ce qui signifie que la dérivée de $F$ (la différence d'un jour à l'autre)  
# c'est l'évolution de $f$ mais **d'une année sur l'autre**

# %% [markdown]
# **exemple 2: effet lissant**

# %% [markdown]
# pour bien voir l'effet 'lissant' de la fenêtre glissante, prenons des données synthétiques:

# %%
import numpy as np

# %% scrolled=true
# c'est l'occasion de voir comment créer des timeseries
# par programme
# ici 100 jours consécutifs
date_index = pd.date_range('2018-01-01', periods=100)

# un battement
X = np.arange(100)
s = pd.Series(10*np.cos(X/10) + 2*np.cos(X), index=date_index)

plt.figure()
s.plot();


# %% [markdown]
# voici l'effet du rolling avec des fenêtres de 1 semaine et 4 semaines

# %%
rolling_7 = s.rolling(window=pd.Timedelta(7, 'D'),
                             center=True).mean()
rolling_28 = s.rolling(window=pd.Timedelta(28, 'D'),
                              center=True).mean()

# %% [markdown]
# ici on a choisi d'attacher le résultat (de la moyenne de la corbeille) au **centre** de la corbeille

# %%
# pour afficher les 3 courbes à la fois

pd.DataFrame({
    'original': s,
    'roll 7D': rolling_7,
    'roll 28D': rolling_28,
}).plot();

# %% [markdown]
# **les bornes**
#
# juste pour bien illustrer le comportement aux bornes, voici
# * le nombre de points dans la rolling: **autant de corbeilles que de points**  
#   (on le voit déjà ci-dessus)
# * et le nombre de points par corbeille: **constant, sauf aux extrémités**

# %%
# exactement autant de corbeilles que de points
len(s), len(rolling_7)

# %%
# le nombre de points par corbeille
count_28 = s.rolling(window=pd.Timedelta(28, 'D'),
                     center=True).count()
pd.DataFrame({'points-per-bin-28': count_28}).plot();

# %% [markdown] tags=["level_intermediate"]
# **exercice / digression**
#
#

# %% [markdown] tags=["level_intermediate"]
# la notion de fenêtre glissante fait du sens pour n'importe quelle donnée, même non-temporelle
#
# reproduisez le dessin ci-dessus, mais 
# * en ne gardant que le rolling sur 4 semaines
# * en indiquant une **fenêtre en nombre de points**
#
# que constatez-vous aux extrémités ?

# %% tags=["level_intermediate"]
# prune-begin

# %% tags=["level_intermediate"]
# avec une fenêtre en points, aux extrémités
# il manque des données !

pd.DataFrame({
    'original': s,
    'roll 28 (integer)': s.rolling(window=28, center=True).mean(),
}).plot();


# %% tags=["level_advanced"]
# xxx perplexing !
# ici on utilise window=Timedelta(), agrégé avec sum() 
# et donc on s'attendrait à observer
# un comportement aux bornes franchement différent

# et pourtant...

pd.DataFrame({
    'original': s,
    '??odd ends??': s.rolling(window=pd.Timedelta(28, 'D'),
                              center=True).sum(),
}).plot();


# %% tags=["level_intermediate"]
# prune-end

# %% [markdown]
# ## **exercice** `resample` et `rolling`

# %% [markdown] tags=["level_basic"]
# 8. calculez `df2` qui se concentre sur la valeur de `High` sur la période de Juillet 2018 à fin 2019  
# plottez-la  
# rangez dans la variable `L` le nombre de lignes

# %%
# à vous

# %%
# prune-begin

# %%
df2 = df.loc['2018-07' : '2019'][['High']]

# %%
df2.plot();

# %%
L = len(df2)

# %%
# prune-end

# %% [markdown] tags=["level_basic"]
# 9. appliquez à cette série un `resample()` avec la moyenne des données sur une période d'une semaine  
# plottez le résultat  
# combien d'entrées on devrait y trouver (en fonction de L) si on compare les fréquences des deux séries ?  
# pourquoi ça ne tombe pas exactement juste ?  
# est-ce qu'on pourrait estimer ça autrement ?

# %%
# à vous

# %%
# prune-begin

# %%
df_res = df2.resample('1w').mean()

df_res.plot();

# %%
# il n'y a pas de données le week-end
# donc on a en gros 5 données par semaine

expected = L // 5

# mais ça ça marche mal; il y a pas mal de trous 
# supplémentaires (jours fériés) dans les données
# et du coup L est moins élevé, notre estimation est donc inférieure
# au résultat

expected, len(df_res)

# %%
# un peu de calcul avec les dates
begin, end = df2.index[0], df2.index[-1]
begin, end

# %%
# cette fois c'est mieux
# on doit ajouter 1 car toute semaine commencée est due ;)
(end-begin) // pd.Timedelta('1w') + 1

# %%
# prune-end

# %% [markdown] tags=["level_basic"]
# 10. appliquez à cette série un `rolling()` avec une fenêtre de 1 an  
# plottez le résultat  
# combien d'entrées on devrait y trouver (en fonction de L) ?

# %%
# à vous

# %%
# prune-begin

# %%
# xxx quels paramètres pour obtenir moins d'entrées ?
df_rol = df2.rolling(window='365D').mean()

df_rol.plot();

# %%
# xxx
print(f"{L=} {len(df_rol)=}")
expected = L
expected, len(df_rol)

# %% [markdown] tags=["level_intermediate"]
# ## annexe

# %% [markdown] tags=["level_intermediate"]
# ### les échelles de précision

# %% [markdown] tags=["level_intermediate"]
# un objet `datetime64` est créé avec un paramètre *`unit`*, qui permet de choisir la précision des calculs; et l'intervalle des dates possibles varie bien entendu avec cette précision :

# %% [markdown] tags=["level_intermediate"]
# <div class=note>
#
# Unit Code |	Meaning |	Time span (relative) |	Time span (absolute) |
# -----|----------|------------------------|-----------------------|
# Y |	year | 		+/- 9.2e18 years | 	[9.2e18 BC, 9.2e18 AD]
# M |	month | 		+/- 7.6e17 years | 	[7.6e17 BC, 7.6e17 AD]
# W |	week | 		+/- 1.7e17 years | 	[1.7e17 BC, 1.7e17 AD]
# D |	day | 		+/- 2.5e16 years | 	[2.5e16 BC, 2.5e16 AD]
#   |      |                       |
# h |	hour | 		+/- 1.0e15 years | 	[1.0e15 BC, 1.0e15 AD]
# m |	minute | 	+/- 1.7e13 years | 	[1.7e13 BC, 1.7e13 AD]
# s |	second | 	+/- 2.9e11 years | 	[2.9e11 BC, 2.9e11 AD]
# ms| 	millisecond | 	+/- 2.9e8 years | 	[ 2.9e8 BC, 2.9e8 AD]
# us| 	microsecond | 	+/- 2.9e5 years | 	[290301 BC, 294241 AD]
# ns| 	nanosecond | 	+/- 292 years  |		[ 1678 AD, 2262 AD]
# ps| 	picosecond | 	+/- 106 days | 		[ 1969 AD, 1970 AD]
# fs| 	femtosecond | 	+/- 2.6 hours | 		[ 1969 AD, 1970 AD]
# as| 	attosecond | 	+/- 9.2 seconds | 	[ 1969 AD, 1970 AD]
#     
# </div>

