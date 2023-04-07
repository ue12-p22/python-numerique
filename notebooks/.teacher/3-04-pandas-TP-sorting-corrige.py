# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     cell_metadata_json: true
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
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: TP sur le tri d'une dataframe
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")

# %% [markdown]
# # TP sur le tri d'une dataframe

# %% [markdown]
# **Notions intervenant dans ce TP**
#
# * tri de `pandas.DataFrame` par ligne, par colonne et par index
#
# **N'oubliez pas d'utiliser le help en cas de problème.**

# %% [markdown]
# ## import des librairies et des données

# %% [markdown]
# 1. importez les librairies `pandas`et `numpy`

# %% [markdown]
# 2. importez la librairie `matplotlib.pyplot`  

# %%
# prune-cell
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# 3. lors de la lecture du fichier de données `titanic.csv`  
#    1. gardez uniquement les colonnes `cols` suivantes `'PassengerId'`, `'Survived'`, `'Pclass'`, `'Name'`, `'Sex'`, `'Age'` et `'Fare'`
#
#    1. mettez la colonne `PassengerId` comme index des lignes
#    1. besoin d'aide ? faites `pd.read_csv?`

# %%
# #pd.read_csv?

# %%
# prune-cell
cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('titanic.csv', index_col='PassengerId', usecols=cols)

# %% [markdown]
# 4. affichez le type des colonnes de la dataframe  
# en utilisant l'attribut `dtypes` des objets `pandas.DataFrame`

# %%
# prune-cell
print(  df.dtypes  )
df.head()

# %% [markdown]
# 5. sur le même graphique, et en utilisant `matplotlib.pyplot.plot`
#    1. plotez avec le paramètre `'rs'` la colonne des ages en fonctions des index  
#    (`r` pour rouge et `s` pour le style de point ici square)  
#    1. plotez avec paramètre `'b.'` et sans indiquer les abscisses, la colonne des ages
#    1. que constatez-vous ?
#    <br>
#    1. si vous n'indiquez pas l'axe des abscisses de votre dessin que choisit `plt` ? 

# %%
# prune-cell
plt.plot(df.index, df['Age'], 'rs');

# %%
# prune-cell
# qu'on aurait pu d'ailleurs faire aussi comme ceci
df.Age.plot(style='rs');

# %%
# prune-cell
plt.plot(df['Age'], 'b.');
# par défaut, ici on lui passe une série, et on constate que 
# plt plot avec les index en abscisse et les valeurs en ordonnée

# %% [markdown]
# ## tri des lignes d'une dataframe

# %% [markdown]
# le but de cet exercice est d'organiser les lignes d'une dataframe suivant l'ordre d'une ou de plusieurs colonnes.
#
# utilisez la méthode `df.sort_values()`

# %% [markdown]
# 0. rechargez la dataframe

# %%
# prune-cell
cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('titanic.csv', index_col='PassengerId', usecols=cols)

# %% [markdown]
# 1. pour créer une **nouvelle** dataframe  
# dont les lignes sont triées dans l'ordre croissant des classes des passagers  
# on veut être sûr d'avoir une nouvelle dataframe sans considération de ce que retourne la fonction `sort_values`

# %%
# prune-cell 1.
# on trie dans l'axe des lignes donc `axis=0`
df_sorted = df.sort_values(by='Pclass', ascending=True, axis=0).copy()

# %% [markdown]
# 2. pour constater qu'elles sont triées, affichez les 3 premières lignes de la dataframe  
# vous devez voir que la colonne des `Pclass` est triée  
# que les lignes ont changé de place dans la table  
# et que leur indexation a été conservée

# %%
# prune-cell 2.
df_sorted.head(4)

# %% [markdown]
# 3. triez la dataframe précédente dans l'ordre des ages des passagers  
# elle doit être modifiée sans utiliser d'affectation Python  
# (on veut faire ce qu'on appelle en informatique un *tri en place*)

# %%
# prune-cell 3.
# on trie en place et dans l'axe des lignes
df_sorted.sort_values(by='Age', ascending=True, axis=0, inplace=True)

# %% [markdown]
# 4. constater que les lignes de la dataframe sont triées  
# en affichant les 3 premières lignes de la dataframe

# %%
# prune-cell 4.
df_sorted.head(4)

# %% [markdown]
# 5. plotez la colonne des ages de la  dataframe  
# Que constatez-vous ?

# %%
# prune-cell 5.
plt.plot(df_sorted['Age'], 'b.');

# %% [markdown]
# 6. plotez la colonne dans l'ordre des ages croissants

# %%
# prune-cell 6.
# ici il nous faut passer nous même les X
# sinon, la série a bien été triée mais les index
# sont inchangés, et donc si on passe seulement la série
# triée à plt.plot, il affiche la même chose que plus haut
plt.plot(range(len(df_sorted)), df_sorted['Age'], 'r.');

# %% [markdown]
# ## tri des lignes *égales* au sens d'un premier critère d'une dataframe

# %% [markdown]
# 0. rechargez la dataframe

# %%
# prune-cell
cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('titanic.csv', index_col='PassengerId', usecols=cols)

# %% [markdown]
# 1. affichez les ages des passagers d'index `673` et `746`  
# que constatez-vous ?

# %%
# prune-cell 1.
df.loc[673, 'Age'], df.loc[746, 'Age']

# %% [markdown]
# 2. utilisez le paramètre `by` de `df.sort_values()`  
# afin d'indiquer aussi une seconde colonne - par exemple `Fare`  
# pour trier les lignes identiques au sens de la première colonne  
# rangez dans une nouvelle dataframe

# %%
# prune-cell 2.
df_sorted = df.sort_values(by=['Age', 'Fare'])

# %% [markdown]
# 3. sélectionnez, dans la nouvelle dataframe, la sous-dataframe dont les ages ne sont pas définis  

# %%
# prune-cell 3.
df_sorted_isna = df_sorted[df_sorted['Age'].isna()]

# %% [markdown]
# 4. combien manque-il d'ages ?

# %%
# prune-cell 4.
print(f"we have {len(df_sorted_isna)} missing ages") # nb de passagers dont l'age n'est pas connu

# %% [markdown]
# 5. où sont placés ces passagers dans la data-frame triée ?  
# en début (voir avec `head`) ou en fin (voir avec `tail`) de dataframe ?

# %%
# prune-cell 5.
# en fin
df_sorted.tail()

# %% [markdown]
# 6. trouvez le paramètre de `sort_values()`  
# qui permet de mettre ces lignes en début de dataframe lors du tri

# %%
# prune-cell 6.
df_sorted.sort_values(by='Age', ascending=True, axis=0, na_position='first').head()

# %% [markdown]
# 7. produire une nouvelle dataframe en ne gardant que les ages connus,
#    et triée selon les ages, puis les prix de billet

# %%
# prune-cell 7.
df[df.Age.notna()].sort_values(by=['Age', 'Fare'])

# %% [markdown] {"tags": ["level_intermediate"]}
# ## tri (des colonnes) d'une dataframe selon une ligne

# %% [markdown] {"tags": ["level_intermediate"]}
# en utilisant `pandas.DataFrame.sort_values` il est possible de trier une dataframe  
# dans l'axe de ses colonnes

# %% [markdown] {"tags": ["level_intermediate"]}
# 1. créez une dataframe de 4 lignes et 5 colonnes de valeurs entières aléatoires entre 0 et 100  
#    mettez comme index (par exemple):  
#    aux lignes  `'un'`, `'deux'`, `'trois'` et `'quatre'`  
#    aux colonnes `'a'`, `'b'`, `'c'`, `'d'` et `'e'`  
#    **indice**: voyez la documentation de `pd.DataFrame` 
#    pour construire une dataframe  
#    par programme

# %% {"tags": ["level_intermediate"]}
# prune-cell
df = pd.DataFrame(np.random.randint(0, 100, 20).reshape(4, 5),
                  columns=['a', 'b', 'c', 'd', 'e'],
                  index=['un', 'deux', 'trois', 'quatre'])

# %% [markdown] {"tags": ["level_intermediate"]}
# 2. affichez la dataframe

# %% {"tags": ["level_intermediate"]}
df

# %% [markdown] {"tags": ["level_intermediate"]}
# 3. triez la dataframe en place dans l'ordre de la ligne d'index `trois`

# %% {"tags": ["level_intermediate"]}
# prune-cell
df.sort_values(by='trois', ascending=True, axis=1)

# %% [markdown] {"tags": ["level_intermediate"]}
# ## tri d'une dataframe selon l'index

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# en utilisant `pandas.DataFrame.sort_index` il est possible de trier une dataframe  
# dans l'axe de ses index de ligne (ou même de colonnes)  
# utilisez le même genre de dataframe qu'à l'exercice précédent

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# 1. créez et affichez cette dataframe  
#    par contre cette fois créez des colonnes dans un ordre non alphabétique, par exemple `dbace`

# %% {"tags": ["level_intermediate"]}
# prune-cell
df = pd.DataFrame(np.random.randint(0, 100, 20).reshape(4, 5),
                  columns=list('dbace'),
                  index = ['un', 'deux', 'trois', 'quatre'])
print(df)

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# 2. trier la dataframe par index de ligne croissant  
# et affichez la dataframe

# %% {"tags": ["level_intermediate"]}
# prune-cell
print(df.sort_index(axis=0))

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# 3. triez la dataframe par index de colonne croissant

# %% {"tags": ["level_intermediate"]}
# prune-cell
# pas de changement visible car les colonnes sont déjà triées...
print(df.sort_index(axis=1))

# %% [markdown]
# ***
