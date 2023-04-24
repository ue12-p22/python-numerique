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
#     title: "it\xE9rations"
#   rise:
#     autolaunch: false
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # itérations

# %% [markdown] slideshow={"slide_type": "slide"}
# ## boucle `for`

# %% [markdown] cell_style="split"
# **rappel** pour itérer sur une liste ou un ensemble :
#
# ```python
# for item in container:
#    ...
# ```

# %% [markdown] cell_style="split"
# sur un dictionnaire
#
# ```python
# for cle, valeur in d.items():
#     ...
# ```

# %% [markdown]
# en fait on peut itérer sur un grand nombre d'objets  
# que par définition on appelle **itérables**  
# dont une sous-famille remarquable est celle des **itérateurs**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## itérateurs
#
# vous voulez faire une boucle `for` sur les entiers de 0 à $10^6$  
# avec ce qu'on a vu jusqu'ici, on serait tenté de  
# 1. construire une liste avec les entiers de 0 à 1 million  
# 2. et itérer sur cette liste avec un `for`

# %% [markdown]
# **MAIS** ce n'est pas une bonne idée  
# notamment car ça demande une grosse **allocation mémoire**  
# qui est loin d'être gratuite en termes de performance  
# en fait pour faire cette énumération  
# on n'a besoin que d'**une seule case mémoire**  
# ```c++
# // en C++ on écrirait quelque chose comme
# for (int i=0; i<=1000000; i++) {
#     ...
# }
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `range()`

# %% [markdown] cell_style="split"
# Python offre pour cela une fonction prédéfinie `range(n)`

# %% cell_style="split"
for i in range(4):
    print(i)

# %% [markdown]
# le résultat de la fonction `range()` **n'est pas une liste**  
# c'est ce qu'on appelle un **itérateur**  
# c'est à dire un **tout petit objet** (en terme d'occupation mémoire)  
# qui ne fait que **mémoriser où on en est** dans l'itération

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `range()` - suite

# %% [markdown]
# l'impact sur les performances est majeur !

# %% cell_style="split"
# option avec itérateur

# temps de construction
# de l'objet range
# %timeit -n 1000  range(10**6)

# espace mémoire occupé
# par le range - en octets
iterateur = range(10**6)
import sys
sys.getsizeof(iterateur)

# %% cell_style="split"
# option avec liste

# ici je construis une liste explicite
# et le plus simple en Python est
# d'appeler list() sur l'itérateur

# temps de construction
# %timeit -n 5 list(range(10**6))

# espace mémoire
explicit = list(range(10**6))
import sys
sys.getsizeof(explicit)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `enumerate()`

# %% cell_style="split"
sujets = ['james', 'henri', 'louis']

# on veut lister les éléments
# avec leur indice, c'-à-d produire
# 0: james
# 1: henri
# 2: louis

# %% [markdown] cell_style="split"
# quand on itère sur une  
# liste, comment faire quand  
# à l'intérieur de la boucle  
# on a besoin de l'indice  
# d'énumération ?

# %% cell_style="split"
# bien que ça marche ..
# IL NE FAUT PAS faire comme ça !
for i in range(len(sujets)):
    item = sujets[i]
    print(f"{i}: {item}")

# %% cell_style="split"
# c'est à ça que sert enumerate()

for i, item in enumerate(sujets):
    print(f"{i}: {item}")

# %% [markdown] cell_style="center"
# c'est le propos de la fonction `enumerate()`

# %% [markdown] slideshow={"slide_type": "notes"}
# ce style de programmation à base d'indices est tentant, surtout lorsqu'on vient d'un autre
# langage, mais c'est considéré comme pas du tout pythonique. Il est important de prendre
# l'habitude d'utiliser la boucle `for` de la bonne façon, notamment car la programmation
# par indice ne se prête pas du tout aux itérations plus sophistiquées que nous allons
# étudier.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## boucle `for` - généralisation
#
# de manière générale, on peut écrire une boucle `for` sur un très grand nombre d'objets :
#
# * fichiers en lecture (voir plus loin)
# * itérables du [module `itertools`](https://docs.python.org/3/library/itertools.html)
# * ...

# %%
# itertools contient des itérateurs pour
# matérialiser la plupart des combinatoires
# habituelles

import itertools

# %% cell_style="split" slideshow={"slide_type": "slide"}
from itertools import product # produit carthésien

cartes = ['V', 'D', 'R', 'As']
couleurs = ['♢', '♧', '♡', '♤']

for carte, couleur in product(cartes, couleurs):
    print(f"{carte} de {couleur}")

# %% cell_style="split"
from itertools import permutations

for tirage in permutations(couleurs):
    print(tirage)

# %% [markdown] slideshow={"slide_type": "notes"}
# Dans le cas de la fonction `itertools.product`, remarquez que notre code revient à faire
# deux boucles imbriquées.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `break` et `continue`
#
# dans le corps d'une boucle (`for` ou `while`), on peut utiliser:
#
# * `break` pour terminer directement la boucle
# * `continue` pour passer directement à l'itération suivante

# %% cell_style="split"
# pour illustrer break

# les 4 premières permutations seulement
# remarquez l'emploi de enumerate
for index, tirage in enumerate(
    permutations(couleurs)):
    print(tirage)
    if index >= 4:
        break

# %% cell_style="split"
# pour illustrer continue

# les cartes rouges seulement

for couleur in couleurs:
    if couleur in '♤♧':
        continue
    for carte in cartes:
        print(f"{carte} de {couleur}")

# %% [markdown] slideshow={"slide_type": "slide"}
# `break` et `continue` sont toujours relatives  
# à la boucle la plus imbriquée

# %% cell_style="split"
# une seule boucle
for x, y in product(cartes[:2],
                    couleurs[:2]):
    print(f"{x} de {y}")

# %% cell_style="split"
# idem mais avec
# deux boucles imbriquées
for x in cartes[:2]:
    for y in couleurs[:2]:
        print(f"{x} de {y}")

# %% cell_style="split"
# mais le break n'a pas le même
# comportement dans les deux cas
for x, y in product(cartes[:2],
                    couleurs[:2]):
    if y == '♧':
        break
    print(f"{x} de {y}")

# %% cell_style="split"
# car ici il sort que
# de la boucle intérieure
for x in cartes[:2]:
    for y in couleurs[:2]:
        if y in '♧':
            break
        print(f"{x} de {y}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## compréhension

# %% [markdown]
# un raccourci syntaxique pour construire des containers par itération

# %% cell_style="center"
entrees = [10, -10, 421]

# %% cell_style="split"
# compréhension de liste
[x**2 for x in entrees]

# %% cell_style="split"
# compréhension d'ensemble
{x**2 for x in entrees}

# %% cell_style="split"
# compréhension de dictionnaire
{x : x**2 for x in entrees}

# %% cell_style="split" slideshow={"slide_type": ""}
# avec filtrage - avec toutes
# les variétés de compréhensions
{x**2 for x in entrees if x % 2 == 0}

# %% [markdown] slideshow={"slide_type": "slide"}
# ## expressions génératrices

# %% [markdown]
# la compréhension est souvent élégante  
# mais elle souffre du même problème qu'on a vu plus haut  
# elle **alloue de la mémoire** pour ranger les résultats  
# et dans ces cas-là un **itérateur** est un bien meilleur choix

# %% [markdown]
# dans ces cas-là, il suffit de prendre la compréhension de liste  
# et remplacer les `[]` par `()`  
# cela s'appelle une **expression génératrice**

# %% [markdown] slideshow={"slide_type": "notes"}
# Le fait de devoir allouer de la mémoire a plusieurs inconvénients. Tout d'abord bien
# entendu, la mémoire est une ressource finie, qu'il faut donc utiliser avec parcimonie. De
# plus, lorsqu'un programme a besoin de mémoire il la demande au système d'exploitation, et
# c'est une opération bien plus lente qu'on pourrait le soupçonner naïvement ; et même sur
# une machine dotée d'une mémoire énorme, ce temps d'allocation pénalise les performances.

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# Benchmark : la somme des premiers entiers.

# %% cell_style="split"
# avec une compréhension

# %timeit sum([x for x in range(10**6)])

# %% cell_style="split"
# même chose mais avec
# une expression génératrice

# %timeit sum(x for x in range(10**6))

# %% cell_style="split"
# taille mémoire

comprehension = [x for x in range(10**6)]

sys.getsizeof(comprehension)

# %% cell_style="split"
# aucune comparaison !

generatrice = (x for x in range(10**6))

sys.getsizeof(generatrice)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé
#
# pour itérer sur une suite (un itérable) d'entrées
#
# * on peut écrire un `for`,
# * ou une compréhension,
# * ou une expression génératrice
#
# on n'itère **jamais** sur `range(len(iterable))`  
# on utilise `enumerate` à la place
#
# dans tous les cas où c'est possible
#
# * on recommande d'utiliser un itérateur
# * de préférence à une allocation explicite des résultats
