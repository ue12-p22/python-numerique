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
# **note** on n'utilise pas directement ces deux types en numpy/pandas, mais c'est tout de même la fondation du modèle, donc attardons-nous un tout petit peu

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

t2 = d1 + t1
t2

# %%
t2 - 2 * d1

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
# pour une liste des formats, voir *pour en savoir plus* à la fin de ce notebook

# %%
# # %H c'est pour extraire l'heure
# il y a toute une série de codes de format...
f"{t1:%H==%M}"

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
# et en effet, du coté `pandas` on dispose de 3 types:
#
# * `Timestamp` pour un instant (ça aurait pu/dû s'appeler `Datetime`, mais bon...)
# * `Timedelta` pour une durée
# * `Period` pour un intervalle de temps, représenté par un début **et** une durée
#
# tous ces types sont fabriqués *au dessus* des 2 types de base fournis par `numpy`, et visent principalement à les rendre plus faciles à utiliser

# %% [markdown]
# ## exercice: `pd.to_datetime()`

# %% [markdown]
# vous avez peut-être remarqué que `read_csv` propose des (tas d') options pour la gestion des instants (notamment le paramètre `parse_dates`); toutefois j'ai envie de vous conseiller de rester loin de ce genre de features, au moins pour commencer

# %%
# # pd.read_csv?

# %% [markdown]
# il est sans doute préférable de procéder en deux temps, en combinant `pd.read_csv` et `pd.to_datetime`, ce que je vous invite à faire dans cet exercice

# %%
# # pd.to_datetime?

# %% [markdown] tags=["level_basic"]
# 0. lire le fichier de données `Amazon.csv` avec `read_csv()`  
# affichez les types des colonnes

# %%
# prune-cell
# cols = ['Date', 'High', 'Low']

# %%
# à vous

# %%
# prune-cell
#df = pd.read_csv('Amazon.csv', usecols=cols)
df = pd.read_csv('Amazon.csv')
df.head()

# %% [markdown] tags=["level_basic"]
# 1. traduisez la colonne `Date` dans le type adéquat  
# affichez le nouveau type de la colonne  
# ça peut être intéressant de regarder à la fois `dtypes` sur la dataframe et `dtype` sur la série

# %%
# à vous

# %%
# prune-begin
df['Date'] = pd.to_datetime(df.Date)

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

# %%
# prune-end

# %% [markdown] tags=["level_basic"]
# 2. utilisez la colonne `Date` comme index

# %%
# à vous

# %%
# prune-cell
df.set_index('Date', inplace=True)
df.head()

# %% [markdown] tags=["level_basic"]
# 3. plottez la valeur de l'action au cours du temps
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
# * df[col] est une série
# * df[[col]] est une dataframe
#

# %%
for col in cols:
    df[[col]].plot()

# %%
# prune-end

# %% [markdown]
# ## `NaT` = not a time
#
# utiliser dropna() pour nettoyer

# %% [markdown]
# ## l'accessor `.dt`

# %% [markdown]
# ## slicing

# %% [markdown]
# ## aggrégations avec `resample()` et `rolling()`

# %% [markdown]
# ## arrangements avec `shift()`, `asfreq()`

# %% [markdown]
# ## annexes

# %% [markdown]
# ### pour en savoir plus
#
# * pour une liste complète des codes de formats disponibles dans les f-strings, voir  
#   <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>
#
# * la doc sur les type numpy  
#   <https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64>

# %% [markdown]
# ### les échelles de précision

# %% [markdown]
# un objet `datetime64` est créé avec un paramètre *`unit`*, qui permet d choisir la précision des calculs; et l'intervalle des dates possibles varie bien entendu avec cette précision :

# %% [markdown]
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

