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
#     title: TP sur les types des colonnes
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")

# %% [markdown]
# # TP sur les types des colonnes

# %% [markdown]
# ## import des librairies et des données
#
# **Exercice** pour importer des librairies et des données
#
# 1. importez les librairies `numpy`, `pandas` et `matplotlib.pyplot`
# <br>
#
# 1. importez le fichier de données `iris.csv`  
# la première ligne contient les noms des colonnes  
# les 5 colonnes sont les longueur et les largeurs des sépales et des pétales et le type de l'iris  
# soit `'SepalLength'`, `'SepalWidth'`, `'PetalLength'`, `'PetalWidth'` et `'Name'`
# <br>
#
# 1. Affichez les 3 premières lignes de la dataframe

# %% [markdown]
# ## le type `object` `str`
#
# dans la dataframe précédente
#
# 1. affichez le type des colonnes  
# (attribut `dtypes` des `pandas.Series` ou de la `pandas.DataFrame`)
# <br>
#
# 1. quel est le type des 4 mesures ?
# <br>
#
# 1. quel est le type de la colonne `Name` ?  
# Avez-vous une idée de ce que représente le type `object` des noms des fleurs ?  
# les noms sont des chaînes de caractères
# <br>
#
# 1. essayez de mettre les noms en majuscules  
#    grâce aux indices suivants:
#
#  * il s'agit donc pour nous d'apppliquer la méthode `upper`
#    à toutes les chaînes de caractères (`str`) de  la colonne `df['Name']`
#
#  * les `pandas.Series` formées de chaînes de caractères sont, par défaut, du type `pandas` `object`
#  * ces colonnes ont un accesseur `str` (par exemple ici `df['Names'].str`)
#  * cet attribut permet d'accéder aux méthodes classiques des `str` (comme par exemple `upper()`)
#  * ces fonctions sont naturellement vectorisées  
#    i.e. elles s'appliquent à toute la série (sans for-python)  
# <br>
#   
# 1. observer la valeur de la colonne `Name` dans la dataframe originale  
#    a-t-elle été modifiée ?  
#    comment faire pour la modifier ?

# %% [markdown]
# ## le type `category`
#
# sur la dataframe précédente
#
# 1. utilisez la fonction `pandas.Series.unique` pour afficher la liste des noms d'iris  
# combien avez vous de noms différents ?  
# <br>
#
# 1. inspectez les types des colonnes  
#    que pensez-vous du type `object` `str` pour cette colonne ?  
#    en effet, la colonne `'Name'` serait mieux définie par un type catégorie `'category'`  
#    
#    **rappels** sur la fonction `pandas.Series.astype`  
#
#    * elle possède un paramètre `copy` qui, par défaut, est à `True`
#    * cela signifie que, sans indication spécifique, cette fonction retourne une copie de la colonne
#    <br>
#    <br>
#
# 1. utilisez la fonction `pandas.Series.astype`  
# pour créer une colonne de type `category`  
# que vous appelez `'Name-cat'`
# <br>
#
# 1. comme pour les colonnes de type `str`  
#    vous pouvez accéder aux fonctions et attributs spécifiques des objets de type catégorie  
#    en passant par l'accesseur `cat`
#
#    appliquez l'attribut `codes` aux objets de la colonne `'Name-cat'` en utilisant l'accesseur `cat`  
#    affichez le type de l'objet ainsi obtenu  
#    Que contient cette série ?
#    <br>
#
# ce moyen vous permet d'accéder aux codes que `pandas` a attribué aux trois noms d'Iris  
# `'Iris-setosa'` est `0`  
# `'Iris-versicolor'` est `1`  
# `'Iris-virginica'` est `2`

# %%
# votre code

# %% [markdown] tags=["level_intermediate"]
# ## fabriquer son propre type `category`
#
# *pour les rapides*
#
# avec la technique précédente on n'a pas de **contrôle sur l'ordre** parmi les différentes catégories
#
# imaginez que nous avons maintenant une colonne dont les valeurs uniques sont  
# `bad`, `average`, `good`, `excellent`
#
# on peut définir *son propre type catégoriel* avec la fonction  
# `pd.CategoricalDtype()`
#
# 1. cherchez cette fonction dans la documentation
#    <br>
#    
# 1. utilisez-la pour créer un type catégoriel dans lequel, disons par exemple  
# `'Iris-versicolor'` < `'Iris-setosa'` < `'Iris-virginica'` 
#
# 1. convertissez la colonne `Name` dans ce type
#
# 1. assurez-vous que vous pouvez trier la dataframe selon ce type

# %% tags=["level_intermediate"]
# votre code
