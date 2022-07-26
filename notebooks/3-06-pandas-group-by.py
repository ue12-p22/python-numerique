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
#     title: "regrouper par crit\xE8res"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %% [markdown]
# # regrouper par critères

# %% [markdown]
# ## les données et les librairies

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('titanic.csv', index_col=0)
df.head(3)

# %% [markdown] {"tags": ["framed_cell"]}
# ## introduction
#
# <br> 
#
# en `pandas`, une table de données (encore appelée *dataframe*) a uniquement 2 dimensions
#
# <br>
#
# mais elle peut indiquer, avec ces deux seules dimensions, des sous-divisions dans les données
#
# <br>
#
# les passagers du Titanic sont ainsi divisés
#
# * en homme/femme par la colonne `Sex`
# * en passagers de première, seconde ou troisième classe par la colonne `Pclass`
# * en survivants ou décédés par la colonne `Survived`
# * on pourrait même les diviser en classe d'âge par la colonne `Age`  
#    *enfants* (avant 12 ans), *jeunes* (entre 12 et 20), *adultes* (entre 20 et 60), *personne agées* (+ de 60 ans)
#
# <br>
#
# des analyses mettant en exergue ces groupes de personnes peuvent être intéressantes
#
# <br>
#
# lors du naufrage du Titanic, valait-il mieux être une femme en première classe ou un enfant en troisième ?
#
# <br>
#
# on va calculer des regroupements (partitions)  
# en utilisant la méthode `pandas.DataFrame.groupby`  
# à laquelle on indique un ou plusieurs critères.

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell"]}
# ## groupement par critère unique
#
# <br>
#
# le groupement (la partition) se fait par la méthode `pandas.DataFrame.groupby`
#
# <br>
#
# prenons le seul critère de genre des passagers  
# de la colonne `Sex`
#
# <br>
#
# la colonne a deux valeurs: `female` et `male`
#
# ```python
# df['Sex'].unique()
# -> array(['male', 'female'], dtype=object)
# ```
#
# <br>
#
# `pandas` permet de partitionner la dataframe  
# en autant de sous-dataframes que de valeurs uniques dans la colonne
#
# <br>
#
# faisons la partition de notre dataframe en
#
# * la sous-dataframe des hommes i.e. `male`
# * la sous-dataframe des femmes i.e. `female`
# * nous pourrons alors procéder à des analyses différenciées par genre
#
# <br>
#
# partition par (`by`) l'unique colonne `Sex`  
# ```python
# by_sex = df.groupby(by='Sex')
# ```
#
# <br>
#
# l'objet rendu par la méthode est de type `pandas.DataFrameGroupBy`

# %%
# le code
df['Sex'].unique()

# %%
# le code
by_sex = df.groupby(by='Sex')
by_sex

# %% [markdown] {"tags": ["framed_cell"]}
# ### accès aux sous-dataframes
#
# <br>
#
# la méthode `pandas.DataFrameGroupBy.size`  
# donne la taille des deux partitions  
# (dans un objet de type `pandas.Series`)
#
# ```python
# by_sex.size()
# -> Sex
# female    314
# male      577
# dtype: int64
# ```
#
# <br>
#
# l'objet `pandas.DataFrameGroupBy` est un objet **itérable**  
# qui vous donne les couples `key, dataframe`
#
# ```python
# for group, subdf in by_sex:
#     print(group, subdf.shape) # v est de type pandas.DataFrame
#
# -> female (314, 11)
#    male (577, 11)
# ```
#
# <br>
#
# vous pouvez donc facilement parcourir toutes les sous-dataframes 

# %%
# les tailles des morceaux
by_sex.size()

# %%
# les tailles des morceaux : la somme est correcte
sum(by_sex.size()) == len(df)

# %%
# pour itérer 'à la main'
for group, subdf in by_sex:
    print(group, subdf.shape)

# %% [markdown] {"tags": ["framed_cell"]}
# ### proxying : propagation sur les sous-df
#
# <br>
#
# itérer est intéressant d'un point de vue pédagogique  
# pour bien comprendre la nature d'un objet `DataFrameGroupBy`  
# et éventuellement inspecter son contenu de visu  
#
# <br>
#
# mais en pratique, on peut souvent utiliser une méthode des dataframes  
# **directement** sur l'objet `DataFrameGroupBy` et il est rarement  
# nécessaire d'itérer explicitement dessus  
# (on n'aime pas avoir à écrire un for-Python)
#
# <br> 
#
# dans ce cas l'objet `DataFrameGroupBy` se comporte comme un *proxy*  
# il propage le traitement à ses différents morceaux  
# et s'arrange pour combiner les résultats
#
# <br> 
#
# par exemple on peut extraire une colonne sur toutes les sous-dataframe  
# en utilisant la syntaxe `group[colonne]`, et faire des traitements sur le résultat
#
# ```python
# # quel age ont le plus vieil homme et la plus vieille femme
# by_sex['Age'].max()
# ```
#
# ou encore on peut fabriquer une dataframe qui contient les sommes
# des colonnes de départ, mais par sexe
#
# ```python
# # les sommes des colonnes, mais par sexe 
# by_sex.sum()
# ```

# %%
# souvent on traite un groupby comme une dataframe
# ce qui a l'effet d'appliquer l'opération (ici ['Age'])
# à toutes les sous-dataframe
by_sex.Age.max()

# %%
by_sex.sum()

# %% [markdown] {"tags": ["framed_cell"]}
# ### accéder à un groupe
#
# <br>
#
# on a parfois besoin d'accéder à un groupe précis dans la partition  
# c'est possible avec la méthode `get_group()`  
# qui retourne une dataframe
#
# ```python
# by_sex.get_group('female')
# ```

# %%
by_sex.get_group('female')

# %% [markdown] {"tags": ["framed_cell"]}
# ## groupement multi-critères
#
# <br>
#
# pour des partitions multi-critères  
# passez à `pandas.DataFrame.groupby` une **liste des colonnes**
#
# <br>
#
# la méthode `pandas.DataFrame.groupby`
#
# * calcule les valeurs distinctes de chaque colonne (comme dans le cas du critère unique)
# * mais ensuite il en fait le **produit cartésien**
# * on obtient ainsi les clés des groupes sous la forme de tuples
#
# <br>
#
# prenons les critères `Pclass` et`Sex`
#
# * le premier critère a trois valeurs `1`, `2` et `3` (pour les trois classes de cabines)
# * le second a 2 valeurs `female` et `male`
#
# <br>
#
# on s'attend donc aux 6 clés  
# `(1, 'female')`, `(1, 'male')`  
# `(2, 'female')` `(2, 'male')`  
# `(3, 'female')` `(3, 'male')`  
# (ou du moins à un sous-ensemble de ces 6 clés)
#
# <br>
#
# on regroupe
#
# ```python
# by_class_sex = df.groupby(['Pclass', 'Sex'])
# ```
# <br>
#
# utilisons `size()` pour voir les clés du groupement  
# ici tous les cas du produit cartésien sont représentés
#
# ```python
# by_class_sex.size()
# ->
# Pclass  Sex
# 1       female     94
#         male      122
# 2       female     76
#         male      108
# 3       female    144
#         male      347
# dtype: int64
# ```
#
# <br>
#
# nous découvrons là une `pandas.Series` avec un **`index` composé**  
# qu'en pandas on appelle **un *MultiIndex***

# %% {"scrolled": true}
# le code
by_class_sex = df.groupby(['Pclass', 'Sex'])
by_class_sex.size()

# %% [markdown] {"tags": ["framed_cell"]}
# ### multi-index pour les multi-critères
#
# <br>
#
# inspectons de plus près l'index qui est en jeu ici  
# partons du résultat de `by_class_sex.size()` qui est une `pandas.Series`
#
# ```python
# type(by_class_sex.size())
# -> pandas.core.series.Series
# ```
# <br>
#
# son `index` est un `MultiIndex`
#
# ```python
# df_by_class_sex.size().index
# ->
# MultiIndex([(1, 'female'),
#             (1,   'male'),
#             (2, 'female'),
#             (2,   'male'),
#             (3, 'female'),
#             (3,   'male')],
#            names=['Pclass', 'Sex'])
#
# ```
#
# <br>
#
# les index sont les tuples du produit cartésien  
# on aurait pu aussi les calculer par une compréhension Python comme ceci
# ```python
# {(i, j) for i in df['Pclass'].unique() for j in df['Sex'].unique()}
# ->
# {(3, 'male'),
#  (3, 'female'),
#  (1, 'male'),
#  (1, 'female'),
#  (2, 'male'),
#  (2, 'female')}
# ```

# %%
# le code
type(by_class_sex.size())


# %%
df.groupby(['Pclass', 'Sex']).size().index

# %%
# le code
computed_index = {(i, j) for i in df['Pclass'].unique() for j in df['Sex'].unique()}
computed_index

# %%
# pour vérifier
computed_index == set(df.groupby(['Pclass', 'Sex']).size().index)

# %% [markdown] {"tags": ["framed_cell"]}
# ### les éléments de l'index sont des tuples
#
# <br>
#
# les éléments dans le `MultiIndex` sont des tuples Python
#
# <br>
#
# par exemple, nous pouvons toujours itérer sur les sous-dataframes  
# de la partition, sauf qu'ici ce qui décrit le groupe, c'est un 2-tuple  
# donc on adapterait l'itération sur ce groupby multi-critère  
# comme ceci
#
# ```python
# for (class_, sex), subdf in by_class_sex:
#     print(f"there were {len(subdf)} {sex} in class {class_} ")
#
# there were 94 female in class 1 
# there were 122 male in class 1 
# there were 76 female in class 2 
# there were 108 male in class 2 
# there were 144 female in class 3 
# there were 347 male in class 3 
# ```
#

# %%
# le code
for (class_, sex), subdf in by_class_sex:
    print(f"there were {len(subdf)} {sex} in class {class_} ")


# %% [markdown] {"tags": ["level_intermediate", "framed_cell"]}
# ### display de `head()` avec IPython
#
# <br>
#
# on veut afficher les 2 premières lignes de chaque dataframe de la partition
#
# <br>
#
# utiliser la méthode `head()` avec `print` n'est pas aussi joli  
# que l'affichage de la dernière expression de la cellule
#
# ```python
# for group, subdf in by_class_sex:
#     print(group, subdf.head(1))
# ```
#
# <br>
#
# pour retrouver la même qualité d'affichage (en html)  
# il faut utiliser la méthode `IPython.display.display()`  
# en important la librairie `IPython`
#
# ```python
# import IPython
# for group, subdf in by_class_sex:
#     print(group)
#     IPython.display.display(subdf.head(1))
# ```

# %%
# le code : c'est moche
#for group, subdf in by_class_sex:
#    print(group, subdf.head(1))

# %% {"tags": ["level_intermediate"]}
# le code
import IPython
for group, subdf in by_class_sex:
    print(group)
    IPython.display.display(subdf.head(1))

# %% [markdown]
# ## **exercice** sur les partitions `groupby`

# %% [markdown]
# on veut calculer la partition avec, dans cet ordre, la classe `Pclass`, le genre `Sex`, et l'état de survie `Survived`
#
# 1. sans calculer la partition  
# proposez une manière de calculez le nombre probable de sous parties dans la partition  

# %%
# votre code

# %% [markdown]
# 2. calculez la partition avec `pandas.DataFrame.groupby`  
#    et affichez les nombres d'items par groupe

# %%
# votre code

# %% [markdown]
# 3. affichez la dataframe des entrées pour les femmes qui ont péri et qui voyagaient en 1ère classe

# %%
# votre code

# %% [markdown]
# 4. **révision**  
#    refaites la même extraction sans utiliser un `groupby()`

# %%
# votre code

# %% [markdown]
# 5. créez un `dict` avec les taux de survie par genre dans chaque classe
#
#    vous devez obtenir quelque chose de ce genre
# ```
# {('female', 1): 0.96,
#  ('female', 2): 0.92,
#  ('female', 3): 0.5,
#  ('male', 1): 0.36,
#  ('male', 2): 0.15,
#  ('male', 3): 0.13}
# ```

# %%
# votre code

# %% [markdown]
# 6. créez à partir de ce `dict` une `pandas.Series`  
#    avec comme nom `'taux de survie par genre dans chaque classe'`  
#    **indice:** comme tous les types en Python  
#    `pd.Series()` permet de créer des objets par programme  
#    voyez la documentation avec `pd.Series?`  

# %% [markdown]
# ## intervalles de valeurs d'une colonne

# %% [markdown] {"tags": ["framed_cell"]}
# ###  introduction
#
# <br>
#
# parfois il y a trop de valeurs différentes dans une colonne  
# du coup on veut faire un découpage de ces valeurs en intervalles
#
# <br>
#
# par exemple dans la colonne des `Age`  
#
# * si nous faisons un groupement brutal sur cette colonne  
# comme nous avons 88 âges différents  
# cela ne donne pas d'information intéressante
# <br>
#
# * mais ce serait intéressant de raisonner par **classes** d'âges par exemple
#    - *'enfant'* jusqu'à 12 ans
#    - *'jeune'* entre 12 ans (exclus) et 19 ans (inclus)
#    - *'adulte'* entre 19 (exclus) et 55 ans (inclus)
#    - *'+55'*  les personnes de strictement plus de 55 ans  
#
# <br>
#
# afin de compléter la colonne des ages  
# `pandas` propose la fonction `pandas.cut`
#
# <br>
#
# nous allons voir un exemple
#
# ```python
# pd.cut?
# ```

# %%
# le code (à décommenter pour essayer)
# # pd.cut?

# %% [markdown] {"tags": ["framed_cell"]}
# ###  découpage en intervalles d'une colonne
#
# <br>
#
# avec `pandas.cut` nous allons créer dans notre dataframe  
# une nouvelle colonne qui contient les intervalles d'ages  
# `(0, 12]`, `(12, 19]`, `(19, 55]` et  `(55, 100]`
#
# <br>
#
# `pandas.cut`
#
# * s'applique à une colonne de votre dataframe
# * vous devez précisez les bornes de vos intervalles avec le paramètre `bins`  
# * les bornes min des intervalles seront exclues  
# * la fonction retourne une nouvelle colonne
#
# <br>
#
# ```python
# pd.cut(df['Age'], bins=[0, 12, 19, 55, 100])
# ->
# PassengerId
# 552    (19.0, 55.0]
# 638    (19.0, 55.0]
# 499    (19.0, 55.0]
# 261             NaN   <- age inconnu au départ
# 395    (19.0, 55.0]
#            ...     
# 326    (19.0, 55.0]
# 396    (19.0, 55.0]
# 832     (0.0, 12.0]
# Name: Age, Length: 891, dtype: category
# Categories (4, interval[int64, right]): [(0, 12] < (12, 19] < (19, 55] < (55, 100]]
# ```
# <br>
#
# remarquez  
#
# * on doit donner toutes les bornes des intervalles  
#   les bornes se comportent comme des poteaux  
#   ici 5 bornes produisent 4 intervalles  
#
# * les bornes min des intervalles sont bien exclues
# * la colonne est de type `category` (cette catégorie est ordonnée)
# * des labels sont générés par défaut
# * les items en dehors des bornes sont transformés en `nan`
#
# <br>
#
# vous pouvez donner des labels aux intervalles avec le paramètre `labels`
#
# ```python
# pd.cut(df['Age'],
#        bins=[0, 12, 19, 55, 100],
#        labels=['children', ' young', 'adult', '55+'])
# ```
#
# <br>
#
# souvent on va ranger cette information dans une nouvelle colonne  
# et ça on sait déjà comment le faire
# ```python
# df['Age-class'] = pd.cut(
#     df['Age'],
#     bins=[0, 12, 19, 55, 100],
#     labels=['children', ' young', 'adult', '55+'])
# ```
#
# <br>
#
# comment feriez-vous pour inspecter le type (des valeurs) de cette colonne ?  
# est-ce un type ordonné ?
#
# <br>
#
# **révision**  
# comment feriez-vous pour vous débarrasser maintenant de la colonne `Age` dans la dataframe
#

# %%
# le code
pd.cut(df['Age'], bins=[0, 12, 19, 55, 100])

# %%
# le code
# pareil mais avec des labels ad-hoc
age_class_series = pd.cut(df['Age'], bins=[0, 12, 19, 55, 100],
       labels=['children', ' young', 'adult', '55+'])
age_class_series

# %%
# pour ranger ça dans une nouvelle colonne
df['Age-class'] = age_class_series

# %%
# le type est une catégorie, il est bien ordonné 
age_class_series.dtype

# %%
# pour effacer la colonne 'Age'
print("avant", df.columns)
del df['Age']
print("après", df.columns)

# %% [markdown] {"tags": ["framed_cell"]}
# ###  groupement avec ces intervalles
#
# <br>
#
# nous avons la colonne `Age-classes` 
#
# <br>
#
# comme c'est un type catégorie, vous pouvez utiliser cette colonne dans un `groupby`
#
# <br>
#
# ```python
# df.groupby(['Age-class', 'Survived', ])
# ```
#
# <br>
#
# vous avez désormais  
# une idée de l'utilisation de `groupby`  
# pour des recherches multi-critères sur une table de données
#
# <br>
#
# **exercice**  
# calculez les taux de survie de chaque classe d'age par classes de cabines

# %%
# le code
df.groupby(['Age-class', 'Survived', ]).size()

# %% [markdown] {"tags": ["framed_cell"]}
# ## `pivot_table()`
#
# <br>
#
# le type d'opérations que l'on a fait dans ce notebook est fréquent  
# spécifiquement, on veut souvent afficher:
#
# * la valeur (précisément, une aggrégation des valeurs) d'une colonne  
# * en fonction de deux autres colonnes (catégorielles)  
# * qui sont utilisées dans les directions horizontale et verticale 
#
# <br>
#
# exemple précis, on pourrait visualiser comme ceci
#
# * le taux de survie  
# * par classe de cabine (en lignes)
# * et par genre (en colonnes)
# <img src="media/pivot-titanic.png" width=200px>
#
# <br>
#
# il existe une méthode `pivot_table()` qui s'avère très pratique  
# pour faire ce genre de traitement **en un seul appel**  
# comme toujours, pensez à lire la doc avec `df.pivot_table?`
#
# <br>
#
# les paramètres les plus importants sont 
#
# * `values` : la (ou les) colonne(s) qu'on veut regarder  
#   ce seront les valeurs **dans le tableau**
#
# * `index` : la (ou les) colonne(s) utilisée(s) pour **les lignes** du résultat
# * `columns` : idem pour **les colonnes**
# * `aggfunc` : la fonction d'aggrégation à utiliser sur les `values`  
#   il y a toujours plusieurs valeurs qui tombent dans une case du résultat  
#   il faut les agréger; par défaut on fait **la moyenne**
#
# <br>
#
# ainsi la table ci-dessus s'obtient **tout simplement** comme ceci
#
# ```python
# df.pivot_table(
#     values='Survived',
#     index='Pclass',
#     columns='Sex',
# )
# ```

# %%
# #df.pivot_table?

# %%
# pour obtenir la table ci-dessus

df.pivot_table(
    values='Survived',
    index='Pclass',
    columns='Sex',
)

# %% [markdown] {"tags": ["framed_cell"]}
# ### `pivot_table()` et agrégation
#
# <br>
#
# dans le cas présent on n'a **pas précisé** la fonction d'**aggrégation**  
# du coup c'est la moyenne qui est utilisée, sur la valeur de `Survived`  
# qui vaut 0 ou 1 selon les cas, et donc on obtient le taux de survie  
#
# <br>
#
# **exercice**
# obtenez la même table que ci-dessus avec cette fois le nombre de survivants

# %%
# votre code

# %% [markdown] {"tags": ["framed_cell"]}
# ### `pivot_table()` et multi-index
#
# <br>
#
# comme on l'a vu, il est possible de passer aux 3 paramètres  
# `values`, `index` et `columns` des **listes** de colonnes
#
# <br>
#
# le résultat dans ce cas utilise un `MultiIndex`  
# pour en quelque sorte "ajouter une dimension"  
# dans l'axe des x ou des y, selon les cas
#
# <br>
#
# **exercice**  
# observez les résultats obtenus par exemple  
# en ajoutant dans chacune des dimensions
#
# * comme valeur supplémentaire `Age`
# * comme critère supplémentaire `Sex`  
# et notamment que pouvez-vous dire des index (en lignes et en colonnes)  
# du résultat produit par `pivot_table()`

# %%
# relisons depuis le fichier pour être sûr d'avoir la colonne 'Age'
df = pd.read_csv('titanic.csv')

# %%
# votre code
# plusieurs values
df2 = ...

# %% {"cell_style": "center"}
df2.columns

# %%
df2.index

# %%
# votre code
# plusieurs columns
df3 = ...

# %%
df3.columns

# %%
df3.index

# %%
# votre code
# plusieurs index
df4 = ...

# %%
df4.columns

# %%
df4.index

# %% [markdown]
# ### **exercice** sur `pivot_table()`

# %%
df = pd.read_csv('wine.csv')
df.head()

# %% [markdown]
# 1. affichez les valeurs min, max, et moyenne, de la colonne 'magnesium'

# %% [markdown]
# 2. définissez deux catégories selon que le magnesium est en dessous ou au-dessus de la moyenne (qu'on appelle 'mag-low' et 'mag-high'); rangez le résultat dans une colonne 'mag-cat'

# %% [markdown]
# 3. calculez cette table
#
# ![](media/pivot-table-expected.png)

# %% [markdown] {"tags": ["framed_cell", "level_intermediate"]}
# ## accès au dictionnaire des groupes
#
# <br>
#
# l'attribut `pandas.DataFrameGroupBy.groups`  
# est un dictionnaire qui décrit les partitions:  
# - la clé correspondent à un groupe  
# - et la valeur est une **liste des index** des lignes du groupe
#
# ```python
# by_sex.groups
#     -> 
# {'female': [499, 395, 703, 859, ...], 'male': [552, 638, 261, 811, ...]}
# ```
#
# <br>
#
# on peut utiliser cette information pour inspecter plus finement  
# le contenu du groupby  
#
# <br>
#
# par exemple pour afficher les noms des 3 premiers membres de chaque groupe
#
# ```python
# for group, indexes in by_sex.groups.items():
#     print(group, df.loc[indexes[:3], 'Name'])
# ```

# %% {"tags": ["level_intermediate"]}
# le code
by_sex.groups

# %% {"tags": ["level_intermediate"]}
# le code
for group, indexes in by_sex.groups.items():
    print(group, df.loc[indexes[:3], 'Name'])

# %% [markdown] {"tags": ["level_advanced"]}
# ## pour en savoir plus
#
# on recommande la lecture de cet article dans la documentation `pandas`, qui approfondit le sujet et notamment la notion de `split-apply-combine` 
#
# (qui rappelle, de loin, la notion de *map-reduce*)
#
# https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

