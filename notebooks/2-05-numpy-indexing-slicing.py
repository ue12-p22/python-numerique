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
#     title: indexation et *slicing*
#   notebookname: indexation & slicing
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %%
import numpy as np
from matplotlib import pyplot as plt

# %% [markdown]
# # indexation et *slicing*

# %% [markdown]
# ## contenu de ce notebook (sauter si déjà acquis)
#
#
# ce notebook détaille les manières d'accéder à des éléments et de slicer des tableaux `numpy`
#
# <br>
#
# les slices sont des vues et non des copies
#
# <br>
#
# la notion de `numpy.ndarray.base`
#
# <br>
#
# voir les `exercices avancés pour les rapides`

# %% [markdown] {"tags": ["framed_cell"]}
# ## accès aux éléments d'un tableau    
#
# <br>
#
#
# *accéder à des éléments ou à des sous-tableaux  
# va nous permettre de leur appliquer des fonctions vectorisées*
#     
#     
# <br>
#     
# la manière d'accéder aux éléments d'un tableau `numpy`  
# dépend de la forme du tableau (`shape`)
#     
#    
# <br>
#
# la forme d'un `numpy.ndarray` est donnée par une indexation  
# sur le segment mémoire sous-jacent continu de votre tableau
#
# <br>
#     
# par exemple  
# un `numpy.ndarray` de $12$ éléments 
#
# <div class="memory">
#
# ```
# ☐☐☐☐☐☐☐☐☐☐☐☐
# ```
#
# </div>
#     
# peut être indexé sous différentes dimensions et formes
#
# * dimension 1, par exemple $(12,)$
# * dimension 2, par exemple $(1, 12)$ $(6, 2)$ $(3, 4)$ $(4, 3)$
# * dimension 3, par exemple $(2, 3, 2)$...

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell"]}
# ### accès à un tableau de dimension 1
#
# <br>
#
# vous avez besoin d'**un seul index**
#     
# <br>
#
# ```python
# tab = np.arange(12)
# tab[0] = np.pi
# ```
# <br>
#
#     
# Quelle est le type de `tab[0]` ?  
# Quelle est la valeur de `tab[0]` ?    
#
# rappelez-vous
#
# * les éléments d'un tableaux `numpy` sont typés et leur taille est fixe
#
# <br>
#
# pour mettre des réels dans un tableau  
# il faut que le type des éléments corresponde
#
# ```python
# tab1 = tab.astype(np.float64)
# tab1[0] = np.pi # 3.141592653589793
# ```

# %% {"scrolled": true}
# le code
tab = np.arange(12)
tab[0] = np.pi
tab[0].dtype, tab[0]

# %%
# le code
tab1 = tab.astype(np.float64)
tab1[0] = np.pi
tab1[0].dtype, tab1[0]

# %% [markdown] {"tags": ["framed_cell"]}
# ### accès à un tableau de dimension > à 1
# <br>
#
# l'accès à un élément du tableau dépend de la forme du tableau  
#
# <br>
#     
# il y aura un indice par dimension
#     
# <br>
#   
# en dimension 2    
# ```python
# tab = np.arange(12).reshape((2, 6))
#     
# # première ligne, deuxième colonne
#     line, col = 0, 1
#     tab[line, col] = 1000
#     
# tab
# -> array([[ 0, 1000,  2,  3,  4,  5],
#           [ 6,    7,  8,  9, 10, 11]])
# ```
#     
# <br>
#         
#
# en dimension 3      
# ```python
# tab.resize((2, 3, 2))
#
# # deuxième matrice, troisième ligne, première colonne
#     
# mat, line, col = 1, 2, 0
# tab[mat, line, col] = 2000
# tab
# -> array([[[   0, 10],
#            [   2,  3],
#            [   4,  5]],
#
#           [[   6,  7],
#            [   8,  9],
#            [2000, 11]]])
# ```
#     
# <br>
#
# nombre d'éléments dans chaque dimension
# ```python
# [tab.shape[i] for i in range(tab.ndim)]
# -> [2, 3, 2]
# ```
#     
# <br>
#     
# remarque  en dimension $\ge2$  
# les deux dernières dimensions sont les lignes et les colonnes
#
# * ainsi le nombre de lignes c'est `tab.shape[-2]`
# * et de colonne`tab.shape[-1]`

# %%
# le code
tab = np.arange(12).reshape((2, 6))
    
# première ligne, deuxième colonne
line, col = 0, 1
tab[line, col] = 1000
tab

# %%
# le code
tab.resize((2, 3, 2))

# deuxième matrice, troisième ligne, première colonne
    
mat, line, col = 1, 2, 0
tab[mat, line, col] = 2000
tab

# %% [markdown]
# ### exercices

# %% [markdown]
# **accès à un élément**  
# 1. créez un tableau des 30 valeurs paires à partir de 2
#
#
# 2. donnez lui la forme de 2 matrices de 5 lignes et 3 colonnes
#
#
# 3. accédez à l'élément qui est à la 3ème colonne de la 2ème ligne de la 1ère matrice
#
#
# 4. obtenez-vous 12 ?

# %%
# votre code

# %% [markdown] {"cell_style": "center"}
# **exercice**
#
# 1. faites un `np.ndarray` de forme $(3, 2, 5, 4)$  
#    avec des nombre aéatoires entiers entre 0 et 100
#    
#    
# 2. affichez-le et
#    vous voyez trois groupes et 2 matrices de 5 lignes et 4 colonnes
#
#
#
# 3. affichez le nombre des éléments des deux dernières dimensions
#
#
# indice   
#
# * utilisez `numpy.random.randint`
# * son `help` vous dira comment passer la forme au tableau à sa création  
# (celui de `np.random.randint` selon la manière d'importation de `numpy` )

# %%
# votre code ici

# %% [markdown]
# ## accéder à un sous-tableau (slicing)

# %% [markdown] {"tags": ["framed_cell"]}
# ### différence slicing `python` et `numpy`
#
# <br>
#     
#
# le **slicing** `numpy` est *syntaxiquement équivalent* à celui des listes `Python`
#     
# <br>
#     
# la **grande** différence est que
#
# * quand vous slicez un **tableau `numpy`** vous obtenez une **vue** sur le tableau initial  
# (avec une nouvelle indexation)
#
# * quand vous slicez une **liste `python`** vous obtenez une **copie** de la liste initiale
#
#    
# <br>
#     
# le slicing `numpy` va
#
# * regrouper des éléments du tableau initial
# * dans un sous-tableau `numpy.ndarray` avec l'indexation adéquate
# * la mémoire sous-jacente reste la même
#     
# <br>
#     
# la seule structure informatique qui sera créée est l'indexation  
#     
# <br>
#     
# vous pourrez ensuite, par exemple, modifier ces éléments  
# et donc ils seront modifiés dans le tableau initial
#     
# <br>
#
#     
# <br>
#
# </div>

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell"]}
# ### rappel du slicing Python
#
# <br>
#    
# **rappel du slicing Python**
#     
#     
# * `l[from:to-excluded:step]` 
#     
#     
# * paramètres tous optionnels  
# par défaut: `from = 0` `to-excluded = len(l)`et `step=1`
#     
#     
# * indices négatifs ok `-1` est le dernier élément, `-2` l'avant dernier ...
#
# <br>
# la liste python des 10 premiers entiers
#     
# ```python
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     
# # un élément sur 2 en partant du début de la liste (copie)
# l[::2]
#     
# # un élément sur 3 en partant du premier élément de la liste (copie)
# l[1::3]
#     
# # la liste en reverse (copie)
# l[::-1]
#     
# # la liste entière (copie)
# l[::]
# # ou
# l[:]
# ```
# <br>
#
# </div>

# %%
# le code
l =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(l[::2])
print(l[1::3])
print(l[::-1])
print(l[:])

# %% [markdown] {"tags": ["framed_cell"]}
# ### slicing en dimension 1<br>
#
# on crée un `numpy.ndarray` de dimension 1 de taille 10
#     
# <br>
#     
# * on prend un élément sur 2 en partant du début de la liste  
# * on modifie les éléments du sous-tableau obtenu  
# * le tableau initial est modifié
#     
#     
#     
# ```python
# vec = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
# print(vec[::2])     # [0 2 4 6 8]
# vec[::2] = 100
# print(vec)          # [100, 1, 100, 3, 100, 5, 100, 7, 100, 9]
# ```

# %%
# le code
vec = np.arange(10)
print(vec[::2])
vec[::2] = 100
vec

# %% [markdown] {"tags": ["framed_cell"]}
# ### slicing en dimension > à 1 (a)
#
# <br>
#
# on crée un `numpy.ndarray` en dimension 4, de forme $(2, 3, 4, 5)$  
# on l'initialise avec les $120$  premiers entiers
#     
# ```python
# tab = np.arange(120).reshape(2, 3, 4, 5)
# ```
#     
# <br>
#    
# on a 2 groupes de 3 matrices de 4 lignes et 5 colonnes    
#     
# <br>
#     
# * on accède au premier groupe de matrices 
# ```python
# tab[0]
# ```
#     
# <br>
#     
# * on accède à la deuxième matrice du premier groupe de matrices
# ```python
# tab[0, 1]
# ```
#     
# <br>    
#
# * on accède à la troisième ligne de la deuxième matrice du premier groupe de matrices
#    
# ```python
# tab[0, 1, 2]
# ```
# <br>    
#
# * on accède à la quatrième colonne de la deuxième matrice du premier groupe de matrices
#    
# ```python
# tab[0, 1, :, 3] # remarquez le ':' pour indiquer toutes les lignes
# ```
#
#     
# </div>

# %%
# le code
tab = np.arange(120).reshape(2, 3, 4, 5)
print(    tab    )
print(    tab[0]    )
print(    tab[0, 1]    )
print(    tab[0, 1, 2]    )
print(    tab[0, 1, :, 3]    )

# %% [markdown] {"tags": ["framed_cell"]}
# ### slicing en dimension > à 1 (b)
# <br>
#
# on crée un `numpy.ndarray` en dimension 4, de forme $(2, 3, 4, 5)$  
# on l'initialise avec les $120$  premiers entiers
#     
# ```python
# tab = np.arange(120).reshape(2, 3, 4, 5)
# ```
#   
# <br>
#     
# on peut combiner les slicing des 4 dimensions, ici  
# `tab[from:to:step, from:to:step, from:to:step, from:to_step]`  
# <br>
#
# de l'indice `from` à l'indice `to` (exclus) avec un pas `step`  
#
# <br>
#     
# à savoir    
#
# * quand vous voulez la valeur par défaut de `from`, `to` et `step` vous ne mettez rien
# * quand les valeurs par défaut sont en fin d'expression, elles sont optionnelles
# * `::` devient `:`
#     
# <br>
#     
# **exemples**
#     
# la première matrice de tous les groupes de matrice
# ```python
# tab[::, 0, ::, ::]
# ```
# tous les groupes  
# la première matrice  
# toutes les lignes  
# toutes les colonnes
#     
# <br>
#     
# qui s'écrit aussi
# ```python
# tab[:, 0, :, :]
# tab[:, 0] # ou encore, plus simplement
# ```    
# </div>

# %%
tab = np.arange(120).reshape(2, 3, 4, 5)
tab[:, 0]

# %% [markdown]
# **exercices**
#
# 1. extrayez du tableau `tab` précédent  
# ```python
# tab = np.arange(120).reshape(2, 3, 4, 5)
# ```
#
# la sous-matrice du milieu (garder deux lignes et 3 colonnes, au centre) des premières matrices de tous les groupes
#
# $\begin{bmatrix}\begin{bmatrix} 6 & 7 & 8\\ 11 & 12 & 13 \end{bmatrix}, \begin{bmatrix} 66 & 67 & 68 \\ 71 & 72 & 73 \end{bmatrix}\end{bmatrix}$  
# <br>
#
# **indices**  
# on a 2 groupes de 3 matrices de 4 lignes et 5 colonnes
#
# donc
#
# * pour les 2 groupes de matrices
# * dans la première matrice
# * la sous-matrice du milieu
# (obtenue en enlevant une épaisseur de largeur 1 sur le pourtour)  
#
# donc
#
# * tous les groupes `:`
# * la première matrice (indice `0`)
# * de la première ligne (indice `1`) à l'avant dernière ligne (indice `-1`) step par défaut
# * idem pour les colonnes

# %%
# votre code

# %% [markdown] {"tags": ["framed_cell"]}
# ## les sous-tableaux sont des vues, et non des copies
#
# <br>
#
# le slicing calcule une nouvelle indexation sur le segment mémoire du tableau existant
#
#
# <br>
#     
# si à chaque slicing, `numpy` faisait une copie du tableau sous-jacent, les codes seraient inutilisables  
# parce que coûteux (pénalisés) en place mémoire
#     
#   
# <br>
#     
# **donc lors d'un slicing**
#
# * un nouvel objet `np.ndarray` est bien créé,
# * son indexation est différente de celle de l'objet `np.ndarray` initial
# * mais ils **partagent** la mémoire (le segment unidimensionnel sous-jacent)
#     
#     <br>
#     
# si un utilisateur veut une copie, il la fait avec la méthode `copy`
#
# ```python
# tab1 = tab[:, 0, 1:-1, 1:-1].copy()
# ```

# %% [markdown]
# ***

# %% [markdown] {"tags": ["framed_cell", "level_intermediate"]}
# ## partage du segment sous-jacent ou non? - avancé    
#
# <br>
#
# un tableau `numpy.ndarray` peut être
# 1. un tableau *original* (on vient de le créer éventuellement par copie)
# 1. une vue sur un tableau (il a été créé par slicing ou indexation)  
#   il partage son segment de mémoire avec au moins un autre tableau
#     
# <br>
#     
#     
# l'attribut `numpy.ndarray.base` vaut alors
#     
#     
# 1. `None` si le tableau est un tableau original
#
# ```python
# tab = np.arange(10)
# print(tab.base)
# -> None
# ```
#     
#     
# ```python
# tab1 = np.arange(10)
# tab2 = tab1.copy()
# print(tab2.base)
# -> None
# ```
#     
# 2. **le tableau original qui a servi à créer la vue**  
#     quand le tableau est une vue  
#   
#
#
# ```python
# tab1 = np.array([[1, 2, 3], [4, 5, 6]])
# tab2 = tab1[0:2, 0:2] # une vue
# tab2.base is tab1
# -> True
# ```
#     
# ```python  
# tab1 = np.arange(120)
# tab2 = tab1.reshape(2, 3, 4, 5) # une vue
# tab2.base is tab1
# -> True
# ```      
#
# <br>
#  
# faites attention, dans l'exemple
#
# ```python
# tab1 = np.arange(10).reshape(2, 5)
# ```
#     
# `tab1.base` est l'objet `np.arange(10)`  
#     
# <br>
# <br>
#     
#     
# les `numpy.ndarray` ayant le même objet `numpy.ndarray.base`
#
# * partagent tous leur segment sous-jacent
# * sont différentes vues d'un même tableau original  
# (celui indiqué par leur attribut `base`)
#
# * modifier les éléments de l'un modifiera les éléments des autres  
# (ils *pointent tous* sur le même segment de mémoire)
#     
# <br>
#     
# `numpy` essaie de créer le moins de mémoire possible  
# pour stocker les éléments de ses tableaux

# %%
# le code
tab1 = np.arange(10)
print(tab1.base)

# %%
# le code
tab1 = np.arange(10)
tab2 = tab1.copy()
print(tab2.base)

# %%
# le code
tab1 = np.array([[1, 2, 3], [4, 5, 6]])
tab2 = tab1[0:2, 0:2] # vue
tab2.base is tab1

# %%
# le code
tab1 = np.arange(120)
tab2 = tab1.reshape(2, 3, 4, 5) # une vue
tab2.base is tab1

# %%
# le code
tab1 = np.arange(10).reshape(2, 5)
tab1.base

# %% [markdown]
# **exercice**
#
#
# 1. créez un nouveau tableau formé des deux matrices $[\begin{pmatrix} 2 & 4 & 6\\ 8 & 10 & 12 \end{pmatrix}, \begin{pmatrix} 14 & 16 & 18 \\ 20 & 22 & 24 \end{pmatrix}]$.  
# <br>
#
# 1. affichez sa `base`
# <br>
#
# 1. *slicez* le tableau pour obtenir $[\begin{pmatrix} 24 & 22 & 20 \\ 18 & 16 & 14 \\ \end{pmatrix}, \begin{pmatrix} 12 & 10 & 8 \\ 6 & 4 & 2\end{pmatrix}] $
# <br>
#
# 1. affichez la `base` de la slice
# <br>
#
# 1. vérifiez que les deux `base` sont le même objet

# %%
# votre code ici

# %% [markdown] {"tags": ["framed_cell"]}
# ## modification des sous-tableaux
#
# <br>
#     
# pour modifier un sous-tableau, il faut simplement faire attention 
# 1. au type des éléments  
# 2. et à la forme du tableau

# %% [markdown]
# ## exercices avancés pour les rapides

# %% [markdown]
# avant d'aborder ces exercices, il existe un utilitaire très pratique (parmi les 2347 que nous n'avons pas eu le temps de couvrir ;); il s'agit de `numpy.indices()`
#
# commençons par un exemple :

# %%
lignes, colonnes = np.indices((3, 5))

# %% {"cell_style": "split"}
lignes

# %% {"cell_style": "split"}
colonnes

# %% [markdown]
# vous remarquerez que dans le tableau qui s'appelle `lignes`, la valeur dans le tableau correspond au numéro de ligne; dit autrement :
#
# * `lignes[i, j] == i` pour tous les $(i, j)$,
#     
# et dans l'autre sens bien sûr 
#
# * `colonnes[i, j] == j`

# %% {"cell_style": "split"}
lignes[1, 4]

# %% {"cell_style": "split"}
colonnes[1, 4]

# %% [markdown]
# Pourquoi est-ce qu'on parle de ça me direz-vous ? 
#
# Eh bien en guise d'indice, cela vous renvoie à la notion de programmation vectorielle.
#
# Ainsi par exemple si je veux créer une matrice de taille (3,5) dans laquelle `M[i, j] == i + j`, je **ne vais surtout par écrire une boucle `for`**, et au contraire je vais écrire simplement

# %%
I, J = np.indices((3, 5))
M = I + J
M


# %% [markdown]
# ### les rayures

# %% [markdown]
# Écrivez une fonction `zebre`, qui prend en argument un entier *n* et qui fabrique un tableau carré de coté $n$, formé d'une alternance de colonnes de 0 et de colonnes de 1.

# %% [markdown]
# par exemple pour $n=4$ on s'attend à ceci
#
# ```console
# 0 1 0 1 
# 0 1 0 1 
# 0 1 0 1 
# 0 1 0 1 
# ```

# %% [markdown]
# ### le damier
#
# Écrivez une fonction *checkers*, qui prend en argument la taille *n* du damier, et un paramètre optionnel qui indique la valeur de la case (0, 0), et qui crée un tableau `numpy` carré de coté $n$, et le remplit avec des 0 et 1 comme un damier (0 pour les cases noires et 1 pour les cases blanches).
#
#
# https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x1-checkers

# %% [markdown] {"tags": ["level_advanced"]}
# ### le damier (variante)

# %% [markdown] {"tags": ["level_advanced"]}
# Il y a beaucoup de méthodes pour faire cet exercice de damier; elles ne vont pas toutes se généraliser pour la variante :
#
# **Variante** écrivez une fonction `super_checkers` qui crée 
#
# * un damier de coté $k.n \times k.n$ 
# * composé de blocs de $k\times k$ homogènes (tous à 0 ou tous à 1)
# * eux mêmes en damiers
# * on décide que le premier bloc (en 0,0) vaut 0
#
# c'est-à-dire par exemple pour $n=4$ et $k=3$ cela donnerait ceci :
#
# ```
# 0 0 0 1 1 1 0 0 0 1 1 1 
# 0 0 0 1 1 1 0 0 0 1 1 1 
# 0 0 0 1 1 1 0 0 0 1 1 1 
# 1 1 1 0 0 0 1 1 1 0 0 0 
# 1 1 1 0 0 0 1 1 1 0 0 0 
# 1 1 1 0 0 0 1 1 1 0 0 0 
# 0 0 0 1 1 1 0 0 0 1 1 1 
# 0 0 0 1 1 1 0 0 0 1 1 1 
# 0 0 0 1 1 1 0 0 0 1 1 1 
# 1 1 1 0 0 0 1 1 1 0 0 0 
# 1 1 1 0 0 0 1 1 1 0 0 0 
# 1 1 1 0 0 0 1 1 1 0 0 0 
# ```

# %% {"tags": ["level_advanced"]}
def super_checkers(n, k):
    ...


# %% {"tags": ["level_advanced"]}
# doit vous donner la figure ci-dessus
# éventuellement avec des False/True au lieu de 0/1
super_checkers(4, 3)


# %% [markdown]
# ### les escaliers

# %% [markdown]
# Écrivez une fonction *escalier*, qui prend en argument un entier *n*, qui crée un tableau de taille *2n+1*, et qui le remplit de manière à ce que:
#    - aux quatre coins du tableau on trouve la valeur *0*
#    - dans la case centrale on trouve la valeur *2n*
#    - et si vous partez de n'importe quelle case  et que vous vous déplacez d'une case (horizontalement ou verticalement), en vous dirigeant vers une case plus proche du centre, la valeur que vous trouvez est *1* de plus que la valeur de la case où vous étiez.

# %% [markdown]
# https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x3-stairs

# %% [markdown] {"tags": ["level_advanced"]}
# ### calculs imbriqués (avancé)

# %% [markdown] {"tags": ["level_advanced"]}
# Regardez le code suivant :

# %% {"tags": ["level_advanced"]}
# une fonction vectorisée
def pipeline(array):
    array2a = np.sin(array)
    array2b = np.cos(array)
    array3 = np.exp(array2a + array2b)
    array4 = np.log(array3+1)
    return array4

# %% [markdown] {"tags": ["level_advanced"]}
# Les questions : j'ai un tableau `X` typé `float64` et de forme `(1000,)`
#
# * j'appelle `pipeline(X)`, combien de mémoire est-ce que `pipeline` va devoir allouer pour faire son travail ?
# * quel serait le minimum de mémoire dont on a besoin pour faire cette opération ?
# * voyez-vous un moyen d'optimiser `pipeline` pour atteindre ce minimum ?

# %% [markdown] {"tags": ["level_advanced"]}
# **indice**
#
# * l'exercice vous invite à réfléchir à l'utilisation du paramètre `out=` qui est supporté dans les fonction vectorisées de numpy
# * dans ce cadre, sachez qu'on peut presque toujours remplacer l'usage d'un opérateur (comme ici `+`) par une fonction vectorisée (ici `np.add`)

