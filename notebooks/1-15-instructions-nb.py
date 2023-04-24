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
#     title: instructions
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # instructions

# %% [markdown]
# Certaines de ces instructions seront décrites dans le notebook sur les itérations.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le branchement `if`

# %% [markdown] cell_style="split"
# forme générale
#
# ```python
# if exp1:
#     ...
#     ...
# elif exp2:
#     ...
#     ...
# else:
#     ...
#     ...
# ```

# %% cell_style="split"
note = 14
appreciation = None

if note >= 16:
    appreciation = 'félicitations'
elif note >= 10:
    appreciation = 'reçu'
else:
    appreciation = 'recalé'

# %%
appreciation

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ## la boucle `while`
#
# forme générale  
#
# ```python
# while exp:
#     ...
#     ...
# ```

# %% cell_style="split"
n = 132
log = 0

while n >= 1:
    log = log + 1
    n = n // 2

# %% cell_style="split"
log

# %% [markdown]
# ## `for`, `break` et `continue`

# %% [markdown]
# voir le notebook sur les `iterations`

# %% [markdown]
# ## `try`, `raise` et `except`

# %% [markdown]
# voir le notebook sur les `fonctions`
