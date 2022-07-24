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
#   notebookname: "alg\xE8bre lin\xE9aire"
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>UE12</span>
# <span><img src="media/ensmp-25-alpha.png" /></span>
# </div>

# %%
from IPython.display import HTML
HTML('<link rel="stylesheet" href="slides-notebook.css" />')

# %%
import numpy as np

# %% [markdown]
# # algèbre linéaire

# %% [markdown]
# ## contenu de ce notebook (notebook à sauter)
#
# <br>
#
# **IMPORTANT**  
# ce notebook est utile aux enseignements de mathématiques  
# **sachez qu'il existe** pour vous y référer  
# **sans l'étudier** en cours d'informatique
#
# <br>
#
# **liste des fonctions présentées** (succinctement)
#
#     
# | fonctions           |   comportement |
# |-----------------|--------|
# | `np.dot` | produit de matrice |
# | `np.linalg.norm` | normes de matrice |
# | `np.transpose` | transposition de matrice |
# | `np.linalg.det` | déterminant |
# | `np.linalg.inv` | inversion |
# | `np.linalg.eig` | valeurs propres |
# | `np.linalg.solve` | résolution de système linéaire |
# | `np.eye`       |matrice identité  |
# | `np.diag`      | matrice diagonale|
#     
# </div>

# %% [markdown] {"tags": ["framed_cell"]}
# ##  introduction et contexte
# <br>
#
# les fonctions d'algèbre linéaire `numpy.linalg` sont très efficaces, parce que
# 1. fondées sur des algorithmes efficaces 
# 1. codées dans des langages *bas niveau* très proches de la mémoire donc rapides
# 1. implémentations qui tirent parti du *multithreading*  
# (découpage d'un programme en sous-programmes s'exécutant *en même temps*)
#     
# <br>
#     
#
# pour les différences entre les fonctions de `numpy` et de `scipy`  
# lire les documentations  https://docs.scipy.org/doc/numpy/reference/routines.linalg.html
#     
# <br>
#      
# nous avons vu précédemment des opérations élément-par-élément comme `numpy.mult`(`*`)  
# nous allons voir rapidement, les fonctions dédiées à l'algèbre linéaire
#
# <br>
#    
# la librarie `numpy` est utilisée dans vos cours de mathématiques  
# pour les manipulations de vecteurs et de matrices 
#     
# <br>    
#
# aussi nous ne regardons que quelques fonctions de base en dimension < à 3
#                                                                        
# pour plus d'information, regardez la documentation
#
# https://numpy.org/doc/stable/reference/routines.linalg.html

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell"]}
# ## terminologie
#
# <br>
#     
# on va se mettre d'accord sur les terminologies `matrice`, `vecteur` et `produit`
#
# <br>
#     
# attention au type des éléments
# * les `matrices` et les `vecteurs` seront des `numpy.ndarray`
# * les affectations peuvent entraîner des modifications de valeurs
#
# <br>
#     
# ```python    
# A = np.array([[2, 3, -7], [6, -4, 5]])
# A.dtype # int64
# A[0] = np.pi
# A ->[[ 3,  3,  3], # A[0] vaudra 3 pas np.pi
#      [ 6, -4,  5]]
# ```

# %%
A = np.array([[2, 3, -7], [6, -4, 5]])
print(A.dtype)
A[0] = np.pi
A

# %% [markdown] {"tags": ["framed_cell"]}
# ## les matrices et vecteurs
#
# <br>
#     
# une **matrice** de $m$ lignes et $n$ colonnes
# * est un tableau `numpy.ndarray`
# * de dimension `2`  
# * de forme `(m, n)`
#     
# exemple
#     
# ```python
# m, n = 4, 3
# A = np.arange(12).reshape(m, n)
# print(A)    
# print(A.ndim)   # 2
# print(A.shape)  # (4, 3)
# ```    
# les objets de forme `(1, n)` et `(m, 1)` sont des matrices 
#     
# <br>
#  
# ----------------------------------
#     
# un **vecteur** de taille $n$
# * est un `np.ndarray`
# * de dimension `1`
# * de forme `(n,)`
#
# exemple
#
# ```python
# V = np.array([1, -3, 8])
# print(V)
# print(V.ndim)
# print(V.shape)
# ```

# %%
# le code
m, n = 4, 3
A = np.arange(12).reshape(m, n)
print(A)    
print(A.ndim)
print(A.shape)

# %% {"scrolled": true}
# le code
V = np.array([1, -3, 8])
print(V)
print(V.ndim)
print(V.shape)

# %% [markdown] {"tags": ["framed_cell"]}
# ## le produit d'une matrice et d'un vecteur `numpy.dot`
#
# <br>
#     
# $A\cdot V$
# * `np.dot(A, V)`
# * ou aussi `A.dot(V)`
#     
#     
# <br>
#     
# matrice    
# ```python
# m, m = 4, 3    
# A = np.arange(12).reshape(m, n)
# A -> [[ 0  1  2]
#       [ 3  4  5]
#       [ 6  7  8]
#       [ 9 10 11]]
# ```
#    
# vecteur    
# ```python
# V = np.arange(3).reshape(n)
# V -> [0 1 2]
# ```
#     
# produit
# ```python
# np.dot(A, V)
# -> [ 5 14 23 32]
# ```
#
# ou encore
# ```python
# A.dot(V)
# -> [ 5 14 23 32]    
# ```

# %%
m, n = 4, 3
A = np.arange(12).reshape(m, n)
print(A)
V = np.arange(3).reshape(n)
print(V)
print(np.dot(A, V))
print(A.dot(V))

# %% [markdown] {"tags": ["framed_cell"]}
# ## le produit de deux matrices `numpy.dot`
#
# <br>
#     
# $A\cdot B$
# * `np.dot(A, B)`
# * ou aussi `A.dot(B)`
#     
#     
# <br>
#     
# matrices `A` et `B`   
# ```python
# A = np.arange(12).reshape(m, n)
# A -> [[ 0  1  2]
#       [ 3  4  5]
#       [ 6  7  8]
#       [ 9 10 11]]
#
# B = np.arange(10, 22).reshape(n, m)
# B -> [[10 11 12]
#       [13 14 15]
#       [16 17 18]
#       [19 20 21]]
# ```
#    
# produit
# ```python
# np.dot(A, B)
# -> [[102 108 114]
#     [334 356 378]
#     [566 604 642]
# ```
#
# ou encore
# ```python
# A.dot(B)
# -> [[102, 108, 114]
#     [334, 356, 378]
#     [566, 604, 642]]
# ```
#     
#
# </div>

# %%
# le code
m, n = 3, 4
A = np.arange(12).reshape(m, n)
print(A)
B = np.arange(10, 22).reshape(n, m)
print(B)
np.dot(A, B)
A.dot(B)

# %% [markdown] {"tags": ["framed_cell"]}
# ##  produit matriciel avec `@` et `numpy.matmul`
#
# <br>
#  
# il existe une fonction `numpy.matmul`  
# qui s'écrit aussi sous la forme `@`
#     
# <br>
#     
# ```python
# np.matmul(A, B)
# ```
#     
#   
# ```python
# A@B
# ```
# <br>
#     
# `numpy.matmul` et `np.dot`
# * se ressemblent en dimension 2
# * la multiplication par un scalaire n'est  pas possible avec `numpy.matmul`
# * en dimensions supérieure à 2, leur comportement diffère complètement
#
# **préférer utiliser `numpy.dot`**

# %%
# le code
np.matmul(A, B)
A @ B

# %% [markdown] {"tags": ["framed_cell"]}
# ## le produit scalaire
#
# <br>
#
# `numpy.dot` appliquée à deux vecteurs donne leur  produit scalaire
#     
# ```python
# V1 = np.array([1, -3, 8])
# V1.shape # (3,)
# V1 -> [ 1, -3,  8]
# ```
# <br>
#      
# ```python
# V2 = np.array([-6, 4, -7])
# V2.shape # (3,)
# V2 -> [-6 4 -7]
# ```
#
# <br>
#
# ```python
# np.dot(V1, V2)
# -> -74
# ```
#
#      
# ```python
# V1.dot(V2)
# ```

# %%
#le code
V1 = np.array([1, -3, 8])
V1.shape # (3,)
V1

# %%
#le code
V2 = np.array([-6, 4, -7])
V2.shape # (3,)
V2

# %%
#le code
np.dot(V1, V2)

# %% [markdown] {"tags": ["framed_cell"]}
# ## la norme de vecteur
#
# <br>
#  prenons un vecteur $V =[v_1, ..., v_n]$ 
#     
# la norme `np.linalg.norm(V)`  
# est la racine carré du produit scalaire du vecteur par lui-même  
#     
#  $\displaystyle \left\|{ {V}}\right\|_{2}={\sqrt {v_{1}^{2}+\cdots +v_{n}^{2}}}$
#     
#
# <br>
#
# un vecteur    
# ```python
# V = np.array([1, -3, 8])
# ```
#
# <br>
#
# la fonction idoine
# ```python
# np.linalg.norm(V)
# -> 8.602325267042627
# ```
#
# <br>
#     
# autre calcul
# ```python
# np.sqrt(np.dot(V, V))
# -> 8.602325267042627
# ```
#     
# <br>
#     
#  
# autre calcul
# ```python
# np.sqrt(np.sum(V*V))
# -> 8.602325267042627
# ```   
#     
# <br>
#     
# pour les autres normes, regardez la documentation
#     
# https://numpy.org/doc/stable/reference/routines.linalg.html

# %%
# le code
V = np.array([1, -3, 8])
np.linalg.norm(V)
np.sqrt(np.dot(V, V))
np.sqrt(np.sum(V*V))

# %% [markdown] {"tags": ["framed_cell"]}
# ## la transposée d'une matrice
#
# <br>
#
# fonction `numpy.transpose`  
# ou `.T` pour écrire des codes plus lisibles
#     
# <br>
#
# une matrice
#     
# ```python
# A = np.arange(1, 13).reshape(4, 3)
# A -> [[ 1  2  3]
#       [ 4  5  6]
#       [ 7  8  9]
#       [10 11 12]]
# ```
#
# <br>
#
# sa transposée
#     
# ```python
# np.transpose(A)
# -> [[ 1,  4,  7, 10],
#     [ 2,  5,  8, 11],
#     [ 3,  6,  9, 12]])
# ```
# <br>
#
# ou encore
#     
# ```python
# A.T
# ```

# %%
# le code
A = np.arange(1, 13).reshape(4, 3)
print(A)
print(np.transpose(A))
print(A.T)

# %% [markdown] {"tags": ["framed_cell"]}
# ## les matrices identité
#
# <br>
#
# se construisent avec la fonction `numpy.eye`  
# (*eye* et *I* se prononcent pareil en anglais)
#     
# <br>
#     
# la fonction renvoie des matrices de type flottant
#     
# <br>
#
# ```python
# I = np.eye(5)
# I.shape # (5, 5)
# I.dtype # 'float64'
# I ->  [[1., 0., 0., 0., 0.],
#        [0., 1., 0., 0., 0.],
#        [0., 0., 1., 0., 0.],
#        [0., 0., 0., 1., 0.],
#        [0., 0., 0., 0., 1.]]
# ```

# %%
# le code
I = np.eye(5)
print(I.shape)
print(I.dtype)

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell"]}
# ## le déterminant d'une matrice
#
# <br>
#     
# la fonction `numpy.linalg.det`  
# déclenche l'exception `np.linalg.LinAlgError` si la matrice n'est pas carrée
# <br>
#     
# une matrice carrée
#     
# ```python
# A = 2*np.eye(3)
# A -> [[2., 0., 0.],
#       [0., 2., 0.],
#       [0., 0., 2.]]
# ```
# <br>
#     
# son déterminant
#     
# ```python
# np.linalg.det(A)
# ->  7.999999999999998   
# ```
#
# <br>
#     
# tentative de calcul du déterminant sur une matrice non-carrée
# ```python
# B = np.array([[2, 3, 4], [5, 6, 7]])
# try:
#     np.linalg.det(B)
# except np.linalg.LinAlgError as e:
#     print(e)
# -> Last 2 dimensions of the array must be square
# ```

# %%
# le code
A = 2*np.eye(3)
np.linalg.det(A)

# %%
#le code
B = np.array([[2, 3, 4], [5, 6, 7]])
try:
    np.linalg.det(B)
except np.linalg.LinAlgError as e:
    print(e)

# %% [markdown] {"tags": ["framed_cell"]}
# ## les matrices diagonales
#
# On peut créer une matrice diagonale à partir de la liste des éléments de sa diagonale
#
# <br>
#  
# `numpy.diag`
# * sur une matrice, extrait le tableau des éléments de sa diagonale
# * sur une liste d'éléments, construit la matrice diagonale
#
# <br>    
# la matrice
#     
# ```python
# A = np.random.randint(-100, 100, size=(3, 4))
# A ->  [[-11 -76  91 -97]
#        [ 65  68 -40  55]
#        [ 30  81 -45  28]]
# ```
# sa diagonale
#     
# ```python
# np.diag(A)
# -> [-11  68 -45]
# ```
#
# <br>
#     
# un vecteur  
# possible avec une liste Python
#     
# ```python
# l = np.array([9, -45, 6])
# ```    
# <br>
#     
# la matrice diagonale
#     
# ```python
# np.diag(l)
# -> [[  9,   0,   0],
#     [  0, -45,   0],
#     [  0,   0,   6]]
# ```

# %%
# le code
A = np.random.randint(-100, 100, size=(3, 4))
print(A)
np.diag(A) 

# %%
# le code
l = np.array([9, -45, 6])
np.diag(l)

# %% [markdown] {"tags": ["framed_cell"]}
# ## la trace d'une matrice
#
# <br>
#
# `numpy.trace` fait la somme des éléments de la diagonale de la matrice
#
# <br>
#     
# la matrice `A`
#     
# ```python
# A = np.arange(9).reshape(3, 3)
# A -> [[0, 1, 2],
#       [3, 4, 5],
#       [6, 7, 8]]
# ```
#
# <br>
#     
# la trace de `A`
#     
# ```python    
# np.trace(A)
# -> 12
# ```
#     
# <br>
#     
# la trace de `A`
#     
# ```python    
# np.sum(np.diag(A))
# -> 12
# ```
#     
# </div>

# %%
# le code
A = np.arange(9).reshape(3, 3)
print(A)
print(np.trace(A))
print(np.sum(np.diag(A)))

# %% [markdown] {"tags": ["framed_cell"]}
# ## l'inversion d'une matrice
#
# <br>
#
# `numpy.linalg.inv(A)` est le calcul de $A^{-1}$
#     
# <br>
# une matrice
#     
# ```python
# R = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=np.float)
# R -> [[0., 1., 0.],
#       [0., 0., 1.],
#       [1., 0., 0.]]
# ```
#     
# <br>
#     
# son inverse   
# ```python
# np.linalg.inv(R)
# -> [[0., 0., 1.],
#     [1., 0., 0.],
#     [0., 1., 0.]]   
# ```
#
# <br>
#
# testons si cela fonctionne comme attendu $A^{-1}A = I$
#    
# ```python
# np.all(np.dot(R, IR) == np.eye(3))
# -> True
# ```
#
#     
# <br>
#     
# cet exemple est correct mais ce n'est pas toujours le cas  
# puisque les calculs informatiques sont approchés   
# (un exemple dans la slide suivante)

# %% {"cell_style": "center"}
# le code
R = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=np.float)
print(R)
IR = np.linalg.inv(R)
print(IR)
print(np.all(np.dot(R, IR) == np.eye(3)))

# %% [markdown] {"tags": ["framed_cell"]}
# ## calculs approchés (avec tolérance)
#
# <br>
#     
#     
# testons $A^{-1}A = I$ sur une matrice quelconque de floats  
# générés aléatoirement
#     
#    
# ```python
# A = np.random.random(size=(3, 3))
# I = np.eye(len(A))      # matrice identité
# A_1 = np.linalg.inv(A)
# np.all(I == np.dot(A_1, A))
# -> False
# ```    
#
# <br>
#     
# dans ce cas  $A^{-1}A \neq I$
#     
# <br>
#     
# regardons le produit $A^{-1}A$
#     
# ```python
# np.dot(A_1, A)
# -> [[ 1.00000000e+00  9.47934554e-18  3.24735868e-17]
#     [-2.69206416e-17  1.00000000e+00 -4.22197093e-18]
#     [ 6.52983031e-18  1.58976614e-17  1.00000000e+00]]
# ```      
#     
# <br>
#     
#     
# il est très proche de $I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ \end{bmatrix}$ mais pas exactement égal  
#     
# en effet si en mathématiques on écrit $A^{-1}A = I$, en informatique c'est plutôt $A^{-1}A \approx I$  
# (*égal* à une tolérance près)  
#
# <br>
#     
# d'ou l'intérêt de la fonction de comparaison `numpy.isclose`  
# qui effectue une comparaison de deux tableaux à une tolérance près
#     
# <br>
#     
# ```python
# np.all(np.isclose(np.dot(A_1, A), I))
# -> True
# ```    
# <br>
#     
# ça fonctionne bien comme attendu

# %%
A = np.random.random(size=(3, 3))
I = np.eye(len(A))
A_1 = np.linalg.inv(A)
np.all(I == np.dot(A_1, A))
print(np.dot(A_1, A))
np.all(np.isclose(np.dot(A_1, A), I))

# %% [markdown] {"tags": ["framed_cell"]}
# ## les valeurs propres d'une matrice (*eigen values*)
#
# <br>
#
# on va calculer les $v$ tels que:
#    - $f(v) = \lambda v$ 
#    - $M \cdot v = \lambda v$
#  `
#
#
# avec la fonction `numpy.linalg.eig` qui retourne
# * la liste des valeurs propres *eigen-values*
# * et la liste des vecteurs propres *eigen-vectors*
#
# <br>
#     
# prenons une matrice `M`    
#    
# ```python
# M = np.random.random(size=(3, 3))
# ```
#     
# <br>
#     
# calculons ses valeurs et vecteurs propres `M`    
#    
# ```python
# alpha, v  = np.linalg.eig(M)
# alpha.shape # (3,)
# v.shape # (3, 3)  
# ```
# * les 3 valeurs propres sont dans un vecteur
# * les 3 vecteurs propres forment les colonnes d'une matrice
#     
# <br>
#     
# prenons le premier vecteur propre et sa valeur propre
#     
# ```python
# v0 = v[:, 0] # premier vecteur propre (première colonne)
# alpha0 = alpha[0] # première valeur propre
# ```
#
# <br>
#     
# vérifions si $M \cdot v_0 = \lambda_0 v_0$  
# i.e. si `np.dot(M, v0) ==  alpha0*v0))`
#     
# <br>
#
# naturellement les calculs sont approchés  
# il faut utiliser l'égalité à une tolérance près
#     
# <br>
#     
# ```python
# np.all(np.isclose(np.dot(M, v0),  alpha0*v0))
# -> True
# ```
#    
# c'est bien ça
#     
# <br>
#     
# exercice:  
#     parcourez les vecteurs propres et les valeurs propres  
# et vérifiez, pour chaque couple si $M \cdot v_i \approx \lambda_i v_i$

# %% {"cell_style": "center"}
# le code
M = np.random.random(size=(3, 3))
alpha, v  = np.linalg.eig(M)
alpha.shape, v.shape


v0 = v[:, 0] # le premier vecteur propre
alpha0 = alpha[0] # la première valeur propre

np.all(np.isclose(np.dot(M, v0),  alpha0*v0))

# %%
# votre code ici

# %% [markdown] {"tags": ["framed_cell"]}
# ## résolution d'un système linéaire
#
# <br>
#
# on va calculer avec la fonction `numpy.linalg.solve`  
# les racines du système linéaire $A \cdot x = b$
#     
# <br>
#
# prenons une matrice
#     
# ```python
# A = np.random.random(size=(3, 3))
# ```
# <br>
#     
# prenons un vecteur
#     
# ```python
# b = np.array([1, 2, 3])
# ```
#     
# <br>
#
# calculons la racine de l'équation $A \cdot x = b$
#     
#     
# ```python
# x = np.linalg.solve(A, b)
# ```
#
# <br>
#
# vérifions si $A \cdot x \approx b$
#     
#    
# ```python
# np.all(np.isclose(np.dot(A, x), b))
# -> True
# ```
#     
# <br>
#
# une erreur `numpy.linalg.LinAlgError` sera levée
# * si elle n'est pas carrée
# * si la matrice n'est pas inversible

# %%
# le code
A = np.random.random(size=(3, 3))
b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)
np.all(np.isclose(np.dot(A, x), b))

