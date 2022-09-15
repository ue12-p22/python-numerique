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
#     title: les tableaux
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %% [markdown]
# # les tableaux

# %% [markdown]
# ## contenu de ce notebook (sauter si déjà acquis)
#
# <br>
#
#
# fonctions de création de tableaux `np.ndarray`
#
# | les fonctions | ce qu'elles font |
# |-|-|
# | `np.array` | renvoie la version ndarray d'un tableau existant |
# | `np.empty` | renvoie un ndarray vide (éléments non initialisés) |
# | `np.zeros` | renvoie un ndarray rempli de *0.* (float) |
# | `np.ones` | renvoie un ndarray rempli de *1.* (float) |
# | `np.linspace` | un vecteur de valeurs bien espacées entre deux bornes |
# | `np.random.randint` | entiers aléatoirement générés |
# | `np.random.randn` | flottants aléatoirement générés |
#
#
#
# <br>
#
# attributs/méthodes de manipulation de tableaux `np.ndarray`
#
# | attributs/méthodes | ce qu'ils font |
# |-|-|
# | `np.ndarray.shape`    | la forme du tableau (tuple) |
# | `np.ndarray.size`     | le nombre d'éléments du tableau |
# | `np.ndarray.ndim`     | le nombre de dimensions du tableau |
# | `np.ndarray.dtype`    | le type des éléments |
# | `np.ndarray.itemsize` | la taille en octet d'un élément |
# | `np.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octet |
# | `np.ndarray.astype`   | copie tableau avec autre taille des éléments |
#
# <br>
#
# la taille (en nombre d'octets) des éléments d'un `numpy.ndarray` existant est constante  
# une modification peut causer une conversion de la valeur
#
# <br>
#
# calculs de temps d'exécution avec `%timeit`

# %% [markdown] tags=["framed_cell"]
# ## rappels
#
# <br>
# <br>
#     
# Python ne possède pas, de base, de type adapté aux tableaux multi-dimensionnels 
#
# <br>
#     
# ceux-ci sont proposés par la librairie numérique `numpy`  
# qu'il faut installer séparément (`pip install numpy` dans le terminal)

# %%
import numpy as np

# %% [markdown] tags=["framed_cell"]
# ## tableaux  multi-dimensionnels `numpy`
# <br>
#     
# créés par la méthode `numpy.array`  
# (ici plus précisément `np.array` comme l'identifiant utilisé lors de l'import est `np` mais on reste genéral)
#     
# <br>
#     
# leur type est `numpy.ndarray` (tableau en dimension n)
#  
# <br>
#     
# attributs et méthodes que nous allons utiliser souvent
#     
# | nom                      | comportement                                     |
# |--------------------------|--------------------------------------------------|
# | `numpy.ndarray.shape`    | la forme du tableau (tuple)                      |
# | `numpy.ndarray.dtype`    | le type des éléments                             |
# | `numpy.ndarray.astype`   | crée tableau avec nouveau type d'éléments        | 
#
# <br>
#     
# ou moins souvent
#     
# | nom                      | comportement                                     |
# |--------------------------|--------------------------------------------------|
# | `numpy.ndarray.ndim`     | le nombre de dimensions du tableau               |
# | `numpy.ndarray.itemsize` | la taille en octet d'un élément                  |
# | `numpy.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octets |

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### création d'un tableau multi-dimensionnel
# <br>
# <br>
#
# reprenons notre matrice en Python brut
#
# ```python
# matrice = [
#     [1, 2, 3, 4, 5], 
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]
# ```
#     
# <br>
#     
# avec la fonction `numpy.array` nous créons un tableau multi-dimensionnel initialisé avec notre matrice
#
# ```python    
# mat = np.array(matrice)
# ```
#
# <br>
#     
# nous n'avons indiqué
#
# * ni la forme du tableau
# * ni le type des éléments
#
# `numpy.array` a tout déduit
#  
#     
# <br>
#     
# **type** de `mat` est `numpy.ndarray` i.e. *n-dimensional-array*
#
# ```python
# type(mat)
#     -> <class 'numpy.ndarray'>
# ```

# %% [markdown]
# le code

# %%
matrice = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

mat = np.array(matrice)

print(mat)

print(type(mat))

# %% [markdown] tags=["framed_cell"]
# ###  type et taille mémoire des éléments du tableau
# <br>
# <br>
#     
# ```python
# matrice = [
#     [1, 2, 3], 
#     [4, 5, 6]
# ]    
# mat = np.array(matrice)
# ```
# <br>
#     
# l'attribut `numpy.ndarray.dtype` donne le **type des éléments** du tableau
#
# ```python
#     
# mat.dtype
# -> dtype('int64') 
# ```
# ou bien
# ```python
#     
# mat.dtype
# -> dtype('int32') 
# ```
# <br>
#     
# tous les éléments sont du même type et de la même taille  
# (ici des entiers signés codés sur 64 bits = 8 octets ou bien 32 bits = 4 octets)
#
# <br>
#     
# l'attribut `numpy.ndarray.itemsize` donne le nombre d'octets d'un élément du tableau
#
# ```python
# mat.itemsize
# -> 8 # chaque élément fait 8 octets dans le cas int64
# ```
#     
# <br>
#     
# l'attribut `numpy.ndarray.nbytes`  donne le nombre d'octets total du tableau
#
# ```python
# mat.nbytes
# -> 48 # 6 éléments de 8 octets chacun dans le cas int64
# ```

# %%
# le code
matrice = [
    [1, 2, 3], 
    [4, 5, 6]
]    
mat = np.array(matrice)
mat.dtype, mat.itemsize, mat.nbytes

# %% [markdown] tags=["framed_cell"]
# ### taille, forme, dimension du tableau    
# <br>
# <br>
#     
# ```python
# matrice = [
#     [1, 2, 3], 
#     [4, 5, 6]
# ]    
# mat = np.array(matrice)
# ```
#     
#   
# <br>    
#     
#     
# l'attribut `numpy.ndarray.shape` donne la forme d'un tableau sous la forme d'un tuple
#     
# ```python
# mat.shape
# -> (2, 3) # 2 lignes et 3 colonnes
# ```    
#   
#     
#     
# <br>
#     
# l'attribut `numpy.ndarray.size` donne le nombre d'éléments du tableau
#     
# ```python
#    
# mat.size # mat.shape[0] * mat.shape[1]
# -> 6
# ```    
#     
# <br>
#     
# l'attribut `numpy.ndarray.ndim` donne la dimension d'un tableau
#    
# ```python
# mat.ndim # len(mat.shape)
# -> 2
# ```

# %%
# le code
print(mat.shape)
print(mat.size, mat.shape[0] * mat.shape[1])
print(mat.ndim, len(mat.shape))

# %% [markdown] tags=["framed_cell"]
# ### création d'un tableau avec le type des éléments    
# <br>
# <br>
#     
# on peut laisser `numpy` décider du type des éléments    
#
# ```python
# matrice = [
#     [-128, -78, -32], 
#     [17, 5, 127]
# ]
# mat = np.array(matrice)
# mat.dtype
# -> int64
# ```
#     
# <br>
#     
# calculons l'élément minimum et l'élément maximum d'un tableau
#     
# ```python
# mat.min(), mat.max()
# -> -128 127
# ```
#
# <br>
#     
# Combien faut-il d'octets, au minimum, pour stocker des entiers entre $-128$ et $127$ ?  
# un seul octet
#
# <br>
#     
# Quel type d'entier dois-je utiliser ?
#     
# <br>
#     
# **rappel avec n bits**, on représente $2^n$ valeurs entières
# - soit des entiers signés $\in [ -2^{n-1}$, $2^{n-1}-1]$
# - soit des entiers non signés $\in [0, 2^n-1]$
#     
#     
# <br>
#     
#     
# on peut donc utiliser le type  
#
# * `numpy.int8` pour le type des entiers signés sur 8 bits  
#   $256$ valeurs de $-128$ à $127$
#
# * le type correspondant sera `numpy.int8` (entier signé sur 8 bits)
#     
# <br>
#     
#
# avec le paramètre `dtype` on indique, à la fonction `numpy.array`, le type des éléments
#     
# ```python
# matrice = [
#     [-128, -78, -32], 
#     [17, 5, 127]
# ]
# mat = np.array(matrice, dtype=np.int8) 
# mat.dtype
# -> int8
# ```   
#
# <br>
#     
# **trompons-nous** et demandons un type `numpy.uint8`  
# naturellement, `numpy` vous obéit aveuglement ...  
# si il rencontre un problème avec une valeur: il modifie la valeur, pas le type que vous imposez ! 
#     
# ```python
# mat = np.array(matrice, dtype=np.uint8) 
# mat
# -> [[128, 178, 224], # ouh là là ! 128 = 256 - 128
#                      # (complément à 2)
#     [ 17,   5, 127]], dtype=uint8
# ```

# %%
# le code
matrice = [
    [-128, -78, -32], 
    [17, 5, 127]  
]
mat = np.array(matrice)

print(mat.min(), mat.max())
print(mat.dtype)

# %% scrolled=true
# le code avec type
matrice = [
    [-128, -78, -32], 
    [17, 5, 127]
]
mat = np.array(matrice, dtype=np.int8) 
mat

# %%
# le code avec erreur
matrice = [
    [-128, -78, -32], 
    [17, 5, 127]
]
mat = np.array(matrice, dtype=np.uint8)
mat

# %% [markdown]
# **exercice**
#
# 1. créez un tableau pour stocker la matrice ci-dessous avec le plus petit type entier non signé
#
# ```python
# l = [[  0,   8,  34,   8],
#      [255,  61, 128, 254]]
# ```
#
# 2. puis, essayez avec le type `numpy.int8`

# %%
# votre code ici

# %% [markdown] tags=["framed_cell"]
# ### modifier le type des éléments d'un tableau existant    
# <br>
# <br>
#      
# la méthode `numpy.ndarray.astype` crée un nouveau tableau de la même forme que le tableau initial   
# avec la taille indiquée pour les éléments
#     
# ```python
# l = [[  0,   8,  34,   8],
#      [255,  61, 128, 254]]
#
# mat = np.array(l)
# mat1 = mat.astype(np.int8)
# mat1
# ```
#     
# <br>
#     
# `mat` et `mat1` ne partagent **pas** le tableau d'éléments sous-jacent  
# `mat1` est **une copie indépendante** avec la nouvelle taille  
# l'ancien `mat` existe toujours avec sa taille initiale

# %%
# le code
l = [[  0,   8,  34,   8],
     [255,  61, 128, 254]]

mat = np.array(l)
print(    mat     )
mat1 = mat.astype(np.int8)
print(    mat1    )
print(    mat     )

# %% [markdown] tags=["framed_cell"]
# ## `numpy` calcule à taille constante    
# <br>
# <br>
#
# créons un tableau avec des éléments de type entier (type par défaut)
#     
# ```python
# l = [-1, 2, 3]
# mat = np.array(l)
# mat
#     -> [-1, 2, 3]
# ```
# <br>
#     
# multiplions les éléments du tableau `mat` par $100$
#     
# <br>
#     
#      
# ```python
# mat*100
# -> [-100,  200,   300]  
# ```
#
# <br>
#
# créons maintenant un tableau avec des éléments de type *entier signé sur 8 bits* (1 octet)
#     
# ```python
# l = [-1, 2, 3]
# mat = np.array(l, np.int8)
# mat
#     -> [-1, 2, 3]
# ```
# <br>
#     
# multiplions les éléments du tableau `mat` par $100$
#     
# <br>
#     
#      
# ```python
# mat*100
# -> [-100,  -56,   44]  
# ```
#     
# **et non pas** `[-100,  200,  300]`
#     
# <br>
#     
# le problème ?
#
# * `numpy` ne modifie jamais la taille (le type) des éléments d'un tableau existant
# * il calcule donc à taille-mémoire constante 
# * et convertit au-besoin les valeurs
#
#     
# <br>
#
# pour éviter tout problème restez sur le type inféré par `numpy`  
# vos entiers seront le plus souvent des `numpy.int64` ou des `numpy.int32`

# %%
# le code
l = [-1, 2, 3]
mat = np.array(l)
print(    mat    )
print(    mat*100    )
print(    mat.dtype    )

# %%
# le code
l = [-1, 2, 3]
mat = np.array(l, np.int8)
print(    mat    )
print(    mat*100    )

# %% [markdown] tags=["framed_cell"]
# ## autres constructeurs de  `numpy.ndarray`
# <br>
# <br>
#     
#
# | les méthodes | ce qu'elles font |
# | --------------------------- | --------------------- ---------------------- |
# | `numpy.zeros` | renvoie un ndarray rempli de *0.* (float) |
# | `numpy.ones` | renvoie un ndarray rempli de *1.* (float) |
# | `numpy.empty` | renvoie un ndarray vide i.e. sans initialiser ses éléments |
#     | | |
# | `numpy.arange` | tableau de valeurs régulièrement espacées|
# | `numpy.linspace` |  tableau de valeurs régulièrement espacées|
#     | | |
# | `numpy.random.randint` | entiers aléatoirement générés |
# | `numpy.random.randn` | flottants aléatoirement générés |

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### tableau de zéros `numpy.zeros`
# <br>
# <br>
#     
# voud devez indiquer à la fonction `numpy.zeros` la forme du tableau
#     
#     
# ```python
# zorro = np.zeros(shape=(4, 5))
# zorro
# -> [[0., 0., 0., 0., 0.],
#     [0., 0., 0., 0., 0.],
#     [0., 0., 0., 0., 0.],
#     [0., 0., 0., 0., 0.]]
# ```
#     
# <br>
#     
# on peut donner d'autres paramètres, comme le type des éléments...
#     
# ```python
# zorro1 = np.zeros(shape=(4, 5), dtype=np.uint64)
# zorro1
# -> [[0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ```

# %%
# le code
zorro = np.zeros(shape=(4, 5))
zorro

# %%
# le second code
zorro1 = np.zeros(shape=(4, 5), dtype=np.uint64)
zorro1

# %% [markdown] tags=["level_basic"]
# **exercice**
#
#
# * affichez le type des éléments de `zorro`
#
#
# * créez le tableau multi-dimensionnel des entiers positifs 8 bits suivant
#
# ```python
# array([[[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]],
#
#        [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]])
# ```

# %%
# votre code ici

# %% [markdown] tags=["framed_cell"]
# ### tableau non-initialisé `numpy.empty`
# <br>
#     
# la fonction `numpy.empty`
#     
# <br>
#     
# **utilité ?**
#
# * ne pas perdre de temps à initialiser inutilement un tableau
# * quand vous n'allez jamais utiliser la valeur initiale des éléments

# %% [markdown]
# **exercice**
#
# 1. créez un tableau de forme `(3, 5)` de valeurs non-initialisées  
# de type entiers signés sur 8 bits
# 1. affichez-le
# 1. que contient-il ?

# %%
# votre code ici

# %% [markdown] tags=["framed_cell"]
# ### tableau de valeurs régulièrement espacées
# <br>
# <br>
#
# `numpy.arange(from, to, step)`
#
# * nombres équidistants de `step` sur l'intervalle `[from, to[`  
# * n'utilisez pas un incrément (step) non entier
#     
#     
#     
# <br>
#     
#     
# `numpy.linspace(from-included, to-included, n)`
#
# * `n` réels régulièrement espacés dans un intervalle
# * la valeur supérieure de l'intervalle **est** incluse

# %% [markdown]
# exemple un sinus

# %%
from matplotlib import pyplot as plt

X = np.linspace(-np.pi, np.pi, 30)
Y = np.sin(X)
plt.plot(X, Y)

# %% [markdown]
# **astuce**
#
# pour éviter de voir apparaitre la ligne avec le vilain `[<matplotlib.lines.Line2D at 0x...>]`, on ajoute habituellement un `;` à la fin de la dernière ligne de la cellule

# %%
# pour éviter l'affichage superflu, ajoutez un ;
plt.plot(X, Y);

# %% [markdown]
# ## tableaux de valeurs aléatoires

# %% [markdown] tags=["framed_cell"]
# ### générateur de valeurs aléatoires entières
#
# <br>
# <br>
#     
# `numpy.random.randint` permet de tirer un nombre entier aléatoirement entre deux bornes  
# (la seconde est exclue)
# ```python
# borne_inf = 10
# borne_sup = 20
# np.random.randint(borne_inf, borne_sup)
# ```
#
# <br>    
#  
# passez lui le paramètre `size` (et non pas `shape`)
# pour générer un tableau-multi-dimensionnel d'une forme donnée 
#
# ```python
# np.random.randint(10, 20, size=(2, 3, 5))
# -> 
# array([[[11, 18, 14, 19, 16],
#         [17, 14, 15, 11, 11],
#         [13, 17, 11, 10, 13]],
#
#        [[12, 14, 10, 13, 17],
#         [11, 17, 18, 19, 18],
#         [19, 15, 10, 17, 18]]])
# ```

# %%
# le code
borne_inf = 10
borne_sup = 20
np.random.randint(borne_inf, borne_sup)

# %%
# le code
np.random.randint(10, 20, size=(2, 3, 5))

# %% [markdown] tags=["framed_cell"]
# ### générateur de valeurs aléatoires réelles
#
# <br>
#     
# `numpy.random.randn` renvoie un échantillon  
# de la loi normale centrée-réduite (moyenne 0, écart-type 1)
#
# ```python
# np.random.randn()
# -> 0.19176811586596798
# ```
#     
# <br>
#     
# `numpy.random.randn(d0, ..., dn)` génére un tableau de `shape` $(d_1, ..., d_n)$
#
# ```python
# np.random.randn(2, 3, 1)
# ->
# array([[[-0.91543618],
#         [-2.12493972],
#         [ 0.93155056]],
#
#        [[-0.17198904],
#         [-0.69164236],
#         [-0.43321452]]])
# ```
#
# <br>
#
# la librairie `numpy.random`
#
# * contient plus de fonctionnalités pour le calcul scientifiques que `random.random`  
# * sait manipuler efficacement des tableaux `numpy.ndarray`

# %%
# le code
np.random.rand()

# %%
# le code
np.random.randn(2, 3, 1)

# %% [markdown]
# **exercice** génération aléatoire et affichage *couleur*
#
#
# avec la fonction `numpy.random.randint` 
# dont l'aide est obtenu en tapant
# ```python
# np.random.randint?
# ```
#
# 1. construisez une image de $10 \times 10$ pixels en format RBG  
# i.e. chaque pixel est composé de 3 valeurs entières entre 0 et 255 inclus
#
#
# 2. affichez l'image avec `plt.imshow`

# %%
# votre code ici

# %% [markdown] tags=["level_intermediate", "framed_cell"]
# ## comparaison des temps de création tableaux - avancé
# <br>
# <br>
#
# `%timeit` permet d'évaluer le temps d'exécution d'une ligne de code  
# `%%timeit` permet d'évaluer le temps d'exécution d'une cellule de code  
#
# <br>
#     
# ```python
# %timeit 1 + 1
# -> 8.16 ns ± 0.124 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
# ```
# la moyenne et l'écart-type des temps d'exécution de l'instruction `1 + 1` ont été calculés  
# (cela a été fait 7 fois et le meilleur résultat a été pris, voir le help)
#     
# <br>
#
# * avec `-n` vous pouvez baisser le nombre de calculs, ce sera donc moins précis
#     
# ```python
# %timeit -n 10000 1 + 1
# -> 12.5 ns ± 3.4 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# ```    
#     
# <br>
#
# `ns` = nano-seconde
#     
# <br>
#     
# calcul du temps d'exécution d'une cellule
#
# ```python
# %%timeit
# a = 1
# a + 1
# ```

# %% tags=["level_intermediate"]
# le code
# %timeit 1 + 1

# %%
# le code
# %timeit -n 10000 1 + 1

# %% tags=["level_intermediate"]
# %%timeit
a = 1
a + 1

# %% [markdown] tags=["level_intermediate"]
# **exercice** 
#
# comparez les temps d'exécution de
#
# * la création d'un `numpy.ndarray` à partir d'une liste Python comportant 10.000 floats initialisés à 0  
# ne pas mettre la création de la liste Python dans le calcul du temps
# <br>
#
# * la création d'un `numpy.ndarray` de 10.000 éléments initialisés à 0
# <br>
#
# * la création d'un `numpy.ndarray` de 10.000 éléments non-initialisés
# <br>
#
# * lequel est le plus rapide ?

# %% tags=["level_intermediate"]
# votre code ici
