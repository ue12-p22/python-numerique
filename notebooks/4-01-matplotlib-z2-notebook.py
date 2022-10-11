# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # `%matplotlib notebook`

# %% [markdown]
# de la bonne utilisation de `plt.figure()`, `plt.show()` en fonction du driver `%matplotlib` - épisode 2

# %% [markdown]
# **take home message**
#
# * plus pratique / interactif  
#   * on peut retailler la figure
#   * se déplacer / zoomer dans la figure
# * il **faut** appeler `plt.figure()` pour chaque figure  
# * et en ajouter d'autres `plt.figure()`  
#   pour créer plusieurs figures depuis une seule cellule
# * **attention** à `df.plot()` qui appelle automatiquement `plt.figure()` 

# %% [markdown]
# ***

# %% [markdown]
# c'est le mode que je vous recommande avec les notebooks  
# **note** dans vs-code il faut utiliser plutôt `%matplotlib pyimpl` qui ressemble assez

# %%
# %matplotlib notebook

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

# %% [markdown]
# l'apport principal de ce driver, c'est qu'on peut "naviguer" dans le graphe - zoomer et se déplacer, sauver la figure, etc... avec **la palette d'outils** située par défaut en bas; on peut cliquer sur le carré bleu en haut à droite de la figure pour la rendre 'inactive'

# %% cell_style="split"
# on peut avoir l'impression 
# que ce n'est pas la peine 
# de créer une figure, 
# car la première fois ça fonctionne
# plt.figure()     # <-- c'est mieux de prendre 
                   # l'habitude de le faire
plt.plot(X, Y);

# %% cell_style="split"
# mais en fait si on ne le fait pas
# on écrit dans la dernière figure 
# ouverte
# plt.figure()  # <-- essayez sans le mettre
plt.plot(X, Y2);

# %% [markdown]
# ## plusieurs courbes

# %% cell_style="split"
# du coup avec ce mode c'est important 
# de TOUJOURS créer une figure 
# avant d'écrire dedans
plt.figure()
plt.plot(X, Y)
plt.plot(X, Y2);

# %% cell_style="split"
# et voici comment, tout simplement
# on crée deux figures dans une cellule
plt.figure()
plt.plot(X, Y)
plt.figure()
plt.plot(X, Y2);

# %%
# alors que si on utilise un style à base de
# `plt.show()` qui marche avec le driver 'inline'
# eh bien ici ça ne fonctionne plus du tout
# car les courbes se retrouvent dans la figure du dessus !
plt.plot(X, Y)
plt.show()
plt.plot(X, 2* Y2)  # * 2 pour qu'on la voie bien
plt.show()

# %% [markdown]
# ## `pandas.plot`

# %%
import pandas as pd
df = pd.DataFrame({'sin': Y, 'cos': Y2}, index=X)

# %% [markdown]
# enfin, dernière blague, lorsqu'on affiche directement une dataframe avec `df.plot()`  
# `pandas` fait **automatiquement un appel à `plt.figure()`**  
#
# du coup il faut faire attention:  
# après tout ce qu'on vient de voir on aurait envie de faire  
# mais regardez ce que ça donne:

# %%
plt.figure()    # parce que %matplotlib notebook
                # mais en fait il ne faut pas le mettre
df.plot();

# %% [markdown]
# comme vous le voyez, le premier `plt.figure()` **est de trop**,  
# il ne faut pas le mettre
#
# <br>
#
# mais par contre avec une série ça n'est pas le cas !?!
#
# *go figure*…

# %%
plt.figure()      # ici il faut garder cet appel
df['sin'].plot();

# %% [markdown]
# ***
