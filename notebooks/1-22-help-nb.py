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
#     title: obtenir de l'aide
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # obtenir de l'aide

# %% [markdown]
# ## invoquer le help

# %% [markdown]
# ## help des notebook

# %% [markdown]
# taper, dans une cellule de code, le symbole sur lequel vous voulez avoir de l'aide suivi de `?`
#
# ```python
# Entrée [ ]: int?
# ```
#    
#    
#    
# Une fenêre contenant le help apparaît en bas de votre notebook

# %%
# décommenter pour tester
# # int?

# %% [markdown]
# ## help de Python

# %% [markdown]
# dans le code Python, appeler la fonction `help`
#
#
# * avec un nom en argument `help(int)`, vous obtenez la documentation sur ce nom  
#   ce nom peut être une chaîne `help('if')` 
#
#
# * sans argument `help()`  
#   un utilitaire vous permet d'afficher la documentation des noms que vous entrez

# %%
# décommenter pour tester
# help(help)

# %%
# décommenter pour tester
#help()

# %%
# décommenter pour tester
#help('if')

# %% [markdown]
# ## écrire des messages de help

# %% [markdown]
# une `docstring` est la chaîne de caractère  
# qui apparaît comme première instruction d'une définition  
# (de module, de fonction, de classe ou de méthode de classe)
#
#
# la `docstring` est rangée dans l'attribut `__doc__` des objets
#
# tous vos fonctions, classes, méthodes et modules devraient avoir des docstrings
#
#
# il est conseillé d'utilisez les `"""triple guillemets"""` autour des docstrings 

# %% [markdown]
# exemple: voici un fichier python `foobar.py`  
# remarquez où on a mis la documentation

# %%
# !cat foobar.py

# %% tags=["raises-exception"]
# décommenter pour tester plus de cas

import foobar
       
#help(foobar)
#print(foobar.__doc__)

#help(foobar.foo)
#help(foobar.Bar)

b = foobar.Bar()
help(b)
