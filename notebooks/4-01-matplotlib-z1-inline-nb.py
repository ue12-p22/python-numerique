# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -jupytext.custom_cell_magics,
#       -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
#       -language_info.file_extension, -language_info.mimetype, -toc, -vscode
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # `%matplotlib inline`

# %% [markdown]
# de la bonne utilisation de `plt.figure()`, `plt.show()` en fonction du driver `%matplotlib` - épisode 1 

# %% [markdown]
# **take home message**
#
# * c'est le mode par défaut
# * plusieurs figures dans une cellule:  
#   utiliser `plt.figure()` pour commencer une nouvelle figure  
#   plutôt que `plt.show()` pour en terminer une

# %% [markdown]
# ***

# %%
# si on ne met rien c'est comme si on faisait
# # %matplotlib inline

# %%
import matplotlib.pyplot as plt

# pour changer la taille des figures par défaut
plt.rcParams["figure.figsize"] = (4, 2)

# %% [markdown]
# ## préparation

# %%
import numpy as np

X = np.linspace(0, 2*np.pi)
Y = np.sin(X)
Y2 = np.cos(X)

# %% [markdown]
# ## un plot = une figure

# %% cell_style="split"
# dans ce mode, pas besoin de créer une figure
plt.plot(X, Y);

# %% cell_style="split"
plt.plot(X, Y2);

# %% [markdown]
# ## plusieurs courbes

# %% cell_style="split"
# et plusieurs courbes finissent 
# dans la même figure
plt.plot(X, Y)
plt.plot(X, Y2);

# %% cell_style="split"
# et si on veut mettre plusieurs
# graphiques différents
# on peut faire comme ceci
# qui fonctionne aussi avec le driver notebook
# plt.figure()     # le premier est toujours optionnel
plt.plot(X, Y)
plt.figure()
plt.plot(X, Y2);

# %% cell_style="split"
# on aurait aussi pu utiliser plt.show()
# mais ça par contre ça ne marche pas 
# avec le driver notebook
plt.plot(X, Y)
plt.show()
plt.plot(X, Y2);
# et le dernier n'est pas vraiment obligatoire
#plt.show()
