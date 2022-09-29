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
#     title: '*broadcasting*'
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %% [markdown]
# # *broadcasting*

# %%
import numpy as np

# %% [markdown]
# ## contenu de ce notebook (sauter si déjà acquis)
#
# <br>
#
# comment `numpy` traite intelligemment les tableaux de formes différentes lors des opérations
#
# <br>
#
# les règles de broadcasting

# %% [markdown]
# ## opération sur des tableaux de même forme

# %% [markdown]
# **Exercices**
#
# 1. créez un premier tableau des 120 premiers entiers  
# avec la forme de 2 groupes et 3 matrices de 4 lignes, et nombre de colonnes adéquat
# <br>
#
# 1. créez un second tableau de 120 flottants équidistants entre 0 et 1  
# donnez lui la même forme que le premier tableau
# <br>
#
# 1. utilisez `np.round` pour arrondir les flottants à 2 décimales  
# sans création d'un nouveau tableau (pensez à `out=`)
# <br>
#
# 1. utilisez `np.add` pour ajouter les deux tableaux  
#   a. en créant un troisième tableau pour ranger le résultat  
#   b. en rangeant le résultat dans le premier tableau (avec le paramètre `out`) ?
# <br>
#
# 1. renversez le premier tableau  
#   selon tous les axes

# %%
# votre code

# %% [markdown] {"tags": ["framed_cell"]}
# ## tableaux de formes différentes: broadcasting
# <br>
#     
# vous voulez incrémenter de 1 tous les éléments d'une matrice d'entiers de forme `(100, 100)`
# ```python
# tab = np.arange(0, 10000).reshape(100, 100)
# ```
#     
# <br>
#     
# créer une matrice de `ones` de la même forme et les ajouter... vous convient-il ?
#     
# ```python
# inc = np.ones(shape=(100, 100), dtype=np.int8)
# tab+inc
# ```
#     
# <br>
#     
# c'est clairement sous-optimal: place-mémoire créée inutilement, perte de temps et de lisibilité
#     
# <br>
#     
# `numpy` propose une manière abrégée d'écrire ce genre d'opération grâce au `broadcasting`
#     
#   
# ```python
# tab+1
# ```
#       
# ou encore (moins joli)    
#     
#   
# ```python
# tab+[1]
# ```
#       
# <br>
#     
# simple, élégant et non ambigu
#     
# <br>
#
# mais attention : ne **fonctionne pas** du tout pareil sur les **listes `Python`**
#     
# ```python
# [1, 2, 3, 4, 5, 6] + [10, 20 ] # + est append
# -> [1, 2, 3, 4, 5, 6, 10, 20]
# ```

# %%
# le code
tab = np.arange(0, 10000).reshape(100, 100)
inc = np.ones(shape=(100, 100), dtype=np.int8)
tab+inc
tab+1
tab+[1]

# %%
# code
print([1, 2, 3, 4, 5, 6] + [10, 20])

# %% [markdown]
# ## broadcasting : comment ça marche ?

# %% [markdown] {"tags": ["framed_cell"]}
# ### le broadcasting, c'est quoi ?
# <br>
#     
# c'est la manière dont `numpy` traite les tableaux de formes différentes lors d'opérations
#     
# <br>
#     
# le *plus petit tableau*, **quand c'est possible**, est considéré comme *élargi* à la taille du plus grand  
# afin qu'ils aient des formes compatibles
#     
# <br>
#     
# cela se fait **implicitement**

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell"]}
# ### opération entre un scalaire et un tableau par broadcasting
#
# <br>
#     
# l'opération entre un scalaire est un tableau est toujours possible  
# il est possible de considérer un scalaire comme un tableau de n'importe quelle forme
#
# --------------------------------
# prenons une matrice et l'opération d'addition élément à élément
#     
# ```python
# mat = np.arange(15).reshape(3, 5)
# mat
# -> [[ 0,  1,  2,  3,  4],
#     [ 5,  6,  7,  8,  9],
#     [10, 11, 12, 13, 14]]
# ``` 
#     
# <br>
#
#         
# ```python
# mat + 1
# -> [[ 1,  2,  3,  4,  5],
#     [ 6,  7,  8,  9, 10],
#     [11, 12, 13, 14, 15]]
# ``` 
#
#    
# ------------------
#
# c'est **comme si** le scalaire `1` devenait la matrice $\begin{pmatrix} 1 & 1 & 1 & 1 &1 \\ 1 & 1 & 1 & 1 &1 \\ 1 & 1 & 1 & 1 &1 \\ \end{pmatrix}$
#     
# -----------------------
#     
# naturellement `numpy` ne va **jamais** construire un tel objet  
# il va juste s'arranger pour incrémenter les éléments des lignes et des colonnes de la matrice par `1`

# %% {"cell_style": "split"}
mat = np.arange(15).reshape(3, 5)
mat + 1

# %% {"cell_style": "split"}
# c'est donc comme si on avait
# ajouté à mat ceci
(mat+1) - mat

# %% [markdown] {"tags": ["framed_cell"]}
# ### opération entre une ligne et un tableau par broadcasting
#
# <br>
#  
# la ligne et le tableau doivent obéir à des conditions de forme (plutôt évidentes)
#
# --------------------------------
#     
# prenons une matrice et l'opération d'addition
#     
# ```python
# mat = np.arange(15).reshape(3, 5)
# mat
# -> [[ 0,  1,  2,  3,  4],
#     [ 5,  6,  7,  8,  9],
#     [10, 11, 12, 13, 14]]
# ``` 
#
#     
# -------------------------------------------
# pour ajouter une **ligne** à toutes les lignes d'une matrice  
# il faut naturellement que la forme des lignes corresponde
#     
# **non**    
# ```python
# mat + [10, 20, 30]
# -> ValueError: operands could not be broadcast together with shapes (3,5) (3,) 
# ```   
#
#   
# **oui**
#     
# ```python
# mat + [10, 20, 30, 40, 50]
# # oui
#     [[10, 21, 32, 43, 54],
#      [15, 26, 37, 48, 59],
#      [20, 31, 42, 53, 64]]
# ```   
#
# **oui aussi**
# ```python
# mat + np.arange(10, 60, 10)
# # ou
# mat + np.arange(10, 60, 10).reshape(1, 5)
# ```
#
# -------------------------------
#
# c'est comme si on ajoutait la matrice $\begin{pmatrix} 10 & 20 & 30 & 40 & 50 \\ 10 & 20 & 30 & 40 & 50 \\ 10 & 20 & 30 & 40 & 50 \\ \end{pmatrix}$
#     
#     
# là encore, `numpy` ne va **jamais** générer une telle matrice  
# il va procéder par des boucles sur les lignes de la matrice

# %%
# le code
mat = np.arange(15).reshape(3, 5)

try:
    mat + [10, 20, 30]
except ValueError as e:
    print(e)
    
mat + [10, 20, 30, 40, 50]
mat + np.arange(10, 60, 10)
mat + np.arange(10, 60, 10).reshape(1, 5)

# %% [markdown] {"tags": ["framed_cell"]}
# ### opération entre une ligne et un groupes de matrices
#
# <br>
#     
# de même, on peut ajouter une ligne à tout un groupe de matrices... si la forme des lignes coincide
#     
#     
# <br>
#     
# ```python
# tab = np.arange(30).reshape(2, 3, 5)
# tab
# -> [[[ 0  1  2  3  4]
#      [ 5  6  7  8  9]
#      [10 11 12 13 14]]
#     
#     [[15 16 17 18 19]
#      [20 21 22 23 24]
#      [25 26 27 28 29]]]
# ``` 
#     
# <br>
#     
# ```python
# tab + [1000, 2000, 3000, 4000, 5000]    
# tab
# -> [[[1000, 2001, 3002, 4003, 5004],
#     [1005, 2006, 3007, 4008, 5009],
#     [1010, 2011, 3012, 4013, 5014]],
#
#    [[1015, 2016, 3017, 4018, 5019],
#     [1020, 2021, 3022, 4023, 5024],
#     [1025, 2026, 3027, 4028, 5029]]]
# ```
#
# <br>
#     
# de même pour les groupes de groupes de groupes de ... de matrices, etc.

# %%
# le code
mat = np.arange(30).reshape(2, 3, 5)
print(mat)
mat + [1000, 2000, 3000, 4000, 5000]   

# %%
mat = np.arange(400).reshape(2, 4, 2, 5, 5)
print(mat)
mat + [1000, 2000, 3000, 4000, 5000]   

# %% [markdown] {"tags": ["framed_cell"]}
# ### opération entre une colonne et une matrice
# <br>
#  
# c'est pareil...
#     
# ```python    
# mat = np.arange(15).reshape(3, 5)
# mat
# -> [[ 0,  1,  2,  3,  4],
#     [ 5,  6,  7,  8,  9],
#     [10, 11, 12, 13, 14]]
# ```    
# <br>
#     
# il faut naturellement que la forme des colonnes corresponde
#     
# ```python    
# col = np.array([100, 200, 300]).reshape(3, 1)
# col
# ->    
#   [[100],
#    [200],
#    [300]]
#     
# ```
#     
# remarquez la forme de la colonne `col`
#     
# <br>
#
# on ajoute
#
# ```python    
# mat + col
# ->
#     [[100, 101, 102, 103, 104],
#      [205, 206, 207, 208, 209],
#      [310, 311, 312, 313, 314]]
# ``` 
#     
# <br>
# et ainsi de suite

# %%
# le code
mat = np.arange(15).reshape(3, 5)
col = np.array([100, 200, 300]).reshape(3, 1)
print(col)
mat+col


# %% [markdown] {"tags": ["framed_cell"]}
# ### opération entre une ligne et une colonne
#
# <br>
#     
# cela va faire ce à quoi vous vous attendez: une matrice !
#     
# <br>
#     
# **exercice**
# 1. créer une ligne contenant par exemple 0, 1, 2, 3, 4
# 1. créer une colonne contenant par exemple 10, 20, 30
# 1. ajouter les deux
#     
# <br>
#     
# il faut faire attention à la forme de la colonne `(n, 1)`

# %% [markdown] {"tags": ["level_intermediate", "framed_cell"]}
# ## règles de broadcasting - avancés
#
# <br>
#     
# Les dimensions des deux tableaux, sur lesquels une opération élément-par-élément est appliquée
#
# * sont comparées de droite à gauche (par paire)
#     
#
# * le broadcasting sera possible:
#     1. si les deux dimensions sont identiques
#     1. si l'une des 2 dimensions vaut 1  
#      auquel cas elle est élargie à la dimension requise  
#      et le broadcast continue
#     
#     
# <br>
#     
# * quand les formes ne sont pas consistantes, le broadcasting est impossible  
# `numpy` rejette l'opération en déclenchant une erreur de type `ValueError`
#     
# ```python
# m1 = np.arange(6).reshape(2, 3)
# m2 = np.arange(8).reshape(2, 4)
# m1 * m2
# -> ValueError: operands could not be broadcast together with shapes (2,3) (2,4)
# ```

# %%
# le code d'un exemple
m1 = np.arange(27).reshape(3, 3, 3)
m2 = np.arange(9).reshape(3, 3)
print("m1", m1, "\nm2", m2, "\nprod", m1 * m2)

# %% {"cell_style": "center", "hide_input": false, "tags": ["raises-exception", "level_intermediate"]}
# le code du contre-exemple
m1 = np.arange(6).reshape(2, 3)
m2 = np.arange(8).reshape(2, 4)
try:
    m1 * m2
except ValueError as e:    
    print(f'{m1}\n+\n{m2}\n {e}')

# %% [markdown] {"tags": ["level_intermediate", "framed_cell"]}
# ### exemple de broadcasting - avancés
#
# <br>
#
# * une matrice `A`$=\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\  \end{pmatrix}$ de forme `(2_A, 3_A)`
#     
#     
# * un tableau `b` réduit à  un scalaire $\begin{pmatrix}b_1 \\ \end{pmatrix}$ de forme $(1_b,)$  
#     
#
# * calculons `A + b`
#     
# <br>
#     
# la forme de `A` est $(2_A, 3_A)$ la forme de `b` est ($1_b$,)
# 1. on compare les dimensions de droite: $3_A$ et $1_b$
# 1. $b$ est élargi à $\begin{pmatrix} b_1 & b_1 & b_1 \end{pmatrix}$ de forme $(1_b, 3_b)$
#
# <br>
#     
# on ajoute maintenant un tableau de forme $(2_A, 3_A)$ à une ligne de forme $(1_b, 3_b)$  
# $\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\  \end{pmatrix} + \begin{pmatrix} b_1 & b_1 & b_1  \end{pmatrix}$   
#    
# <br>
#     
# 1. on compare les dimensions précédentes: $2_a$ et $1_b$
# 1. `b` est élargi à la dimension $(2_b, 3_b)$
#  
# <br>
#     
# on ajoute maintenant un tableau de forme $(2_A, 3_A)$ à un tableau de forme  $(2_b, 3_b)$  
#     
#   $\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\  \end{pmatrix} + \begin{pmatrix} b & b & b \\ b & b & b \end{pmatrix} = \begin{pmatrix} a_{11} + b & a_{12} + b & a_{13} + b \\ a_{21} + b & a_{22} + b & a_{23} + b \\  \end{pmatrix}$   
#
# <br>
#     
# les formes sont désormais compatibles, les deux tableaux peuvent être ajoutés

# %% [markdown]
# ***

# %% [markdown] {"tags": ["level_intermediate", "framed_cell"]}
# ### exemple de broadcasting - ajout ligne et colonne
#
# <br>
#
# on veut faire l'opération $\begin{pmatrix} a_{1} & a_{2} & a_{3} \end{pmatrix} + \begin{pmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{pmatrix}$
#
# <br>
#     
# la forme de la matrice-ligne `a` est $(1_a, 3_a)$, la forme de la matrice-colonne `b` est $(4_b, 1_b)$
#
# <br>
#     
#
# `numpy` compare $3_a$ à $1_b$ et élargit *b* à $\begin{pmatrix} b_1 & b_1 & b_1 \\ b_2 & b_2 & b_2 \\ b_3 & b_3 & b_3 \\ b_4 & b_a & b_4 \end{pmatrix}$
#
# <br>
#     
#
# on ajoute maintenant un tableau $(1_a, 3_a)$ à une matrice $(4_b, 3_b)$
#
# <br>
#     
#
# $\begin{pmatrix} a_{1} & a_{2} & a_{3} \end{pmatrix} + \begin{pmatrix} b_1 & b_1 & b_1 \\ b_2 & b_2 & b_2 \\ b_3 & b_3 & b_3 \\ b_4 & b_a & b_4 \end{pmatrix}$
#
# <br>
#     
#  
#    
# `numpy` compare les dimensions $1_a$ et $4_b$ et élargit $a$ à $\begin{pmatrix} a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \end{pmatrix}$
#
# <br>
#     
#    
#  
# $\begin{pmatrix} a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \end{pmatrix} + \begin{pmatrix} b_1 & b_1 & b_1 \\ b_2 & b_2 & b_2 \\ b_3 & b_3 & b_3 \\ b_4 & b_a & b_4 \end{pmatrix} = \begin{pmatrix} a_{1} + b_1 & a_{2} + b_1 & a_{3} + b_1 \\ a_{1} + b_2 & a_{2} + b_2 & a_{3} + b_2 \\ a_{1} + b_3 & a_{2} + b_3 & a_{3}  + b_3\\ a_{1} + b_4 & a_{2} + b_4 & a_{3} + b_4 \end{pmatrix}$
#  
#
# <br>
#
# les formes sont désormais compatibles, les deux tableaux ont pu être ajoutés

# %% [markdown] {"tags": ["framed_cell"]}
# ### exemple de broadcasting en dimension > 2
#
# <br>
# deux groupes de 3 matrices
#     
# ```python
# grp = np.arange(1, 37).reshape(2, 3, 2, 3)
# grp -> [[[[ 1,  2,  3],
#           [ 4,  5,  6]],
#
#          [[ 7,  8,  9],
#           [10, 11, 12]],
#
#          [[13, 14, 15],
#           [16, 17, 18]]],
#
#
#         [[[19, 20, 21],
#           [22, 23, 24]],
#
#          [[25, 26, 27],
#           [28, 29, 30]],
#
#          [[31, 32, 33],
#           [34, 35, 36]]]]
# ```
#
#   
# une matrice
#     
# ```python
# mat = np.array([[100, 200, 300], [400, 500, 600]])
# mat -> [[100, 200, 300],
#         [400, 500, 600]]
# ```
#     
# <br>
# l'opération entre les deux tableaux
#     
# ```python
# grp+mat
#     
# -> ([[[[101, 202, 303],
#        [404, 505, 606]],
#
#       [[107, 208, 309],
#        [410, 511, 612]],
#
#       [[113, 214, 315],
#        [416, 517, 618]]],
#
#
#      [[[119, 220, 321],
#        [422, 523, 624]],
#
#       [[125, 226, 327],
#        [428, 529, 630]],
#
#       [[131, 232, 333],
#        [434, 535, 636]]]])
# ```

# %%
# le code
grp = np.arange(1, 37).reshape(2, 3, 2, 3)
mat = np.array([[100, 200, 300], [400, 500, 600]])
grp+mat

# %% [markdown]
# ## exercice (avancés)

# %% [markdown] {"tags": ["level_advanced"]}
# * implémentez en Python la fonction qui détermine si deux formes (données par des tuples) sont compatibles pour le broadcasting  
# renvoie `True` si compatible et `False` sinon
# ```python
# def are_broadcast_compatible(shape1, shape2):
#     ...
# ```
#
# * faites une fonction de test qui crée deux tableaux en `numpy`, les ajoute et renvoie `True` si l'addition fonctionne et `False` sinon
# ```python
# def test_compatibility(shape1, shape2):
#     ...
# ```
#
# exemples
#
# ```python
# s1 = (1, 2)
# s2 = (3, 1)
# print(test_compatibility(s1, s2))
# print(are_broadcast_compatible(s1, s2))
# -> True
#    True
# ```
#
# ```python
# s1 = ()
# s2 = ()
# print(test_compatibility(s1, s2))
# print(are_broadcast_compatible(s1, s2))
# -> True
#    True
# ```
#
# ```python
# s1 = (2, 2, 1, 2)
# s2 = (2, 1, 3, 1)
# print(test_compatibility(s1, s2))
# print(are_broadcast_compatible(s1, s2))
# -> True
#    True
# ```
#
#
# ```python
# s1 = (2, 2, 1)
# s2 = (2, 1, 3, 1)
# print(test_compatibility(s1, s2))
# print(are_broadcast_compatible(s1, s2))
# -> False
#    False
# ```

# %%
# à vous
def test_compatibility(s1, s2):
    pass

def are_broadcast_compatible(s1, s2):
    pass


# %% {"scrolled": true, "tags": ["raises-exception"]}
# pour corriger votre code

s1 = (1, 2)
s2 = (3, 1)
print(test_compatibility(s1, s2))
print(are_broadcast_compatible(s1, s2))

s1 = ()
s2 = ()
print(test_compatibility(s1, s2))
print(are_broadcast_compatible(s1, s2))

s1 = (2, 2, 1, 2)
s2 = (2, 1, 3, 1)
print(test_compatibility(s1, s2))
print(are_broadcast_compatible(s1, s2))

s1 = (2, 2, 1)
s2 = (2, 1, 3, 1)
print(test_compatibility(s1, s2))
print(are_broadcast_compatible(s1, s2))
