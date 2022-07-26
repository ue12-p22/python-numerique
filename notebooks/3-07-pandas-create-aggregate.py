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
#     title: manipulations de base
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %% [markdown]
# # manipulations de base

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# ## création de dataframe
#
# de très nombreuses voies sont possibles pour créer une dataframe par programme  
# en voici quelques-unes à titre d'illustration  
# voyez la documentation de `pd.DataFrame?` pour les détails  

# %% [markdown] tags=["framed_cell"]
# ### à partir du dict Python des colonnes
#
# <br>
#
# avec la méthode `pandas.DataFrame`  
# on peut créer un objet de type `pandas.DataFrame`
#
# <br>
# le dictionnaire des colonnes
#
# ```python
# cols_dict = {'names' : ['snail', 'pig', 'elephant', 'rabbit',
#                         'giraffe', 'coyote', 'horse'],
#              'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
#              'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }
# ```
#
# <br>
# création de la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(cols_dict)
# df
#
# ->  names     speed   lifespan
# 0    snail    0.1     2.0
# 1    pig      17.5    8.0
# 2    elephant 40.0    70.0
# 3    rabbit   48.0    1.5
# 4    giraffe  52.0    25.0
# 5    coyote   69.0    12.0
# 6    horse    88.0    28.0
# ```

# %%
# le code
import pandas as pd
import numpy as np
cols_dict = {'names' : ['snail', 'pig', 'elephant', 'rabbit',
                        'giraffe', 'coyote', 'horse'],
             'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
             'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }

df = pd.DataFrame(cols_dict)
df

# %% [markdown] tags=["framed_cell"]
# ### à partir du `dict` des colonnes et d'une `list` (d'index) des lignes
#
# <br>
#
# avec la méthode `pandas.DataFrame`
#
# <br>
#
# le `dictionnaire` des id des colonnes  
# la `liste` des id des lignes
#
# ```python
# cols_dict = {'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
#              'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }
#
# line_ids =  ['snail', 'pig', 'elephant', 'rabbit',
#              'giraffe', 'coyote', 'horse']
# ```
#
# <br>
#
# création de la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(cols_dict, index = line_ids)
# df
# ->       speed   lifespan
# snail    0.1     2.0
# pig      17.5    8.0
# elephant 40.0    70.0
# rabbit   48.0    1.5
# giraffe  52.0    25.0
# coyote   69.0    12.0
# horse    88.0    28.0
# ```
#
# <br>
#
# on peut ne pas lui passer la liste des id des lignes

# %%
cols_dict = {'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
             'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }

line_ids =  ['snail', 'pig', 'elephant', 'rabbit',
             'giraffe', 'coyote', 'horse']

df = pd.DataFrame(cols_dict, index = line_ids)
df.values

# %% [markdown] tags=["framed_cell"]
# ### à partir d'un `numpy.ndarray`
#
# <br>
#
# avec la méthode `pandas.DataFrame`
#
# <br>
#
# à partir d'un `numpy.ndarray` qui décrit la *table désirée*  
# attention à la forme
#
# <br>
#
# et attention au `type`  
# le type des éléments d'un `numpy.ndarray` est homogène  
# (si vous mélangez des `float` et des `str` vous n'avez plus que des string à-la-`numpy`...)
#
# <br>
#
# le `numpy.ndarray`
#
# ```python
# nd = np.array([[ 0.1,  2. ],
#                [17.5,  8. ],
#                [40. , 70. ],
#                [48. ,  1.5],
#                [52. , 25. ],
#                [69. , 12. ],
#                [88. , 28. ]])
#
# ```
#
# <br>
#
# la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(nd)
# df
# ->    0     1
# 0    0.1   2.0
# 1   17.5   8.0
# 2   40.0  70.0
# 3   48.0   1.5
# 4   52.0  25.0
# 5   69.0  12.0
# 6   88.0  28.0
# ```
#
# <br>
#
# **remarquez**, sans index
#
# * les index des `2` colonnes sont leurs indices `0` à `1`
# * les index des `7` lignes sont leurs indices `0` à `6`
#
# <br>
#
# on peut passer les index (colonnes et/ou lignes)  
# au constructeur de la `pandas.DataFrame`
#
# ```python
# df = pd.DataFrame(nd,
#                   index=['snail', 'pig', 'elephant',
#                          'rabbit', 'giraffe', 'coyote', 'horse'],
#                   columns = ['speed', 'lifespan'])
# df
# ->       speed   lifespan
# snail    0.1     2.0
# pig      17.5    8.0
# elephant 40.0    70.0
# rabbit   48.0    1.5
# giraffe  52.0    25.0
# coyote   69.0    12.0
# horse    88.0    28.0
# ```

# %%
# le code
nd = np.array([[ 0.1,  2. ],
               [17.5,  8. ],
               [40. , 70. ],
               [48. ,  1.5],
               [52. , 25. ],
               [69. , 12. ],
               [88. , 28. ]])

df = pd.DataFrame(nd)
df

# %%
# le code
nd = np.array([[ 0.1,  2. ],
               [17.5,  8. ],
               [40. , 70. ],
               [48. ,  1.5],
               [52. , 25. ],
               [69. , 12. ],
               [88. , 28. ]])

df = pd.DataFrame(nd,
                  index=['snail', 'pig', 'elephant',
                         'rabbit', 'giraffe', 'coyote', 'horse'],
                  columns = ['speed', 'lifespan'])
df['Names'] = df.index
df.values

# %% [markdown]
# ### **exercice** : création de df et type des éléments

# %% [markdown]
# 1. créer un `numpy.ndarray` à partir de la liste suivante
# ```python
# animals = [['snail', 0.1, 2.0],
#            ['pig', 17.5, 8.0],
#            ['elephant', 40.0, 70.0],
#            ['rabbit', 48.0, 1.5],
#            ['giraffe', 52.0, 25.0],
#            ['coyote', 69.0, 12.0],
#            ['horse', 88.0, 28.0]]
# ```
# 1. Affichez le type des éléments de la table  
# Que constatez-vous ? (U = Unicode)
# <br>
#
# 1. Créez une `pandas.DataFrame` à partir de la table précédente  
# avec pour noms de colonnes `'names'`, `'speed'` et `'lifespan'`
# <br>
#
# 1. affichez la valeur et le type du `'lifespan'` de l'éléphant  
# Que constatez-vous ?  
# (`object` signifie ici `str`)
# <br>
#
# 1. affichez la valeur et le type du `'names'` de l'éléphant  
# Que constatez-vous ?
# <br>
#
# 1. avec `loc` ou `iloc`, modifiez la valeur `elephant` par `'grey elephant'`  
# affichez la valeur et le type du `'names'` de l'éléphant  
# un constat ?
# <br>
#
# 1. affichez le type des colonnes  
# utilisez l'attribut `dtypes` des `pandas.DataFrame`
# <br>
#
# 1. avec la méthode `pandas.DataFrame.to_numpy`  
# affichez le tableau `numpy` sous-jacent de votre data-frame  
# affichez le type du tableau  
# que constatez-vous ?
# <br>
#
# 1. modifiez les colonnes `'speed'` et `'lifespan'` de manière à leur donner le type `float`  
# (utilisez `pandas.Series.astype` voir les **rappels** en fin de cellule)
# <br>
#
# **rappel**
#
# * `astype`  
# la méthode `pandas.Series.astype`, à laquelle vous indiquez un type `float`  
# crée (si c'est possible) une nouvelle `pandas.Series` dont les éléments sont de type `float`
# <br>
#
# * rajouter ou modifier une colonne dans une `pandas.DataFrame`  
# revient à modifier ou rajouter une clé à un `dict`
#
# **explication**
#
# * quand les types des colonnes `numpy` ne sont pas homogènes  
# `numpy` met un tableau de caractères `Unicode` de la *plus grande taille*
#
# * quand les types des colonnes `pandas` ne sont pas homogènes  
# sans indication, `pandas` met `str` `Python`
#
# * quand dans une data-frame `pandas` on mélange des types de colonnes - genre `float` et `str`  
# `pandas` et son tableau `numpy` sous-jacent indiqueront `O` ou `object`  
# pour **mixed data types in columns**

# %% [markdown] tags=["framed_cell"]
# ## agrégations des données
#
# parfois on obtient les données par plusieurs canaux  
# qu'il faut agréger dans une seule dataframe
#
# <br>
#
# les outils à utiliser pour cela sont multiples  
# pour bien choisir, il est utile de se poser en priorité  
# la question de savoir si les différentes sources à assembler  
# concernent les **mêmes colonnes** ou au contraire les **mêmes lignes**  (*)
#   
# <br>
# illustrations:
#
# * on recueille les données à propos du coronavirus, qui sont disponibles par mois  
#   chaque fichier a la même structure - disons 2 colonnes: *deaths*, *confirmed*  
#   l'assemblage consiste donc à agréger les dataframes **en hauteur**
#   
# * on recueille les notes des élèves d'une classe de 20 élèves  
#   chaque prof fournit un fichier excel avec les notes de sa matière  
#   chaque table contient 20 lignes  
#   il faut cette fois agréger les dataframes **en largeur**
#   
# <div class="note">
#     (*) cette présentation est simpliste, elle sert uniquement à fixer les idées
# </div>

# %% [markdown] tags=["framed_cell"]
# ### en hauteur `pd.concat()`
#
# pour l'accumulation de donnée référez-vous  
# aux fonctions suivantes offertes par `pandas`
#
# * la fonction `pd.concat([df1, df2, ..])`  
#   qui a vocation à accumuler des données en hauteur  
#
# * et à la méthode `df1.append(df2)`   
#   qui est une version simplifiée de `concat()`

# %% [markdown] tags=["framed_cell"]
# ### en largeur `pd.merge()`
#
# pour la réconciliation de données, voyez cette fois
#
# * la fonction `pd.merge(left, right)`  
#   ou sous forme de méthode `left.merge(right)`  
#
# * et à la méthode `left.join(right)`
#   une version simplifiée de `left.merge()`

# %% [markdown]
# ### alignements
#
# dans les deux cas, `pandas` va *aligner* les données  
# par exemple on peut concaténer deux tables qui ont les mêmes colonnes  
# même si elles sont dans le désordre
#
# l'usage typique de `merge()`/`join()`  
# est l'équivalent d'un JOIN en SQL  
# pour ceux à qui ça dit quelque chose  
# sans indication, `merge()` calcule les **colonnes communes**  
# et se sert de ça pour aligner les lignes
#

# %%
# exemple 1
# les deux dataframes ont exactement une colonne en commun

df1 = pd.DataFrame(
    data={
        'name': ['Bob', 'Lisa', 'Sue'],
        'group': ['Accounting', 'Engineering', 'HR']})  # une seule colonne

df2 = pd.DataFrame(
    data={
        'name': ['Lisa', 'Bob', 'Sue'],
        'hire_date': [2004, 2008, 2014]})

# %% cell_style="split"
df1

# %% cell_style="split"
df2

# %%
df1.merge(df2)

# %%
# exemple 2
# cette fois il faut aligner l'index de gauche 
# avec la colonne 'name' à droite

df1 = pd.DataFrame(
    index = ['Bob', 'Lisa', 'Sue'],  # l'index
    data={'group': ['Accounting', 'Engineering', 'HR']})  # une seule colonne

df2 = pd.DataFrame(
    data = {'name': ['Lisa', 'Bob', 'Sue'],
            'hire_date': [2004, 2008, 2014]})

# %% cell_style="split"
df1

# %% cell_style="split"
df2

# %%
# du coup ici sans préciser de paramètres
# ça ne fonctionnerait pas
df1.merge(df2, left_index=True, right_on='name')

# %% [markdown] tags=["level_intermediate"]
# ### `concat()` *vs* `merge()`
#
# les deux fonctionnalités sont assez similaires sauf que
#
# * `merge` peut aligner les index ou les colonnes  
#   alors que `concat` ne considère que les index
#
# * `merge` est une opération minaire  
#    alors que `concat` est n-aire  
#    ce qui explique d'ailleurs la différence de signatures  
#    `concat([d1, d2])` *vs* `merge(d1, d2)`
#
# * seule `concat()` supporte un paramètre `axis=` 

# %% [markdown]
# ### **exercice** - collage de datatables
#
# voici 3 jeux de données qu'on vous demande d'assembler  
# pour décrire à la fin 4 caractéristiques à propos de 5 élèves

# %% cell_style="split"
df1 = pd.read_csv('pupils1.csv')
df1

# %% cell_style="split"
df2 = pd.read_csv('pupils2.csv')
df2

# %%
df3 = pd.read_csv('pupils3.csv')
df3

# %%
# votre code

# %% [markdown] tags=["level_intermediate"]
# ### **exercice** - intermédiaire
#
# l'énoncé est le même, sauf que cette fois on a choisi
# d'indexer toutes les tables par la colonne `name`

# %% cell_style="split" tags=["level_intermediate"]
df1i = pd.read_csv('pupils1.csv',
                  index_col='name')
df1i

# %% cell_style="split" tags=["level_intermediate"]
df2i = pd.read_csv('pupils2.csv',
                  index_col='name')
df2i

# %% tags=["level_intermediate"]
df3i = pd.read_csv('pupils3.csv', index_col='name')
df3i

# %% tags=["level_intermediate"]
# votre code

