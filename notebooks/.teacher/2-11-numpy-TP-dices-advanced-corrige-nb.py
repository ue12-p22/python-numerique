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
#     title: exercice sur le *broadcasting*
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %% [markdown]
# # exercice sur le *broadcasting*

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %%
import numpy as np

# %% [markdown]
# ### résultats du tirage de `n` dès à `s` faces

# %% [markdown]
# Deux versions pour cet exercice:
#    - la première est pour les débutants, elle est guidée et amène à construire le résultat pas à pas
#    - la deuxième est pour les forts qui se débrouillent tout seuls

# %% [markdown]
# #### version pour les débutants

# %% [markdown]
# On veut calculer les résultats des tirages de `n` dés à `s` faces. Afin, par exemple de faire des probabilités d'obtention de certains tirages. De combien de manières différentes peut-on obtenir `7` avec `3` dès à `6` faces.

# %% [markdown]
# Si nous prenons un seul dès à `6` faces. Quels sont les tirages possibles ?
#
# oui `1, 2, 3, 4, 5, 6`
#
# Construisez alors un `numpy.ndarray` contenant les tirages d'un dès à `s` faces.

# %%
# votre code ici

# %%
# prune-cell
S1 = np.arange(1, 7)
S1

# %% [markdown]
# Maintenant si on prend `n=2` dès à `s=6` faces. Quels sont les tirages possibles ?
#
# Oui:
#
# |  +  | &#124; | 1 | 2 | 3 | 4 | 5 | 6 |
# |:---:|:------:|:-:|:-:|:-:|:-:|:-:|:-:|
# | *1* | &#124; | 2 | 3 | 4 | 5 | 6 | 7 | 
# | *2* | &#124; | 3 | 4 | 5 | 6 | 7 | 8 | 
# | *3* | &#124; | 4 | 5 | 6 | 7 | 8 | 9 | 
# | *4* | &#124; | 5 | 6 | 7 | 8 | 9 |10 | 
# | *5* | &#124; | 6 | 7 | 8 | 9 |10 |11 | 
# | *6* | &#124; | 7 | 8 | 9 |10 |11 |12 | 
#
#
# Construisez alors un `numpy.ndarray` contenant les tirages de `n=2` dès à `s=6` faces. Un indice ? Utilisez le `broadcasting`:
#
# On vous fait un rappel. Si on ajoute en `numpy` un tableau de forme `(3,)` à un tableau de forme `(3, 1)` on obtient la matrice suivante: $\begin{pmatrix} a_{1} & a_{2} & a_{3} \end{pmatrix} + \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = \begin{pmatrix} a_{1} + b_1 & a_{2} + b_1 & a_{3} + b_1 \\ a_{1} + b_2 & a_{2} + b_2 & a_{3} + b_2 \\ a_{1} + b_3 & a_{2} + b_3 & a_{3}  + b_3\\ a_{1} + b_4 & a_{2} + b_4 & a_{3} + b_4 \end{pmatrix}$

# %%
# votre code ici

# %%
# prune-cell

S1_ = S1.reshape((6, 1))
# print(S1_)
S2 = S1 + S1_
S2

# %% [markdown]
# On remarque que la dimension de notre tableau est le nombre de dès.

# %% [markdown]
# On continue.
#
# Maintenant si je prends `3` dès avec `6` faces, je suis en dimension `3` et je veux donc obtenir un *cube* (avec tous les résultats). Pour obtenir ce cube, je pars de ma matrice (de forme `(s, s)`) des tirages en dimension 2 et j'utilise le broadcast pour lui ajouter une troisième dimension.
#
# Quelle est la forme de ce vecteur ? Il doit déclencher le broadcast donc il doit être de forme `(s, 1, 1)`.
#
# En effet  
# (i) la forme `(s, )` c'est la forme des lignes de la matrice  
# (ii) la forme `(s, 1)` est celle des colonnes  
# (iii) la forme `(1, ..., 1, s)` se broadcast en ligne comme `(1, s)` ou `(s,)` (essayez)
# (iv) la forme `(s, 1, 1)` forcera le broadcast en un cube
#
# Vous avez maintenant tous les indices pour généraliser en dimension `n` dès (vous aurez naturellement une boucle mais bien sûr pas sur les éléments d'un `numpy.ndarray` !)

# %%
# votre code ici

# %%
# prune-cell
S2_ = S1_.reshape((6, 1, 1))
S3 = S2 + S2_
S3

# %% [markdown]
# Cet espace des tirage pourra nous resservir dans de futurs exercices.
#
# Vous remarquez qu'on est dans une manière de faire qui **explicite l'ensemble des solutions** ce qu'on appelle une méthode en force brute. Ces méthodes sont clairement exponentielles.

# %% [markdown] {"tags": ["level_advanced"]}
# #### les dès version  pour les forts

# %% [markdown] {"tags": ["level_advanced"]}
# On étudie les probabilités d'obtenir une certaine somme avec plusieurs dés. 
#
# Tout le monde connaît le cas classique avec deux dés à 6 faces, ou l'on construit mentalement la grille suivante:
#
# |  +  | &#124; | 1 | 2 | 3 | 4 | 5 | 6 |
# |:---:|:------:|:-:|:-:|:-:|:-:|:-:|:-:|
# | *1* | &#124; | 2 | 3 | 4 | 5 | 6 | 7 | 
# | *2* | &#124; | 3 | 4 | 5 | 6 | 7 | 8 | 
# | *3* | &#124; | 4 | 5 | 6 | 7 | 8 | 9 | 
# | *4* | &#124; | 5 | 6 | 7 | 8 | 9 |10 | 
# | *5* | &#124; | 6 | 7 | 8 | 9 |10 |11 | 
# | *6* | &#124; | 7 | 8 | 9 |10 |11 |12 | 
#
# Imaginons que vous êtes un étudiant, vous venez de faire un exercice de maths qui vous a mené à une formule qui permet de calculer, pour un jeu à `nb_dice` dés, chacun à `sides` faces, le nombre de tirages qui donnent une certaine somme `target`.
#
# Vous voulez **vérifier votre formule**, en appliquant une **méthode de force brute**. C'est-à-dire constuire un hypercube avec toutes les possibilités de tirage, puis calculer pour chaque point dans l'hypercube la somme correspondante; de cette façon on pourra compter les occurrences de `target`.
#
# C'est l'objet de cet exercice. Vous devez écrire une fonction `dice` qui prend en paramètres:
#
# * `target` : la somme cible à atteindre,
# * `nb_dice` : le nombre de dés,
# * `sides`: le nombre de faces sur chaque dé.
#
# On convient que par défaut `nb_dice`=2 et `sides`=6, qui correspond au cas habituel.
#
# Dans ce cas-là par exemple, on voit, en comptant la longueur des diagonales sur la figure, que `dice(7)` doit valoir 6, puisque le tableau comporte 6 cases contenant 7 sur la diagonale.
#
# À nouveau, on demande explicitement ici un parcours de type force brute; c'est-à-dire de créer sous la forme d'un tableau `numpy`, un hypercube qui énumère toutes les combinaisons possibles; et sans faire de `for` sur les éléments d'un tableau.

# %% [markdown] {"tags": ["level_advanced"]}
# https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x4-dice

# %% [markdown] {"tags": ["level_advanced"]}
# **Indice**
#
# Il existe en `numpy` une astuce pour augmenter la dimension d'un tableau, ça s'appelle `np.newaxis`, et ça s'utilise comme ceci

# %% {"cell_style": "center", "tags": ["level_advanced"]}
dice_1 = np.arange(1, 7)
dice_2 = dice_1[:, np.newaxis]

# %% {"cell_style": "split", "tags": ["level_advanced"]}
dice_1

# %% {"cell_style": "split", "tags": ["level_advanced"]}
dice_2

# %% [markdown] {"tags": ["level_advanced"]}
# et remarquez que pour créer le tableau ci-dessus il suffit de faire

# %% {"tags": ["level_advanced"]}
dice_1 + dice_2


# %%
# prune-cell

def dice(target, nb_dice=2, nb_sides=6):
    """
    Pour un jeu où on lance `nb_dice` dés qui ont chacun `sides` faces,
    quel est le nombre de tirages dont la somme des dés fasse `target`

    Version force brute, il y a bien sûr des outils mathématiques
    pour obtenir une réponse beaucoup plus rapidement

    Toutes les solutions procèdent en deux étapes

    * calcul de l'hypercube qui énumère les tirages,
      et calcule la somme des dés pour chacun de ces tirages
    * trouver le nombre de points dans le cube où la somme des dés
      correspond à ce qu'on cherche

    les deux étapes sont indépendantes, et peuvent donc être mélangées
    entre les solutions
    """

    # pour élaborer le cube, on procède par broadcating
    # on commence avec un simple vecteur de shape (nb_sides,) - e.g. de 1 à 6
    # on lui ajoute lui-même mais avec une forme (nb_sides, 1) - en colonne donc
    # et ainsi de suite avec
    # shape=(nb_sides, 1, 1) pour la dimension 3,
    # shape=(nb_sides, 1, 1, 1) pour la dimension 4
    sides = np.arange(1, nb_sides+1)
    cube = sides
    # une liste plutôt qu'un tuple pour décrire la shape,
    # car on va y ajouter '1' à chaque tour
    shape = [nb_sides]
    # on a déjà un dé
    for _dimension in range(nb_dice - 1):
        shape.append(1)
        cube = cube + sides.reshape(shape)

    # le cube est prêt,
    # pour chercher combien de cases ont la valeur target,
    # on peut faire par exemple
    return np.sum(cube == target)    


# %%
# prune-cell

def dice_2(target, nb_dice=2, nb_sides=6):
    """
    une variante de la première forme, qui utilise
    astucieusement une matrice diagonale pour énumérer
    les 'shapes' qui entrent en jeu

    credits: aurelien
    """
    sides = np.arange(1, nb_sides+1)
    shapes = np.diag([nb_sides-1]*nb_dice) + 1
    # attention ici c'est le sum Python
    # et non pas np.sum qui ferait complètement autre chose
    cube = sum(sides.reshape(s) for s in shapes)

    # une autre façon de faire le décompte
    return np.count_nonzero(cube == target)
