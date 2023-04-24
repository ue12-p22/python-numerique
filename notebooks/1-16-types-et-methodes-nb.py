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
#     title: "objets, types et m\xE9thodes"
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
# # objets, types et méthodes

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Python est un paradigme orienté objet  
#
# cela signifie que toutes vos données sont des objets  
# entre autres choses chaque objet a un type

# %% cell_style="split" slideshow={"slide_type": "slide"}
# en Python absolument toutes les données
# en mémoire sont des objets
# chaque objet possède (entre autres)
# un type

# un module
import math

# un nombre
x = 4 * math.pi

# une chaine
texte = "une chaine"

# une fonction
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)


# %% cell_style="split"
type(x)

# %% cell_style="split"
type(texte)

# %% cell_style="split"
type(fact)

# %% cell_style="split"
type(math)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthode = fonction attachée à un type

# %% [markdown]
# lorsqu'on appelle un méthode sur un objet,  
# la syntaxe est donc  
#
# ```python
# objet.methode(parametre)
# ```
#
# ce qui se passe c'est que
#
# * on cherche la méthode **à partir du type** de `objet`  
# * on trouve une **fonction**, et on l'appelle
# * avec en premier argument l'objet

# %% [markdown] slideshow={"slide_type": "slide"}
# ## appel de méthode illustré

# %% cell_style="split" slideshow={"slide_type": ""}
chaine = "bonjour"
chaine

# %% cell_style="split"
# la recherche de 'capitalize'
# à partir de `chaine`
# trouve une fonction rangée
# dans le type `str`

la_methode = str.capitalize
la_methode

# %% cell_style="split"
# lorsqu'on écrit ceci
chaine.capitalize()

# %% cell_style="split"
# c'est comme si on avait
# écrit
la_methode(chaine)

# %% cell_style="split"
# si on passe des arguments
chaine.center(13, '-')

# %% cell_style="split"
# ils sont ajoutés après l'objet
str.center(chaine, 13, '-')

# %% [markdown] slideshow={"slide_type": "slide"}
# ## à quoi ça sert ?
#
# par rapport à un appel de fonction, 2 avantages
#
# * la résolution du nom de la méthode se fait à l'exécution
#   * le même code se comporte différemment
#   * sur des entrées de type différents
#   * permet d'écrire du code plus générique
#
# * espaces de nom plus propres  
#   pas besoin d'inventer des noms comme `str_capitalize`
