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
#     title: conditions et masques
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")

# %% [markdown]
# # conditions et masques

# %%
import pandas as pd
import numpy as np

# %% [markdown] tags=["framed_cell"]
# ## conditions sur une dataframe
#
# <br>
#
# dans les analyses de tables de données  
# il est fréquent de **sélectionner des données par des conditions**
#
# <br>
#
# les conditions peuvent s'appliquer, selon le contexte
#
# * à tout un tableau
# * ou à toute une colonne
# * ou à toute une ligne
# * ou à tout un sous-tableau, sous-colonne, sous-ligne
#
# <br>
#
# en `pandas`, comme en `numpy`, les fonctions sont **vectorisées**  
# par souci de rapidité du code
#
# <br>
#
# il ne faut **jamais itérer avec un `for-python`** sur les valeurs d'une table  
# (les itérations se font dans le code des fonctions `numpy` et `pandas`)
#
# <br>
#
# comme en numpy, une expression va s'appliquer à toute la structure
# et retourner une structure du même type
#
# exemple:
#
# * `titanic['Age']` : un objet de type `Series` à valeurs entières
# * `titanic['Age'] > 12` : un objet de type `Series` à valeurs booléennes
#
# (voir ci-dessous)
#

# %% [markdown]
# ***

# %% [markdown] slideshow={"slide_type": "slide"} tags=["framed_cell"]
# ## conditions et masques
#
# <br>
#
# regardons cet exemple en détail:  
# quels passagers avaient moins de 12 ans ?
#
# ```python
# df = pd.read_csv('titanic.csv', index_col='PassengerId')
#
# children = df['Age'] < 12 # l'opérateur < est vectorisé
# children
#
# -> PassengerId
#     552    False  # <- le passager de PassengerId 552 a plus de 12 ans
#     638    False
#            ...
#     326    False
#     396    False
#     832     True  # <- celui-ci par contre a strictement moins de 12 ans
#     Name: Age, Length: 891, dtype: bool
# ```
#
# <br>
#
# cette expression retourne des **booléens** - appelée **un masque**  
# dans une `pandas.Series` dont le type est naturellement `bool`  
# avec, pour chaque valeur de la colonne, la réponse au test
#
# <br>
#
# en `pandas` comme en `numpy` pour combiner les conditions  
#
# * on utilise `&` (et) `|` (ou) et `~` (non)  
# ou les `numpy.logical_and`, `numpy.logical_or`, `numpy.logical_not`
#
# * et **surtout pas** `and`, `or` et `not` (opérateurs `Python` non vectorisés)
# * on **parenthèse toujours** les expressions
#
# ```python
# girls = (df['Age'] < 12) & (df['Sex'] == 'female')
# girls.sum()
# -> 32
# ```
#
# <div class=note>
#     
#   c'est **très important** de bien mettre des parenthéses car les opérateurs bitwise (`&` et
#     autres) ont des  
#   précédences (priorités) qui sont non intuitives, et très différentes des opérateurs logiques (`and` et autres)
#     
# </div>
#
# <br>
#
# on pourra ensuite utiliser ces tableaux de booléens  
#
# * pour leur appliquer des fonctions  
# * comme des masques pour sélectionner des sous-tableaux
#
#

# %%
# le code
df = pd.read_csv('titanic.csv', index_col='PassengerId')
children = df['Age'] < 12
children

# %%
children.dtype

# %% scrolled=false
girls = (df['Age'] < 12) & (df['Sex'] == 'female')
girls.sum()

# %% [markdown] tags=["framed_cell"] slideshow={"slide_type": "slide"}
# ## `value_counts()`
#
# comment calculer le nombre d'enfants ?  
# par exemple nous pouvons sommer les `True` avec `pandas.Series.sum`
#
# ```python
# children = df['Age'] < 12
# children.sum()
# -> 68
# ```
#
# <br>
#
# ou utiliser la méthode `value_counts()`  
# qui compte les occurrences dans une colonne  
#
# ```python
# children = df['Age'] < 12
# children.value_counts()
# -> False    823
#    True      68
#    Name: Age, dtype: int64
# ```
#
# la méthode vous indique la colonne `Age` et son type `int64`
#
# <br>
#
# ainsi parmi les passagers dont on connait l'âge  
# `68` passagers,  ont moins de `12` ans  
# on reviendra tout de suite sur les données manquantes 

# %%
children.sum()

# %%
children.value_counts()

# %% [markdown]
# ## valeurs manquantes

# %% [markdown] tags=["framed_cell"]
# ### contexte général
#
# <br>
#
# souvent, certaines colonnes ont des valeurs manquantes...  
# dans l'exemple du Titanic, ce sont les valeurs qui ne sont pas renseignées dans le `csv`  
#
# <br>
#
# on a souvent besoin de les trouver, les compter, et si nécessaire les éliminer
#
# <br>
#
# `NA` signifie Non-Available et `NaN` Not-a-Number
#
# <br>
#
# sur les `DataFrame` et les `Series`  
# la méthode `isna()` construit **un masque**  
# du même type (DataFrame ou Series donc), 
# et à valeurs booléennes  où
#
# * `True` signifie que la valeur est manquante
# * `False` que la valeur ne l'est pas
#
# <br>
#
# il existe son contraire qui est `notna()`  
# il existe aussi des synonymes `isnull()` et `notnull()` - **préférez** `isna`
#

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### valeurs manquantes dans une colonne
#
# <br>
#
# regardons les valeurs manquantes d'une colonne
#
# ```python
# df['Age'].isna()
# ->  PassengerId
#     552    False
#     638    False
#     499    False
#     261     True
#     395    False
#            ...
#     396    False
#     832    False
#     Name: Age, Length: 891, dtype: bool
# ```
#
# <br>
#
# l'age du passager d'`Id` 261 est manquant  
# on peut le vérifier dans le fichier en format `csv`:
#
# ```
# 261,0,3,"Smith, Mr. Thomas",male,,0,0,384461,7.75,,Q
#                                 ^^
# ```
#
# <br>
#
# combien d'ages sont manquants ?
#
# ```python
# df['Age'].isna().sum()
# -> 177
# ```
#
# on y reviendra

# %% scrolled=true
# le code
df['Age'].isna()

# %%
df['Age'].isna().sum()


# %%
# remarquez qu'on peut tout aussi bien
# utiliser le sum() de np ou de Python
import numpy as np
np.sum(df['Age'].isna()), sum(df['Age'].isna())

# %% [markdown] tags=["framed_cell"]
# ### valeurs manquantes sur une dataframe
#
# <br>
#
# la méthode `isna()` s'applique aussi à une dataframe  
# et elle retourne une **dataframe de booléens** où - sans surprise :  
#
# * `True` signifie que la valeur est manquante
# * `False` que la valeur ne l'est pas
#
# <br>
#
# regardons les valeurs manquantes d'une dataframe
#
# ```python
# df.isna()
# ->              Survived  Pclass   Name    Sex  ...  Ticket   Fare  Cabin  Embarked
# PassengerId                                  ...
# 552             False   False  False  False  ...   False  False   True     False
# 638             False   False  False  False  ...   False  False   True     False
# 499             False   False  False  False  ...   False  False  False     False
# 261             False   False  False  False  ...   False  False   True     False
# 395             False   False  False  False  ...   False  False  False     False
# ...               ...     ...    ...    ...  ...     ...    ...    ...       ...
# 463             False   False  False  False  ...   False  False  False     False
# 287             False   False  False  False  ...   False  False   True     False
# 326             False   False  False  False  ...   False  False  False     False
# 396             False   False  False  False  ...   False  False   True     False
# 832             False   False  False  False  ...   False  False   True     False
#
# [891 rows x 11 columns]
# ```
#
# <br>
#
# vous remarquez une dataframe de la **même taille** que `df`

# %%
# le code
df.isna()

# %% [markdown] tags=["framed_cell"]
# ### compter les valeurs manquantes
#
# <br>
#
# comme en `numpy` je peux appliquer une fonction - ici `sum()` - en précisant l'`axis`  
# `0` on applique la fonction dans l'axe des lignes (le défaut)  
# `1` on applique la fonction dans l'axe des colonnes  
# l'objet retourné est une série contenant le résultat de la fonction
#
# <br>
#
# exemple avec la somme (`sum`) des valeurs manquantes sur l'axe des lignes `axis=0`  
# qui `sum` les lignes entre elles - le résultat est par colonne donc
#
# ```python
# df.isna().sum()       # les deux formes sont 
# df.isna().sum(axis=0) # équivalentes
#
# Survived      0
# Pclass        0
# Name          0
# Sex           0
# Age         177
# SibSp         0
# Parch         0
# Ticket        0
# Fare          0
# Cabin       687
# Embarked      2
# dtype: int64
# ```
# <div class=note>
#
# pour souligner une différence avec `numpy`: comparez le comportement
# * de `array.sum()`
# * et `df.sum()`
#
# </div>
#
# <br>
#
# nous remarquons des valeurs manquantes dans les colonnes `Cabin`, `Age` et `Embarked`

# %% [markdown] tags=["framed_cell"]
# ### dans l'autre direction (axis=1)
#
# <br>
#
# exemple de la somme des valeurs manquantes sur l'axe des colonnes - par personne donc
#
# ```python
# df.isna().sum(axis=1):
# ->  PassengerId
#     552    1
#     638    1
#     499    0
#     261    2
#     395    0
#           ..
#     463    0
#     287    1
#     326    0
#     396    1
#     832    1
#     Length: 891, dtype: int64
# ```
# <br>
#
# le passager d'id `261` a deux valeurs manquantes

# %%
# le code
df.isna().sum()       # c'est la 
df.isna().sum(axis=0) # même chose

# %% scrolled=false
# le code
df.isna().sum(axis=1)

# %% [markdown] tags=["framed_cell"]
# ### utilisation des fonctions `numpy`
#
# <br>
#
# les méthodes `numpy` s'appliquent sur des `pandas.DataFrame` et des `pandas.Series`
#
# <br>
#
# on précise l'`axis`  
# `0` pour l'axe des lignes (c'est le mode par défaut)  
# `1` pour l'axe des colonnes  
#
# <br>
#
# différence avec `numpy`, si on appelle sans préciser `axis`
#
# * avec **numpy**: on obtient le résultat **global**  
# * avec **pandas**: par défaut `axis=0`, on agrège sur l'axe des lignes (par colonne)
#
# <br>
#
# **si on désire le résultat global**
# 1. soit on applique la fonction deux fois  
#    e.g. `df.isna().sum().sum()`
# 1. soit on peut passer par le sous-tableau `numpy`  
#   et là la fonction `numpy.sum()` donnera le résultat global
#
# <br>
#
# la méthode `pandas.DataFrame.to_numpy` retourne le tableau `numpy.ndarray` de la DataFrame `pandas`
#
# ```python
# df.isna().to_numpy()
# -> array([[False, False, False, ..., False,  True, False],
#           [False, False, False, ..., False, False, False],
#           ...,
#           [False, False, False, ..., False,  True, False],
#           [False, False, False, ..., False,  True, False]])
# ```
#
# <br>
#
# on somme
#
# ```python
# np.sum(df.isna().to_numpy())
# df.isna().to_numpy().sum()
# -> 866
# ```
#
# il y a `866` valeurs manquantes dans toute la data-frame
#
# <div class=note>
#     
# remarque: contrairement à ce qu'on avait vu en `numpy`, ici on ne pourrait pas faire `df.isna().sum(axis=(0, 1))`
#     
# </div>    

# %%
df.isna().sum().sum()

# %%
# le code
df.isna().to_numpy()

# %%
# le code
np.sum(df.isna().to_numpy())
df.isna().to_numpy().sum()

# %% [markdown]
# ***

# %% [markdown]
# ## **exercice** valeurs uniques

# %% [markdown]
# 1. lisez la data-frame du titanic `df`

# %% slideshow={"slide_type": ""}
# à vous

# %%
# prune-cell 1.

df = pd.read_csv("titanic.csv")


# %% [markdown]
# 2. utilisez la méthode `pd.Series.unique` (1) pour compter le nombre de valeurs uniques  
# des colonnes `'Survived'`, `'Pclass'`, `'Sex'` et `'Embarked'`  
# vous pouvez utiliser un for-python pour parcourir la liste `cols` des noms des colonnes choisies

# %%
# à vous

# %%
# prune-cell 2.

cols = ['Survived', 'Pclass', 'Sex', 'Embarked']
for c in cols:
    print(f"{c} unique values: {df[c].unique()}")


# %% [markdown]
# 3. utilisez l'expression `df[cols]` pour sélectionner la sous-dataframe réduite à ces 4 colonnes

# %%
# à vous

# %%
# prune-cell
minidf = df[cols]

# %% [markdown]
# 4. utilisez l'attribut `dtypes` des `pandas.DataFrame` pour afficher le type de ces 4 colonnes

# %%
# à vous

# %%
# prune-cell
# une type de catégorie
minidf.dtypes


# %%
# prune-cell 4.
# du coup on pourrait faire
for c in minidf.columns:
    print(f"column {c:>12} has type {minidf.dtypes[c]} =?= {df[c].dtype}")


# %% [markdown]
# 5. que constatez-vous ?  
# quel type serait plus approprié pour ces colonnes ?
#
# (1) servez-vous du help `pd.Series.unique?`

# %%
# à vous

# %% [markdown]
# prune-cell 5.
#
# * la colonne Survived pourrait être un booléen
# * les trois autres colonnes sont des catégories (nombre fini de valeurs possibles)

# %% [markdown]
# ***

# %% [markdown]
# ## **exercice** conditions

# %% [markdown]
# 1. lisez la data-frame des passagers du titanic

# %%
# à vous

# %%
# prune-cell 1.
df = pd.read_csv('titanic.csv', index_col='PassengerId')
# df.isna().to_numpy().sum(), df.isna().sum(axis=1), df.isna().sum(axis=0),

# %% [markdown]
# 2. calculez les valeurs manquantes: totales, des colonnes et des lignes

# %%
# prune-cell 2.

print(10*'-', 'par colonne')
print(df.isna().sum())
print(10*'-', 'par ligne')
print(df.isna().sum(axis=1))
print(10*'-', 'total')
print(df.isna().sum().sum())

# %% [markdown]
# 3. calculez le nombre de classes du bateau

# %%
# prune-cell 3.
len(df['Pclass'].unique())

# %% [markdown]
# 4. calculez le taux d'hommes et de femmes

# %%
# prune-cell 4.
df['Sex'].value_counts()/len(df)

# %% [markdown]
# 5. calculez le taux de personnes entre 20 et 40 ans

# %%
# prune-cell 5.
((df['Age'] >= 20) & (df['Age'] <= 40)).sum()/len(df)

# %% [markdown]
# 6. calculez le taux de survie des passagers

# %%
# prune-cell 6.
print(df['Survived'].value_counts()/len(df))

# le taux de survie
(df['Survived'].value_counts()/len(df))[1]

# %% [markdown]
# 7. calculez le taux de survie des hommes et des femmes par classes  
# on reverra ces décomptes d'une autre manière

# %%
# prune-cell 7.

# classe
cls = 1

# nb d'hommes
pass_h_cls = ((df['Sex'] == 'male') & (df['Pclass'] == cls)).sum()

# nb de femmes
pass_f_cls = ((df['Sex'] == 'female') & (df['Pclass'] == cls)).sum()

# taux survie homme, femme de classe cls
(   ((df['Sex'] == 'male') & (df['Survived'] == 1) & (df['Pclass'] == cls)).sum()/pass_h_cls,
    ((df['Sex'] == 'female') & (df['Survived'] == 1) & (df['Pclass'] == cls)).sum()/pass_f_cls )


# %%
# prune-cell

c1 = (df['Pclass'] == 1).sum()
c2 = (df['Pclass'] == 2).sum()
c3 = (df['Pclass'] == 3).sum()


# %%
# prune-cell

(   ((df['Sex'] == 'female') & (df['Survived'] == 1) & (df['Pclass'] == 1)).sum()/c1,
    ((df['Sex'] == 'male') & (df['Survived'] == 1) & (df['Pclass'] == 1)).sum()/c1     )
