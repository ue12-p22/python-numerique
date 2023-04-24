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
#     title: "Python : g\xE9n\xE9ralit\xE9s"
#   rise:
#     autolaunch: false
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # Python : environnement
#
# ce notebook reprend très rapidement quelques informations  
# issues de la partie initiale de ce cours `intro & install`  
# pour être sûr que vous avez tout ce qu'il faut pour travailler

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ## lancer Python
#
# 1. exécuter un programme déjà fait  
#   `$ python monprogramme.py`
# 1. lancer un interpréteur interactif  
#   `$ python`  
#   ou encore mieux  
#   `$ ipython`
# 1. mode 'mixte' dans des notebooks  
#   `$ jupyter notebook`

# %% [markdown] cell_style="split"
# **illustration**
#
# ces usages ont été vus dans le cours d'introduction, et [dans la vidéo associée](https://youtu.be/i_ZcP7iNw-U)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## nos cas d'usage

# %% [markdown] slideshow={"slide_type": ""}
# vous reconnaissez les programmes impliqués dans les différents scénarios:
#
# * le `terminal`: la façon la plus simple de lancer d'autres programmes
# * l'interpréteur `Python` : le programme qui exécute du code Python
# * interpréteur `IPython` : une surcouche qui ajoute de la souplesse
#   * complétion, aide en ligne, déplacement/édition dans l'historique
# * les notebooks `jupyter`: nos petits cahiers cours/exercices

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sachez à qui vous parlez

# %% [markdown]
# **convention**
#
# lorsque c'est ambigu, on préfixera :
#
# * la commande à taper dans un terminal, avec un `$`
#
# ```bash
#     $ python
# ```
#
# * la commande à taper dans un interpréteur Python, avec `>>>`
#
# ```python
# >>> a = 100
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## note historique
#
# Python2 est une version plus ancienne du langage
#
# * elle **n'est pas compatible** et il ne **faut surtout surtout surtout pas** l'utiliser
# * sa fin de vie est prévue en Janvier 2020 (plus du tout de support)
# * ce qui achève une période de transition de 10 ans...

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# * pendant la période transitoire les deux ont coexisté
# * d'où les commandes `python2` et `python3` qu'on rencontre parfois
# * pour lancer Python3
#   * sur certains systèmes on tape encore `python3`
#   * mais de plus en plus `python` tout court suffit
