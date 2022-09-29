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
#     title: "Python-num\xE9rique - les tables de donn\xE9es"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")

# %% [markdown]
# # Python-numérique - les tables de données

# %% [markdown] tags=["framed_cell"]
# ## introduction sur les tables de données
# <br>
#
# nous avons vu quelques fonctions de `numpy`, pour manipuler les `numpy.ndarray` qui sont des tableaux
#
# * multidimensionnels
# * homogènes
# * d'éléments de taille fixe
#
# <br>
#
# il existe d'autres **tables de données**, très fréquentes en data-science où on a:
#
# * une observation par ligne (ici les passagers du Titanic)  
# * plusieurs informations par observation  
# * les différentes informations forment les colonnes de la table
# * ces colonnes se sont pas toutes du même type...
#
# <img src='media/titanic.png' width="1000"></img>

# %% [markdown]
# ## lecture d'une table de données

# %% [markdown] tags=["framed_cell"]
# ### format CSV
#
# <br>
#
# format de fichier, le plus simple, pour stocker ces tables ? 
#
# * une observation par ligne
# * dans chaque ligne, les informations séparées par un caractère choisi au préalable  
# (qui sera le même pour tout le fichier)
#
# <br>
#
# fichier de format **`CSV`** pour ***Comma-Separated-Values***  
# **notez bien**: le caractère séparateur n'est pas obligatoirement une `,`
#  
# <br>
#
# voici le début du fichier `titanic.csv`, notez:
#
# * le séparateur `,` sans espace autour
# * dans `"Sharp, Mr. Percival James R"` un *faux* séparateur `,` dans une chaîne
# * dans la première ligne, les noms des colonnes (pas obligatoire)
# * des `,,` (quand les informations ne sont pas connues)
#
# ***
#
# ```
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 552,0,2,"Sharp, Mr. Percival James R",male,27.0,0,0,244358,26.0,,S
# 638,0,2,"Collyer, Mr. Harvey",male,31.0,1,1,C.A. 31921,26.25,,S
# 499,0,1,"Allison, Mrs. Hudson J C (Bessie Waldo Daniels)",female,25.0,1,2,113781,151.55,C22 C26,S
# 261,0,3,"Smith, Mr. Thomas",male,,0,0,384461,7.75,,Q.../...
# ```

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### la librairie de data-science
#
# <br>
#
# pour lire, mettre en forme et manipuler des données de data-science  
# on utilise **la librairie `pandas`** (2008)
#
# ```
# import pandas as pd
# ```
#
# <br>
#
# `numpy` ne propose pas directement ces fonctions  
#
# <br>
#
# `pandas` expose un type évolué de table de données: les **`pandas.DataFrame`**
#
# <br>
#
# `pandas` possède un type pour gérer une ligne et une colonne le **`pandas.Series`**
#
# <br>
#
# `pandas` comme `numpy` favorisent l'efficacité  
# (parfois au détriment de la lisibilité)
#
# <br>
#
# `pandas` repose entièrement sur `numpy` (aujourd'hui en tous cas)  
# i.e. les données manipulées par `pandas` sont implémentées comme des tableaux `numpy.ndarray`  
#

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### on importe `pandas`
#
# <br>
#
# on importe la librairie `pandas`  
# avec son raccourci conventionnel
#
# ```python
# import pandas as pd
# ```
# <br>
#
# vous n'avez pas `pandas` ? faites
# ```
# # depuis le terminal
# pip install pandas
# # depuis une cellule du notebook:
# %pip install pandas
# ```
#
# <br>
#
# regardez la version de la librairie installée  
# <https://pandas.pydata.org/docs/whatsnew/index.html>
# ```python
# pd.__version__
# ```

# %%
# le code
import pandas as pd
pd.__version__

# %% [markdown] tags=["framed_cell"]
# ### lecture d'un fichier `csv`
#
# <br>
#
# on lit le fichier de format `csv` de la table de passagers du Titanic
# ```python
# df = pd.read_csv('titanic.csv')
# ```
# <br>
#
# la table est une instance de `pandas.DataFrame`
#
# ```python
# type(df)
# -> pandas.core.frame.DataFrame
# ```
#
# (`pandas.core.frame.DataFrame` est le même type que `pandas.DataFrame`)
#
# <br>
#
# la méthode `df.head()` affiche les qq premières lignes
#
# ```python
# df.head(2)
# ```
#
# <div class=note>
#
# quand on écrit "la méthode `df.head`", ça se lit comme:   
# l'attribut `head` recherché à partir de l'objet `df`  
# comme `df` est une dataframe, on trouve la méthode/fonction qui se trouve être aussi `pd.DataFrame.head`
#     
# </div>    

# %%
# le code 
df = pd.read_csv('titanic.csv')
type(df)

# %%
# pour vous convaincre que les types sont bien les mêmes

pd.core.frame.DataFrame is pd.DataFrame

# %%
# pour afficher les premières lignes
# à votre avis, comment on voit les dernières lignes ?
df.head(2)

# %% [markdown] tags=["framed_cell"]
# ## description rapide de la table des données
#
# <br>
#
# la méthode `describe()` vous donne un premier aperçu rapide de vos données
#
# <br>
#
# sur une `DataFrame`, elle vous donne  
# pour chaque colonne **de type numérique**
#
# * le nombre de valeurs non-manquantes (voir colonne `Age`)
# * la moyenne
# * l'écart-type
# * le minimum
# * les 3 quartiles (les valeurs à 25%, 50% et 75% de données)
# * le maximum
#
# <br>
#
# ```python
# df.describe()
# ->     PassengerId Survived Pclass Age     SibSp   Parch   Fare
# count  891.00      891.00   891.00 714.00  891.00  891.00  891.00
# mean   446.00      0.38     2.30   29.69   0.52    0.38    32.20
# std    257.35      0.48     0.83   14.52   1.10    0.80    49.69
# min    1.00        0.00     1.00   0.42    0.00    0.00    0.00
# 25%    223.50      0.00     2.00   20.12   0.00    0.00    7.91
# 50%    446.00      0.00     3.00   28.00   0.00    0.00    14.45
# 75%    668.50      1.00     3.00   38.00   1.00    0.00    31.00
# max    891.00      1.00     3.00   80.00   8.00    6.00    512.32
# ```
# <br>
#  
# on remarque que `pandas.DataFrame.describe`
#
# * a, par défaut, appliqué les calculs sur **les colonnes numériques**  
# même quand ça n'a pas forcément beaucoup d'intérêt - voir `Survived` ou `Pclass`  
# qui sont plutôt des catégories
#
# * n'a rien fait sur les colonnes non-numériques
#
# <br>
#
# on aurait pu n'appliquer la méthode qu'à une sous-dataframe  
# ```python
# df[['Age', 'Fare']].describe()  
# ```
#
# <br>
#
# ou forcer la méthode à s'appliquer à **toutes les colonnes**  
# pour les colonnes non-numériques, seront affichés à la place
#
# * le nombre de valeurs
# * le nombre de valeurs `unique`s
# * la valeur la plus fréquente `top`
# * sa fréquence `freq`
#
# ```python
# df.describe(include='all')
# ```
#
# <br>
#
# la méthode `describe()` marche aussi sur les séries (colonnes) 
#
# ```python
# df['Sex'].describe()
# ->
# count 891
# unique 2
# top male
# freq 577
# Name: Sex, dtype: object
# ```  
#

# %%
# le code

# pas besoin de 6 chiffres après la virgule
pd.options.display.precision = 2

df.describe()

# %%
df[['Age', 'SibSp', 'Parch', 'Fare']].describe()

# %%
# le code
df.describe(include='all')

# %%
# le code
df['Sex'].describe()

# %% [markdown]
# ## les index et indices des tables

# %% [markdown] tags=["framed_cell"]
# ### la notion d'index
#
# <br>
#
# la clé pour comprendre `pandas`:
#
# * **les lignes et les colonnes ont des index**
# * les opérations sur ces index sont **le plus efficace possible**
# * (on verra par la suite que les lignes et les colonnes ont aussi naturellement des indices, i.e. de `0` à `n-1`)
#
# <br>
#
# **la notion d'index**
#
# un constat  
#
# * rechercher dans une liste est très inefficace  
# (en moyenne $n/2$ essais pour localiser un élément)
#
# **l'idée**
#
# * trouver une caractéristique qui identifie une observation de manière unique  
# (genre *numéro de sécurité sociale* pour un individu)
#
# * calculer un index à partir de cette caractéristique  
# qui soit *le plus unique* possible (pour avoir peu de collisions)
#
# * utiliser cet index comme entrée dans une table
# * la recherche peut alors être considérée comme en temps constant  
#   comme l'accès à un élément d'un tableau
#
# * c'est la technique des **tables de hachage** (comme les `dict` ou `set` Python)
#
# <br>
#
# `pandas` indexe ses lignes et ses colonnes suivant vos indications  
# dit autrement, c'est à vous de choisir parmi les colonnes 
# celle(s) qui peut servir d'identificateur unique pour servir d'index

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### index des colonnes
#
# <br>
#
# dans notre fichier du Titanic seules les colonnes ont un nom  
# (les lignes n'en ont pas), du coup:
#
# * les **colonnes** ont été **indexées par leur nom**
# * les **lignes** ont été **indexées par leur indice**  
# i.e. une *simple numérotation à partir de 0*  
# on y reviendra
#
# <br>
#
# l'attribut `columns` permet d'accéder aux colonnes de la table
#
# ```python
# df.columns
# -> Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#           'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#    dtype='object')
# ```
# <br>
#
# c'est un object de type `Index`; il permet d'accéder facilement aux noms des colonnes
#
# ```python
# df.columns[0]
# -> 'PassengerId'
# ```
#

# %%
# le code
df.columns

# %%
df.columns[0]

# %% [markdown] tags=["framed_cell"]
# ### accès aux colonnes avec `df[]`
#
# <br>
#
# les colonnes ont un traitement privilégié en `pandas`
#
# <br>
#
# une table `pandas` est un "dictionnaire"
#
# * où les clés sont les noms des colonnes
# * où les valeurs sont les colonnes (**de type `Series`**)
#
# <br>
#
# accès à la colonne `Age` de la data-frame du Titanic
#
# * on remarque les `891` entrées
# * on remarque les indices des lignes de `0` à `890` 
# * on constate que le type des éléments de cette colonne est `float64`
# * on constate que l'age du passage d'indice `3` est manquant `NaN` (*Not a Number*)
#
# ```python
# df['Age']
# ->  0      27.00
#     1      31.00
#     2      25.00
#     3        NaN
#     4      24.00
#            ...
#     886    47.00
#     887    30.00
#     888    36.00
#     889    22.00
#     890     0.83
# Name: Age, Length: 891, dtype: float64
# ```
#
# <br>
#
# attention `pandas` accepte que plusieurs colonnes portent le même nom  
# en cas d'accès, il vous les donne toutes

# %% cell_style="split"
df['Age'].head(2)

# %% cell_style="split"
# type Series
type(df['Age'])

# %%
# on peut aussi passer une liste de colonnes
# auquel cas on récupère une dataframe
df[['Age', 'Sex']].head()

# %% [markdown] tags=["framed_cell"]
# ### accès aux colonnes avec `df.`
#
# <br>
#
# Lorsque le nom de la colonne ne comporte pas de caractère bizarre  
# on peut aussi accéder à une colonne au travers d'**un attribut**
#
# <br>
#
# Cette notation est **plus lisible** mais aussi **plus limitée**  
# par exemple ne fonctionne pas si le nom de la colonne contient un espace 
#
# <br>
#
# Il faut le voir uniquement comme *une commodité*  
# **Pas forcément recommandé aux débutants**  
# Mais c'est *très utilisé* - il faut savoir le lire
#
# <br>
#
# ```python
# df.Age is df['Age']
# -> True
# ```

# %% cell_style="split"
# le code
# on peut aussi accéder à une colonne par un attribut
# qui est une notation plus lisible
df.Age

# %% cell_style="split"
df.Age is df['Age']

# %% [markdown] tags=["framed_cell"]
# ### type des colonnes `pandas.Series`
#
# <br>
#
# ```python
#     type(df['Age'])
# -> pandas.core.series.Series
# ```
# <br>
#
# le second type en `pandas` est le type des colonnes, qui sont des `Series`
#
#
# on peut voir la `DataFrame` comme un dictionnaire qui associe  
# { `nom-de-colonne` $\rightarrow$ `un-objet-series` }

# %%
# le code
type(df['Age'])

# %% [markdown] tags=["framed_cell"]
# ### indexer les lignes
#
# <br>
#
# c'est une bonne pratique de choisir **une colonne**  
# comme **index** (des lignes) de la table  
# quand on le peut...
#
# <br>
#
# par exemple, dans la table du titanic, on remarque que  
# la colonne `PassengerId` contient un **identifiant unique** pour chaque passager
#
# <br>
#
# choisissons **cette colonne comme index** (des lignes) de la table  
# pour cela, deux options
#
# 1. directement à la lecture du fichier
#
#    ```python
#    # option 1
#    df = pd.read_csv('titanic.csv', index_col='PassengerId')
#    ```
#
# 2. après coup
#
#    ```python
#    # option 2
#    df = pd.read_csv('titanic.csv')
#    df = df.set_index('PassengerId')
#    ```
#
# <br>
# observez le changement dans la présentation de la table

# %%
# le code
# option 1.
df = pd.read_csv('titanic.csv', index_col='PassengerId')

# %%
# le code
# option 2.
df = pd.read_csv('titanic.csv')
# la table avant
df.head(1)

# %%
# la table après
# remarquez que 'PassengerId' 
# n'est plus présenté de la même manière
df = df.set_index('PassengerId')
df.head(1)

# %% [markdown] tags=["framed_cell"]
# ### une série aussi possède un index
#
# <br>
#
# * accèdons à la colonne `Name`  
#   remarquons qu'ici aussi, l'objet Series possède un index  
#   qui en l'occurrence est `PassengerId` (provient de la `df`)
#
#   ```python
#   df['name']
#   ->  PassengerId
#     552                          Sharp, Mr. Percival James R
#     638                                  Collyer, Mr. Harvey
#     499      Allison, Mrs. Hudson J C (Bessie Waldo Daniels)
#     261                                    Smith, Mr. Thomas
#     395    Sandstrom, Mrs. Hjalmar (Agnes Charlotta Bengt...
#                                  ...
#     463                                    Gee, Mr. Arthur H
#     287                              de Mulder, Mr. Theodore
#     326                             Young, Miss. Marie Grice
#     396                                  Johansson, Mr. Erik
#     832                      Richards, Master. George Sibley
#    ```
#    
# <br>
#
# * toutes les colonnes de la dataframe partagent **le même index**  
#   c'est de cette façon que les colonnes sont "alignées" entre elles
#
# <br>
#
# * accèdons à la colonne `Name` de la première ligne  
#   son index (`PassengerId`) est `552`
#
#   ```python
#   df['Name'][552] # passager d'id 552
#   -> 'Sharp, Mr. Percival James R'
#   ```

# %%
# le code
df = pd.read_csv('titanic.csv', index_col='PassengerId')
df['Name']

# %%
# ici on obtient la première ligne !

# quand on indexe une Series,
# c'est par l'index (552)
# et non pas par l'indice qui ici serait 0
df['Name'][552]

# %% [markdown]
# <div class=note>
#
# ici nous avons un index de type entier; lorsqu'on a un index de type, par exemple, `str`, 
# on peut alors écrire ou bien
#     
# * `series[entier]` pour aller chercher l'indice `entier` 
# * `series[chaine]` pour aller chercher l'index `chaine`
#
# mais avec un index de type entier, c'est l'accès **par index** qui est privilégié
# </div>    

# %% [markdown] tags=["framed_cell"]
# ### différence entre index et indice
#
# <br>
#
# les **indices** c'est quand on compte nos éléments à partir de `0`  
# (les colonnes comme les lignes ont aussi des indices)
#
# <br>
#
# les **index** c'est quand on utilise des valeurs fournies par l'utilisateur, comme
#
# * les **noms** de colonnes
# * ou les **identifiants** de lignes  
#   par ex. plus haut `552` est l'index de la première ligne parce que  
#  dans la colonne-index `PassengerId`, la première ligne contient `552`
#
# <br>
#
# si une table n'a **pas d'index** particulier,  
# i.e. avant qu'on fasse un `set_index()`  
# pandas crée automatiquement un index de type `RangeIndex`  
# dans ce cas l'**index commence à 0**, et du coup  
# incidemment les **indices** et les **index coincident**

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### l'index des lignes
#
# <br>
#
# il est accessible par l'attribut `pandas.DataFrame.index`
#
# <br>
#
# lisons la data-frame du titanic sans fixer l'index de lignes
#
# ```python
# df = pd.read_csv('titanic.csv') 
# df.index
# -> RangeIndex(start=0, stop=891, step=1)
# ```
#
# * l'index est alors un `RangeIndex` de `0` à `890` inclus
#
# <br>
#  
# lisons la data-frame du titanic et choisissons la colonne `PassengerId` comme index de ligne
#
# ```python
# df = pd.read_csv('titanic.csv').set_index('PassengerId')
# df.index
# -> Int64Index([552, 638, 499, 261, 395, 811, 758, 703, 406, 641,
#               ...
#               556, 236, 224, 598, 258, 463, 287, 326, 396, 832],
#              dtype='int64', name='PassengerId', length=891)
# ```
#
# * les index des lignes sont les valeurs de la colonne `PassengerId`
#
# <br>
#
# faisons l'indexation précédente en deux coups  
#
# * on lit la data-frame du titanic  
# * on modifie son index par la colonne `PassengerId` avec la méthode `set_index`  
# remarquez le `inplace` 
#
# ```python
# df = pd.read_csv('titanic.csv')
# df.set_index('PassengerId', inplace=True)
# df.index
# -> Int64Index([552, 638, 499, 261, 395, 811, 758, 703, 406, 641,
#               ...
#               556, 236, 224, 598, 258, 463, 287, 326, 396, 832],
#              dtype='int64', name='PassengerId', length=891)
# ```
#
# <br>
#
# `pandas.Int64Index` et `pandas.RangeIndex` sont tout deux des `pandas.Index`

# %%
# le code
df = pd.read_csv('titanic.csv') 
df.index

# %%
# le code
df = pd.read_csv('titanic.csv').set_index('PassengerId')
df.index

# %%
# le code
df = pd.read_csv('titanic.csv')
df.set_index('PassengerId', inplace=True)
df.index

# %% [markdown] tags=["framed_cell"]
# ## **résumé** à propos des types
#
# * les tables pandas sont représentées par le type `DataFrame`
# * une dataframe a 
#   * un index pour accéder aux colonnes (`df.columns`)  
#   * et un index pour accéder aux lignes (`df.index`)  
#   * ces deux objets sont de type `Index` 
# * une colonne, ou une ligne, sont de type `Series`  
#   qui correspond si on veut à des données en 1 seule dimension

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ## dimension et forme de la table
#
# <br>
#
# `pandas` est fondé sur `numpy`  
# cela pourrait changer dans le futur
#
# <br>
#
# la **dimension** de la table est donnée par l'attribut `pandas.DataFrame.ndim` 
#
# ```python
# df.ndim
# -> 2
# ```
#
# une `pandas.dataFrame` est une table donc a deux dimensions
#
# <br>
#
# la **forme** de la table est donnée par l'attribut `pandas.DataFrame.shape` 
#
# ```python
# df.shape
# -> (891, 11)
# ```
#
# on retrouve là les attributs classiques de `numpy` `ndim`, `shape`
#
# <br>
#
# `numpy` s'occupe de stocker et manipuler le tableau de dimension 2
#
# <br>
#
# `pandas` apporte
#
# * l'indexation du tableau
# * des fonctions pratiques et de haut-niveau pour manipuler cette table de données

# %%
# le code
df = pd.read_csv('titanic.csv', index_col='PassengerId')
print(df.ndim)
print(df.shape)

# %% [markdown]
# ## exercice

# %% [markdown]
# Le fichier `petit-titanic.csv` contient les 10 premières lignes de passagers  
# *Attention* ce n'est **pas exactement** le même format que `titanic.csv`

# %% scrolled=false
# pour voir le contenu du fichier

# %cat petit-titanic.csv

# remarquez qu'on peut aussi le faire en Python pur
#with open("petit-titanic.csv") as f:
#    for line in f:
#        print(line, end="")

# %% [markdown]
# 1. lisez le contenu de ce fichier avec les paramètres par défaut de `pandas.read_csv`  
# affichez les premières lignes avec `pandas.DataFrame.head`  
# <br>
# 1. 
# voyez-vous les trois problèmes ?  
# essayez de les résoudre en étudiant la doc. de la fonction
# `pd.read_csv()`  
# passez à la question 3 pour être aidé
# <br>
#
# 1. 
#   1. passez le **bon séparateur** à la méthode `pandas.read_csv`  
#   1. et indiquez lui que la première ligne  
#      **ne contient pas** la liste des noms des colonnes  
#   1. passez-lui le nom des colonnes puisqu'elles ne sont pas  
#      mentionnées dans le fichier  
#   *spoiler*: voyez les paramètres `sep`, `header` et `names`
# <br>
#
# 1. affichez le nombre de colonnes et de lignes
# <br>
#
# 1. affichez les index des colonnes et des lignes
# <br>
#
# 1. modifiez l'index des colonnes par la liste
# ```Python
# columns = ['Identifiant', 'Survécu', 'Pclass', 
#               'Nom', 'Genre', 'Age', 'SibSp', 'Parch',
#               'Ticket', 'Tarif', 'Cabine', 'Embarquement']
# ```
# <br>
#
# 1. modifiez l'index des lignes par la colonne `'PassengerId'`
#

# %%
# votre code
