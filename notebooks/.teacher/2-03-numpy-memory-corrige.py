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
#     title: "la m\xE9moire"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %% [markdown]
# # la mémoire

# %% [markdown]
# ## contenu de ce notebook (sauter si déjà acquis)
#
# <br>
#
# avoir une intuition de ce qui se passe dans en mémoire pour un `numpy.ndarray`  
#
# <br>
#
# > *An array object represents a multidimensional, **homogeneous** array of **fixed-size** items.*
#
# <br>
#
# * indirection versus décalage (*offset*)
# * indiçage des tableaux `numpy`
# * modification de la taille des tableaux `numpy` avec `numpy.resize` et `numpy.reshape` (la mémoire sous-jacente est partagée)

# %% [markdown] tags=["framed_cell"]
# ## organisation de la mémoire
#
# ### pourquoi comprendre comment <code>numpy</code> travaille en mémoire ?
#
# <br>
#     
# pour prendre des décisions en connaissance de cause  
#
# * savoir les conséquences de vos choix
# * comprendre les erreurs  
# (conversions implicites...)
#
# <br>
#     
# pour ne pas être dépourvu le jour où votre code, en se complexifiant
#
# * devient beaucoup trop lent
# * prend beaucoup trop d'espace mémoire
#     
# <br>
#
# pour vous familiariser avec l'informatique et comprendre
#
# * les mécanismes sous-jacents 
# * les choix des concepteurs
#     
# <br>
#     
# pour vous faire une petite culture en informatique technique
#
# * ne jamais penser que c'est magique, incompréhensible, trop compliqué...
# * le plus souvent c'est simplement logique

# %% [markdown]
# créons un tableau `numpy` en 2 dimensions: 4 lignes et 5 colonnes

# %%
import numpy as np

# %%
mat =  np.array(
    [[1, 2, 3, 4, 5], 
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]])
mat

# %% [markdown]
# la mémoire occupée en mémoire en nombre d'octets (byte)

# %%
mat.nbytes

# %% [markdown] tags=["framed_cell"]
# ### organisation en mémoire des tableaux
#
# <br>
#     
# l'aide (accessible via `help(np.ndarray)`) dit 
# > *An array object represents a multidimensional, homogeneous array of fixed-size items.*
#     
# <br>
#     
# donc un `numpy.ndarray` est un tableau
# 1. **multi-dimensionnel**
# 1. avec un type d'élément **homogène**
# 1. et des éléments de **taille fixe**
#
# <br>
#     
# **homogène**  
#
# * toutes les cases du tableau ont le même type
# * donc elles occupent la même taille en mémoire
# <br>
#     
# **taille fixe**  
#
# * une fois un tableau créé, on ne peut plus modifier la taille de ses éléments  
# i.e. le nombre d'octets sur lequel chaque élément est stocké en mémoire est fixe
#     
#     
#     
# * si on manipule et que la taille des éléments ne suffit plus ?   
# `numpy` convertit la valeur  
# mais ne modifie pas la taille de ses éléments
#     
#     
# * pour modifier la taille des éléments ?  
# on n'a pas le choix, il faut allouer un nouveau tableau, et recopier l'ancien dedans (et c'est à éviter...) 
#     
# <br>
#     
# pourquoi ces **contraintes** ?  
# * pour que `numpy` soit le plus rapide possible dans ses manipulations de tableaux
# * grâce à ces contraintes, passer d'une case du tableau à une autre  est très rapide

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### rapidité des manipulations mémoire
# <br>
#     
# deux **idées** pour assurer la rapidité de manipulation de tableaux en mémoire
#     
#     
# * passez rapidement d'une case du tableau à une autre (**offset**) 
#     
#     
# * avoir la valeur de l'élément directement dans la case (pas **d'indirection** mémoire)

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### offset
#
# <br>
#     
# supposons que le tableau soit représenté en mémoire par un **bloc d'octets continu**  
# (ici 9 cases sont **contiguës** et de même taille - homogène)
#
# <div class="memory">
#
# ```
# ...☐☐☐☐☐☐☐☐☐...
# ```
#     
# </div>
#     
# <br>
#     
#     
# passer d'une case à une autre devient un simple décalage mémoire  
# *on va 2 cases plus loin*  
# <br>
#     
#     
# l'**offset** est la distance qui sépare ces deux cases
#
# <br>   
#     
# un tel décalage devient impossible si un tableau était réparti un peu partout en mémoire...  
#     
# <div class="memory">
#     
# ```
# ...☐.......☐..☐....☐...  
# ☐....☐.....☐.....☐.....  
# ......☐.....
# ```
#     
# </div>

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### pas d'indirection mémoire
# <br>
#     
# pour un tableau, on sait maintenant
#
# * que la taille des éléments est homogène  
# * que le bloc est contigu en mémoire
#     
# <div class="memory">
#     
# ```
# ☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐
# ```
# </div>
#     
# <br>
#     
#     
# l'idée de n'avoir pas d'indirection est
#
# * quand on arrive dans une case du tableau
# * elle contient la valeur qu'on cherche 
# * on n'a pas besoin d'aller ailleurs en mémoire
#     
# <br>
#
# Que pourrait-il y avoir d'autre dans une case que la valeur d'un élément ?
#     
# <br>
#     
# si toutes les cases d'un même tableau en informatique ont la même taille, comment puis-je
#
# * y "*mettre*"  des élément hétérogènes ? entier, réel, string... 
# * modifier ces éléments sans réallouer le tableau ?
#     
# <br>
#     
# ```python
# tab = [1, np.pi, True ]
# tab[0] = 12345678235234501256848345678901234567890264378034
# tab[0] = "bonjour"
# ```
#     
# <br>
#
# en `python`, dans une case d'un vecteur (`list`)
#
# * on ne trouve pas l'objet lui même (`1` ou `"bonjour"`)
# * mais l'**adresse** en mémoire de l'endroit où l'objet a été alloué
#     
# <br>
#     
# si un tableau contient les adresses de ses éléments  
# et pas directement la valeur des éléments  
# il y aura une indirection à faire quand on arrive sur une case

# %% [markdown]
# ### exercice: tableau de chaînes de caractères

# %% [markdown]
# **exercices**
#
# 1. à partir de la liste Python de chaînes de caractères
# ```python
# l = ['un', 'deux', 'trois', 'cinq']
# ```
# créez un tableau `numpy.ndarray` (de nom `tab`) et affichez-le
# <br>
#
# 1. modifiez le premier élément pour mettre `quatre`
# ```python
# tab[0] = 'quatre'
# ```
# et affichez le tableau
# <br>
#
# 1. Que constatez-vous ? Pourquoi `quatr` ?
# <br>
#
# 1. affichez le type des éléments, le comprenez-vous ?  
# `<` est une histoire d'ordre des octets dans les objets  
# `U` signifie unicode  
# Que signifie `5` ?

# %%
# votre code ici

# %%
# prune-cell
l = ['un', 'deux', 'trois', 'cinq']
tab = np.array(l)
print(    tab    )
tab[0] = 'quatre'
print(    tab    )
tab.dtype

# %% [markdown]
# `numpy` cherche le plus petit type pour stocker les chaînes de caractères initiales
#
# ici une case est constituée d'un tableau d'au plus 5 caractères  
# (une case n'est pas l'adresse d'une chaîne de caractère mais bien la valeur de la chaîne)

# %% [markdown]
# ### exercice: tableau hétérogène

# %% [markdown]
# **exercice**
#
#
# 1. créez un tableau `np.ndarray` à partir de la liste Python suivante
# ```python
# l = [127, 128, 17.4, np.pi, True, False]
# ```
# <br>
#
# 1. affichez le type des éléments  
# que constatez-vous ?  
# que `numpy` a trouvé le plus petit type pouvant contenir tous ces objets numériques
# <br>
#
# 1. ajoutez à la liste Python `l`, la chaîne de caractères `bonjour`  
# et créez un autre `numpy.ndarray` à partir de la nouvelle valeur de `l`
# <br>
#
# 1. affichez les éléments    
# Que constatez-vous ? 
# <br>
#
# 1. quel type `numpy` a-t-il trouvé pour stocker tous ces éléments ?

# %%
# votre code ici

# %%
# prune-cell
l = [127, 128, 17.4, np.pi, True, False]
tab = np.array(l)
print(    tab.dtype    )

# %%
# prune-cell
l.append('bonjour')
tab = np.array(l)
tab

# %% [markdown]
# Pour plus d'informations, voir https://numpy.org/doc/stable/user/basics.types.html

# %% [markdown]
# ## index des tableaux

# %% [markdown] tags=["framed_cell"]
# ### forme des tableaux numpy
#
# <br>
#     
# la mémoire d'un `numpy.ndarray` est **toujours** un **segment unidimensionnel continu de cases de même taille et même type**
#     
# <div class="memory">
#     
# ```    
# ☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐
# ```
# </div>
#     
# <br>
#
# `numpy` crée sur cette base, un système d'indexation
#
# * pour *considérer* le tableau sous une forme (`shape`) multi-dimensionnelle

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### 1-dimension
#
# <br>
#       
# créons un tableau de dimension 1 donc de `shape=(30,)`   
# ```python
# seg = np.ones(shape=(30,))
# ```
#
# <br>
#     
# un seul index suffit à le parcourir
#
# <div class="memory">
#
# ```
#  ☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐
#             ↑
#            seg[i]
#                
# ```
#
# </div>
#     
# <br>
#
# l'index est l'offset à partir du premier élément du tableau
#     
# <br>
#
# le premier élément du tableau est indiqué par `seg`  
# avec un offset de `0`
#     
# <br>
#     
# voila pourquoi la plupart du temps en informatique, les **tableaux commencent à l'index 0**
# (et pas 1, sauf pour *matlab*, *R*, *Fortran*...)

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### 2-dimension
#
# <br>
#       
# créons un tableau de dimension 2, par exemple de `shape=(5, 6)`   
# ```python
# seg = np.ones(shape=(5, 6))
# ```
#
# <br>
#     
# il faut 2 index pour le parcourir  
#     un pour les lignes et un pour les colonnes `seg[i, j]`
#
# <div class="memory">
#
# ```
#     
#    ☐☐☐☐☐☐
#    ☐☐☐☐☐☐
# i  ☐☐☐☐☐☐
#    ☐☐☐☐☐☐
#    ☐☐☐☐☐☐
#       ↑
#       j
#                
# ```
#
# </div>    
#
# ${0 \leq i \leq 4}$  
# ${0 \leq j \leq 5}$

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### 3-dimension
#
# <br>
#      
# créons un tableau de dimension 3, par exemple de `shape=(4, 5, 6)`   
# ```python
# seg = np.ones(shape=(4, 5, 6))
# ```
#
# <br>
#       
# 3 index pour le parcourir `seg[i, j, k]`  
# table, ligne, colonne
#
# <div class="memory">
#     
# ```
#                   i   
#     
#    ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐
#    ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐
#  j ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐
#    ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐
#    ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐   ☐☐☐☐☐☐
#       k        
#                
# ```
#
# </div> 
#     
#     
# et ainsi de suite

# %% [markdown]
# ## changer la forme d'un tableau

# %% [markdown] tags=["framed_cell"]
# ### fonctions `resize` et `reshape`
#
# <br>
#
# on peut modifier la forme d'un `numpy.ndarray` existant  
# tant qu'on ne modifie pas son nombre d'éléments
#     
# <br>
#     
# deux fonctions pour *réindexer* un tableau: `ndarray.reshape` et `ndarray.resize`
#     
# <br>
#
# `np.ndarray.reshape`  
# renvoie un tableau contenant les mêmes données avec une nouvelle forme
#     
# <br>
#     
# `np.ndarray.resize`  
# modifie la forme du tableau *en-place* (directement dans le tableau)  
# et ne renvoie donc rien
#     
# <br>
#     
# aucune des deux fonction ne crée un nouveau segment de données  
# elle ne recréent que l'indexation  
#     
# <br>
#     
# **reshape**    
#
# ```python
# seg = np.arange(0, 30)
# seg = seg.reshape(5, 6) # reshape retourne le tableau ainsi modifié
# seg = seg.reshape(2, 5, 3)
# ```
#     
# on peut le faire dès la création du tableau
#
# ```python
# l = range(30)
# seg = np.array(l).reshape(2, 5, 3)
# ```
# <br>
#
# **resize**
#     
# ```python
# seg = np.arange(0, 30)
# seg.resize(5, 6) # resize modifie le tabeau en place
# seg.resize(2, 5, 3)
# ```
#    
# <br>
#
# si aucune mémoire n'est créée, c'est que les différentes indexations prises sur un tableau  
# **partagent l'objet sous-jacent**

# %%
# le code
seg = np.arange(0, 30)
seg = seg.reshape(5, 6) # reshape retourne le tableau ainsi modifié
print(seg)
seg = seg.reshape(2, 5, 3)
print(seg)

# %%
# le code
seg = np.arange(0, 30)
seg.resize(5, 6) # resize modifie le tabeau en place
print(seg)
seg.resize(2, 5, 3)
print(seg)

# %% [markdown]
# ### mémoire partagée

# %% [markdown]
# **exercice**
#
# 1. créez un tableau `tab` de 6 `ones` de forme `(6)`  
# et affichez-le
# <br>
# 1. mettez dans `tab1` le reshape de `tab` avec la forme `(3, 2)`  
# et affichez-le
# <br>
# 1. modifiez le premier élément de `tab`
# <br>
# 1. affichez `tab1`  
# a-t-il été modifié ?
# <br>
#
# les deux objets  `tab` et `tab1` de type `numpy.ndarray`
#
# * sont des objets différents (leurs index sont différents)
# * mais ils ont le même segment sous-jacent de données
# * toucher l'un a pour effet de modifier l'autre

# %%
# votre code

# %%
# prune-cell
tab = np.ones(shape=(6))
print(    tab    )

tab1 = tab.reshape(3, 2)
print(    tab1    )

tab[0] = 99
print(    tab    )
print(    tab1    )

# %% [markdown] tags=["framed_cell"]
# ## les lignes et colonnes
#
# <br>
#     
# pour les tableaux `numpy.ndarray` en dimension supérieure ou égale à 2
#
# * les deux dernières valeurs de leur forme  `tab.shape`   
# sont leur nombre de ligne et leur nombre de colonne
#     
# <br>
#  
# **exercice**
#     
# 1. faites un tableau de `ones` de forme `(1, 2, 3, 4, 5)`
# 1. afficher son nombre de lignes et son nombre de colonnes

# %%
tab = np.ones(shape=(1, 2, 3, 4, 5))
print(tab.shape[-2:])

