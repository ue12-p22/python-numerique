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
#     title: tests et masques sur tableaux
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")

# %% [markdown]
# # tests et masques sur tableaux

# %%
import numpy as np

# %% [markdown]
# ## contenu de ce notebook (sauter si déjà acquis)
#
# <br>
#
# tests sur les tableaux multi-dimensionnels `numpy` par fonctions vectorisées `ufunc` 
#
# <br>
#
# masques/filtres booléens
#
# <br>
#
# composition des conditions  
# opérateurs logiques *bit-à-bit* `&` `|`  `~`  
# équivalent `numpy` `np.logical_and` `np.logical_or` `np.logical_not`  
#
# <br>
#
# obtenir une vue sur les éléments du tableau initial  
# `numpy.argwhere`, `numpy.nonzero` et `numpy.putmask`

# %% [markdown] {"tags": ["framed_cell"]}
# ## tests sur tableaux multi-dimensionnels
#
# <br>
#
# l'idée est de tester en une opération **tous les éléments** d'un tableau
#
# <br>
#
# **prenons un exemple**
#
# <br>
#     
# générons aléatoirement un tableau d'entiers  
# (ici entre `0` et `9`)
#    
# ```python
# tab = np.random.randint(10, size=(2, 3))
# -> tab [[1 8 5]
#         [7 0 2]]
# ``` 
#     
# <br>
#     
# testons la parité des éléments
#     
# ```python
# tab%2 == 0
# ```
# ou encore - équivalent mais en appelant une fonction plutôt que l'opérateur `==`
#     
# ```python
# np.equal(tab%2, 0)
# ```   
# <br>
#     
# les résultats des comparaisons élément-par-élément  
# sont rangés dans un tableau `np.ndarray`  
# de même taille que le tableau initial
#    
# ```python
# tab%2 == 0
# -> [[False,  True,  False],
#     [False,  True,  True]]    
# ```
#     
# <br>
#
#        
# **remarquez**
#     
# * dans l'expression `tab%2 == 0` et `np.equal(tab % 2, 0)`
# * le broadcast de `0` en un tableau de `0` de la même taille que `tab`

# %%
# le code
tab = np.random.randint(10, size=(2, 3))
print(tab)
print(tab % 2 == 0)
print(np.equal(tab % 2, 0))
res = tab % 2 == 0
print(res.shape)

# %% [markdown] {"tags": ["framed_cell"]}
# ## n'utilisez pas de for-python: utilisez les `ufunc`
#
# <br>
#         
# les opérations de comparaison s'appliquent à tous les éléments d'un tableau en une seule fois  
#
# * il ne faut **jamais** utiliser de **for-python**
# * les fonctions sont vectorisées (les *UFuncs*)
#
# ```python
# type(np.greater)
# -> numpy.ufunc
# ```

# %% {"cell_style": "split"}
# > est une ufunc

# on peut écrire indifféremment
tab > 5

# %% {"cell_style": "split"}
# ou bien
np.greater(tab, 5)

# %% [markdown] {"tags": ["framed_cell"]}
# ## combiner les résultats
#
# <br>
#     
#     
# **les résultats** peuvent être combinés
#
# * en un résultat **global**
# * en des **sous-tableaux** de résultats
#     
# <br>
#     
# un tableau
# ```python
# tab = np.random.randint(10, size=(2, 3))
# -> tab [[1 8 5]
#         [7 0 2]]
# ``` 
# <br>
#     
# regardons si il existe au moins une valeur paire dans le tableau des résultats
#     
# ```python
# res = np.equal(tab%2, 0)    
# np.any(res)
# -> True
# ```     
#
#      
# <br>
#     
# regardons si toutes les valeurs sont paires
#     
# ```python
# res = np.equal(tab%2, 0)    
# np.all(res)
# -> False
# ```     
#
# <br>
#     
# comptons le nombre global de valeurs paires
#    
# ```python
# res = tab%2 == 0    
# print(np.sum(res))
# -> 3
# ```     
#
# il existe une fonction dédiée  
# (elle compte le nombre d'éléments non nuls)  
# ```python
# np.count_nonzero(tab%2==0)
# -> 3
# ```
#     
# <br>
#     
#
# comptons le nombre de valeurs paires dans l'axe des lignes du tableau
#     
# ```python
# res = tab %2 == 0    
# print(np.sum(res, axis=0)) # axe des lignes
# -> [0, 2, 1]
# ```  
#
# avec la fonction dédiée  
# (elle compte sur les axes)  
# ```python
# np.count_nonzero(tab%2==0, axis=0)
# -> [0, 2, 1]
# ```

# %% {"scrolled": false}
# le code
tab = np.random.randint(10, size=(2, 3))
res = np.equal(tab%2, 0)
print(np.any(res))
print(np.all(res))
print(np.sum(res))
print(np.count_nonzero(tab%2==0))
print(np.sum(res, axis=0))
np.count_nonzero(tab%2==0, axis=0)

# %% [markdown] {"tags": ["framed_cell"]}
# ## les masques/filtres booléens
#
# <br>
#     
# le tableau des résultats des tests est un **masque booléen**  
#
# * il a la **même forme** que le tableau initial
# * il va servir de **filtre** sur le tableau initial
#     
# <br>
#     
# il va permettre de sélectionner dans le tableau initial  
# les éléments pour lesquels le test est vrai
#     
# <br>
#     
# générons un `numpy.ndarray` de forme `(2, 3, 4)` d'entiers entre -10 et 10
#
# ```python
# tab = np.random.randint(-10, 10, size=(2, 3, 4))
# ```
#
# <br>
#
#
# * filtrons les entiers strictement positifs
# ```python
# tab[tab > 0]
# ```
#
# * ou encore
# ```python
# tab[np.greater(tab, 0)]
# ``` 
#    
# <br>
#
# on peut modifier tous les éléments filtrés d'un seul coup  
# lors de l'application du filtre
#
# ```python
# tab[tab > 0] = 0
# tab # n'a plus que des éléments négatifs ou nuls
# ```
#
# <br>
#
# on peut aussi construire les indices des éléments sélectionnés  
# pour les repérer dans le tableau original

# %%
# le code
tab = np.random.randint(-10, 10, size=(2, 3, 4))
tab

# %% {"scrolled": true}
print(tab[np.greater(tab, 0)])
print(tab[tab > 0])

# %%
# le code
tab [tab > 0] = 0
tab

# %% [markdown] {"tags": ["framed_cell"]}
# ## composition des conditions
#
# <br>
#     
# 4 règles
#
# * vous ne pouvez **pas** utiliser les opérateurs logiques Python `and`, `or`, `not`  
#   (ils ne sont **pas** vectorisés)
#
# * vous devez utiliser les opérateurs logiques *bit-à-bit* `&` `|`  `~`
# * ou leur équivalent en fonction `numpy`  
#   `np.logical_and` `np.logical_or` `np.logical_not`  
#   (qui sont binaires)
#
# * vous devez parenthéser les sous-termes de vos expressions
#     
# <br>
#     
# on crée un tableau d'entiers aléatoires entre 0 et 100
#     
# ```python
# tab = np.random.randint(100, size=(3, 4))
# ```
#             
# <br>
#     
# masque pour sélectionner les éléments entre 25 et 75 
#     
# ```python
# (tab >= 25) & (tab < 75)
# ```
#                             
# <br>
#     
# masque pour sélectionner les éléments non-pairs entre 25 et 75
#     
#     
# ```python
# (tab >= 25) & (tab < 75) & ~(tab%2==0)
# ```
#     
# <br>
#     
# et donc en version `numpy`
#     
# ```python
# np.logical_and(tab >= 25, tab < 75)
# ```    
#     
# ```python
# np.logical_and(tab >= 25, np.logical_and(tab < 75, np.logical_not(tab%2==0)))
# ```

# %%
# le code
tab = np.random.randint(100, size=(3, 4))
print(tab)
print((tab >= 25) & (tab < 75))
print((tab >= 25) & (tab < 75) & ~(tab%2==0))

# %%
# le code
print(np.logical_and(tab >= 25, tab < 75))
print(np.logical_and(tab >= 25, np.logical_and(tab < 75, np.logical_not(tab%2==0))))

# %% {"tags": ["level_intermediate"]}
# ATTENTION
# en Python pur on a le droit d'écrire un test comme
# 25 <= tab < 75
# MAIS comme ça va implicitement faire un 'and'
# ça ne fonctionne pas avec les tableaux numpy
try:
    25 <= tab < 75
except Exception as exc:
    print("OOPS - ne marche pas avec numpy\n", exc)

# %% [markdown]
# ## modifier les éléments dans tableau d'origine

# %% [markdown] {"tags": ["framed_cell"]}
# ### affecter une sélection
#
# <br>
#
# avec une expression de *sélection* de cette forme `tab[mask]`   
# on peut **aussi modifier** (ces emplacements dans) le tableau de départ  
# en affectant directement une valeur  
# remarquez que la sélection se trouve à gauche du signe `=`
#
# ```python
# tab = np.array([[1, 2, 3], [4, 5, 6]])
# tab[tab % 2 == 0] = 100
# print(tab)
# [[  1 100   3]
#  [100   5 100]]
# ```

# %%
# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
tab[tab % 2 == 0] = 100
print(tab)

# %% [markdown] {"tags": ["framed_cell", "level_intermediate"]}
# ### c'est fragile (1)
#
# <br>
#
# par contre il faut être un peu prudent; certaines formes, pourtant voisines en apparence, ne vont pas fonctionner
#
# **1er cas**
#
# maladroitement, je range la sélection dans une variable  
# la sélection ne se trouve plus à gauche du `=`  
# dans cette forme l'affectation va en fait modifier un tableau temporaire  
# bref, ça **ne fonctionne plus** !  
#
#
# ```python
# tab = np.array([[1, 2, 3], [4, 5, 6]])
# view = tab[tab%2==0]
# view[...] = 100
# print(tab) 
# -> ([[1, 2, 3], # et non [1, 100, 3],...
#      [4, 5, 6]])
# print(view)
# -> [100 100 100]
# ```    

# %% {"tags": ["level_intermediate"]}
# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
view = tab[tab%2==0]
view[...] = 100
print(tab)
print(view)

# %% [markdown] {"tags": ["framed_cell", "level_intermediate"]}
# ### c'est fragile (2)
#
# **2ème cas**
#
# imaginons que je ne veux modifier **que le premier** des éléments pair  
# je vais essayer en *indexant* ma sélection  
# mais ça **ne fonctionne pas** comme espéré  
# ici encore l'effet de bord se perd dans la nature  
# et le tableau original n'est pas modifié
#
#
# ```python
# tab = np.array([[1, 2, 3], [4, 5, 6]])
# tab[tab%2==0][0] = 100
# print(tab) 
# -> ([[1, 2, 3], # et non [1, 100, 3],...
#      [4, 5, 6]])
# ```    

# %% {"tags": ["level_intermediate"]}
# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
tab[tab%2==0][0] = 100
print(tab) 


# %% [markdown] {"tags": ["framed_cell", "level_intermediate"]}
# ### repérer les éléments par leurs indices
#
# <br>
#     
# dans ce genre de situation, pour modifier les éléments sélectionnés dans le tableau d'origine, on peut repèrer les éléments par leur indice dans le tableau d'origine
#
# <br>
#     
# et pour calculer ces indices, deux fonctions:
#
# * la fonction `numpy.nonzero`
# * la fonction `numpy.argwhere` (avancé)

# %% [markdown] {"tags": ["level_intermediate"]}
# ***

# %% [markdown] {"tags": ["framed_cell", "level_intermediate"]}
# ### la fonction `numpy.nonzero`
#
# <br>
#     
# `numpy.nonzero`
#
# * renvoie un tuple de même dimension que le tableau d'origine
# * dans chaque dimension, on a la liste des indices
#     
# <br>
#     
# exemple
#     
# ```python
# tab = np.array([[1, 2, 3], [4, 5, 6]])
# np.nonzero(~(tab%2==0))
# -> ([0, 0, 1], [0, 2, 1])
# ```
#     
# <br>
#     
# la première liste contient les indices des lignes  `[0, 0, 1]`
#     
# la seconde liste contient les indices des colonnes `[0, 2, 1]`
#     
#     
# `tab[0, 0]` `tab[0, 2]` et `tab[1, 1]` sont les 3 éléments
#   
# ```python
# print(tab[0, 0], tab[0, 2], tab[1, 1])
# -> 1, 3, 5
# ```
#     
# <br>   
#
# la **magie**: vous pouvez indicer le tableau d'origine avec ce tuple  
# pour obtenir une vue sur le tableau d'origine
#     
#  
# ```python
# tab[np.nonzero(~(tab%2==0))]
# -> 1, 3, 5
# ```
#    
# <br>
#     
# et donc vous pouvez modifier les éléments du tableau original    
#  
# ```python
# tab[np.nonzero(~(tab%2==0))] = 1000
# tab
# -> [[1000,    2, 1000],
#     [   4, 1000,    6]]
# ```

# %% {"tags": ["level_intermediate"]}
tab = np.array([[1, 2, 3], [4, 5, 6]])
print("non zero", np.nonzero(~(tab%2==0)))
print("elements", tab[0, 0], tab[0, 2], tab[1, 1])
print("filter", tab[np.nonzero(~(tab%2==0))])
tab[np.nonzero(~(tab%2==0))] = 0
print("edited tab", tab)

# %% [markdown] {"tags": ["framed_cell", "level_intermediate"]}
# ###  la fonction `numpy.argwhere`
#
# <br>
#     
# `numpy.argwhere`
#
# * renvoie un tableau de dimension 2
# * autant de lignes que d'éléments filtrés
# * chaque ligne donne l'index d'un élément  
# dans chacune des dimensions du tableau d'origine
#     
#     
# <br>
#     
# exemple
#     
# ```python
# tab = np.array([[1, 2, 3], [4, 5, 6]])
# np.argwhere(~(tab%2==0))
# -> [[0, 0],
#     [0, 2],
#     [1, 1]]
# ```
#     
# <br>
#     
# la première ligne contient les indices du premier élément  `[0, 0]`
#     
# la seconde ligne contient les indices du second élément `[0, 2]`
#     
# la troisième ligne contient les indices du troisième élément `[1, 1]`
#     
#     
# <br>   
#
# vous ne pouvez **pas**  indicer directement le tableau d'origine par ce tableau  
# et non on ne fait pas de `for-python`
#
#   
# <br>
#     
# on remarque
#
# * que les résultats de `numpy.nonzero` et  `numpy.argwhere` sont très proches
# * à une transposée et un type `tuple` près
#     
# ```python
# cond = ~(tab%2==0)
# np.nonzero(cond)            # ([0, 0, 1], [0, 2, 1])
# np.argwhere(cond)           # [[0 0] [0 2] [1 1]]
# np.argwhere(cond).T         # [[0 0 1] [0 2 1]]
# tuple(np.argwhere(cond).T)  # ([0, 0, 1], [0, 2, 1])
# tab[tuple(np.argwhere(cond).T)]    
# -> array([1, 3, 5])
# ```

# %% {"tags": ["level_intermediate"]}
# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
cond = ~(tab%2==0)
print(np.argwhere(cond).T)
print(np.nonzero(cond))
print(tuple(np.argwhere(cond).T))
tab[tuple(np.argwhere(cond).T)]

# %% [markdown] {"tags": ["framed_cell", "level_advanced"]}
# ### modifier avec `array.putmask()`
#
# **avancés**
#
# <br>
#     
# la fonction `numpy.putmask(tab, cond, value)` remplace dans un `numpy.ndarray`  
# les éléments obéissant à une condition, par une valeur donnée en argument
#     
# <br>
#     
# la modification est effectuée dans le tableau (en place)
#     
# <br>
#     
# ```python
# tab = np.arange(12).reshape(3, 4)
# np.putmask(tab, tab%2==1, 0)
# tab -> ([[ 0,  0,  2,  0],
#         [ 4,  0,  6,  0],
#         [ 8,  0, 10,  0]])
# ```

# %% {"tags": ["level_advanced"]}
# le code
tab = np.arange(12).reshape(3, 4)
np.putmask(tab, tab%2==1, 0)
tab
