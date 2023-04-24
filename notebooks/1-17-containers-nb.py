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
#     title: types containers
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
# # types containers

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la liste
#
# permet de créer des collections très souples :
#
# * séquence d'objets de n'importe quel type
# * on peut insérer / détruire des objets
# * pas de contrainte sur la taille

# %% cell_style="split"
# on crée une liste avec des [ ]
homogene = [0, 12]
homogene

# %% cell_style="split"
# on peut mélanger
# les types
heterogene = [2.3, "abc"]
heterogene

# %% cell_style="split"
# des listes dans des listes
groupe = [True, homogene,
          "chaine", heterogene]
groupe

# %% cell_style="split"
type(groupe)

# %% cell_style="split" slideshow={"slide_type": "slide"}
groupe

# %% cell_style="split" slideshow={"slide_type": ""}
# comme avec les chaines
# on peut accéder au i-ème élément
# les indices commencent à 0

# le premier élément est
# donc le booléen
groupe[0]

# %% cell_style="split"
# on peut remplacer un élément
groupe[1] = '-'
groupe

# %% cell_style="split"
# et le dernier
groupe[-1]

# %% cell_style="split"
# est heterogene
groupe[-1] == heterogene

# %% cell_style="split"
# le slicing s'applique aussi
# comme sur les chaines de caractère
groupe[::2] # du début à la fin avec un pas de 2

# %% [markdown] slideshow={"slide_type": "slide"}
# ## liste et opérateurs

# %% [markdown]
# de nombreux opérateurs sont définis aussi sur les listes

# %% cell_style="split"
# on peut ajouter deux listes,
# ça les concatène
[1, 2, 3] + [4, 5, 6]

# %% cell_style="split"
# la comparaison est
# lexicographique

[1, 2, 3] <= [1, 2, 4]

# %% cell_style="split"
# l'opérateur d'appartenance
'chaine' in groupe

# %% cell_style="split"
# et sa négation
'tutu' not in groupe

# %% [markdown] slideshow={"slide_type": "slide"}
# ## itérations
#
# approfondi dans une section ultérieure  
# mais dans sa forme la plus simple: `for .. in .. :`

# %%
for item in groupe:
    print(item)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## listes et performances

# %% [markdown]
# **À savoir**  
# la liste est une structure de données très souple du coup elle n'est que *relativement
# efficace*  
# elle est surtout optimisée pour être modifiée **par la fin**  
# habituellement à base des méthodes `append` et `pop`

# %% cell_style="split"
tutu = []

# on n'a pas encore vu le for
# mais vous pouvez deviner ce que ça fait
for c in 'abc':
    tutu.append(c)
    print(tutu)

# %% cell_style="split"
# et à l'envers
while tutu:
    c = tutu.pop()
    print(c)

# %% [markdown]
# MAIS cela n'est un problème qu'avec des données nombreuses - $10^4$  
# du coup pour des preuves de concept la liste est **TRÈS** flexible et pratique

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le tuple
#
# similaire à la liste, mais qu'**on ne peut pas modifier**  
# (on parle d'objets **non mutables** - ou immuables)  
# ne sera pas approfondi dans ce primer  
# on va voir tout de suite à quoi ça peut bien servir

# %% cell_style="split"
# ressemble à une liste, mais s'écrit avec des ()

paquet = (12, "abc")
paquet

# %% cell_style="split"
# on ne peut plus y toucher
# paquet[0] = 15 n'est pas autorisé
# ni paquet.append(0)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## l'ensemble

# %% [markdown]
# une autre forme de container, mais assez différent :  
#
# * comme pour les ensembles mathématiques, un même élément  
#   ne peut apparaitre qu'une seule fois dans un ensemble
#
# * la **recherche d'un élément** dans un ensemble est **très efficace**  
#   contrairement aux listes, on n'a pas besoin de balayer tous les éléments  
#   repose sur la notion de table de hachage - détaillé dans le cours avancé
#
# * par contre, limitation sur les éléments  
#   certains types ne sont pas éligibles
#   par ex. on ne peut pas mettre une liste dans un ensemble  
#   utiliser à la place un `tuple`

# %% cell_style="split" slideshow={"slide_type": "slide"}
# pour créer un ensemble
ensemble = {12, "abc"}
ensemble

# %% cell_style="split"
# méthode add() pour ajouter
ensemble.add(True)
ensemble

# %% cell_style="split"
# pas de doublon
ensemble.add("abc")
ensemble

# %% cell_style="split"
# la recherche est rapide
# bien sûr, c'est surtout intéressant
# sur des grosses données

12 in ensemble

# %% cell_style="split"
# on peut mettre un tuple dans un ensemble
ensemble.add((2, 3))
ensemble

# %% cell_style="split"
# et pour enlever
ensemble.remove(12)
ensemble

# %% [markdown] slideshow={"slide_type": "slide"}
# ### itérations sur l'ensemble

# %% [markdown]
# forme la plus simple, idem : `for .. in ..`  
# attention qu'un ensemble n'a pas d'ordre naturel  
# depuis Python-3.7 le parcours se fait dans l'ordre des insertions

# %%
for item in ensemble:
    print(item)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le dictionnaire
#
# aussi un container, mais cette fois c'est conceptuellement  
# un ensemble d'associations de la forme
#
#     clé → valeur

# %% cell_style="split"
# la syntaxe pour créer
# un dictionnaire en clair
annuaire = {'alice': 25, 'bob': 32}

# %% cell_style="split"
# les clés sont ici les 2 chaines
# 'alice', 'bob'

annuaire

# %% cell_style="split" slideshow={"slide_type": "slide"}
# on ne peut plus accéder par indice
# annuaire[0] ne veut rien dire!

# par contre on peut accéder par clé
annuaire['bob']

# %% cell_style="split"
# pareil pour écrire
# si la clé est inconnue on l'ajoute

annuaire['eve'] = 40
annuaire

# %% cell_style="split"
# si la clé existe déjà
# on écrase la valeur associée
annuaire['alice'] = 50
annuaire

# %% cell_style="split"
# pour effacer une clé  
del annuaire['eve']
annuaire

# %% cell_style="split" slideshow={"slide_type": ""}
annuaire

# %% cell_style="split"
# la recherche d'une clé est aussi rapide
# que la recherche dans les ensembles

'alice' in annuaire

# %% [markdown] slideshow={"slide_type": "slide"}
# ## digression : affectation multiple

# %% cell_style="split"
# plutôt que de faire
a = 10
b = 20

print(f"a={a}, b={b}")

# %% cell_style="split"
# on peut faire en Python
a, b = 10, 20

print(f"a={a}, b={b}")

# %% [markdown]
# dans ce contexte c'est un gadget, mais c'est intéressant parfois  
# car les termes à droite de `=` sont tous évalués avant de faire les affectations

# %% slideshow={"slide_type": ""}
# et ainsi on peut par exemple
# échanger deux variables
a, b = b, a

print(f"a={a}, b={b}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## itération sur un dictionnaire

# %% [markdown]
# même remarque que les ensembles : pas d'ordre naturel  
# depuis Python-3.7 le parcours se fait dans l'ordre des insertions

# %%
for cle, valeur in annuaire.items():
    print(f"{cle} → {valeur}")

# %% [markdown]
# cette forme est à mettre en rapport avec l'affectation multiple  
# dans ce sens que ça revient à faire ceci :

# %%
# en décomposant un peu pour bien comprendre
for couple in annuaire.items():
    cle, valeur = couple # on appelle cela de l'unpacking
    print(f"{cle} → {valeur}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonctions et arguments multiples (1)
#
# **optionnel**

# %% [markdown]
# mécanisme pour définir un nombre quelconque d'arguments à une fonction

# %%
# parfois on a envie qu'une fonction puisse
# accepter un nombre variable d'arguments

def foo(fixe, *variable):
    """
    fixe reçoit le premier argument
    variable reçoit un tuple avec tous les autres arguments de l'appel
    """
    print(f"premier argument: {fixe}")
    print(f"les autres: {variable} - de type {type(variable)}")
    for item in variable:
        print(f"item {item}")


# %% cell_style="split"
foo(1)

# %% cell_style="split"
foo(1, 2)

# %%
foo(1, 2, 3)

# %% [markdown] slideshow={"slide_type": "notes"}
# bien entendu on ne peut définir qu'un seul paramètre de ce genre, et il doit apparaitre en
# dernier dans la signature de la fonction  
# Si on pouvait en mettre plusieurs, il y aurait ambigüité quant à qui reçoit quoi.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonctions et arguments multiples (2)
#
# **optionnel**

# %% [markdown]
# dans l'autre sens, si j'ai un container avec des objets
# que je veux passer individuellement à une fonction

# %%
# par exemple j'ai une liste
args = [1, 2, 3]

# et en fait je veux appeler
# foo(1, 2, 3)
#
# je pourrais faire
# foo(args[0], args[1], arg[2])
#
# mais bien sûr ça ne marchera
# que si args contient 3 objets

# %% cell_style="split"
# dans ce cas on peut utiliser à nouveau
# l'étoile, et faire plutôt
foo(*args)

# %% cell_style="split"
# vérifions que c'est bien
# ce qu'on voulait
foo(1, 2, 3)

# %% [markdown] slideshow={"slide_type": "notes"}
# à l'appel de la fonction par contre on peut passer plusieurs arguments étoilés, leurs
# composants sont simplement ajoutés dans l'ordre aux arguments de la fonction.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé
#
# Python propose des types prédéfinis
#
# * `list` : un container flexible et ordonné, accessible par indice
# * plus accessoirement, `tuple` pour créer des containers similaires mais non modifiables
# * `set` : un container non-ordonné, sans doublon, et à recherche rapide
# * `dict` : un ensemble d'associations clé → valeur,  
#   à recherche rapide, accessible par clé
#
# * la forme `*args` permet aux fonctions d'accepter un nombre quelconque d'arguments
#   * définition `def foo(*args):`
#   * appel `foo(*args)`
