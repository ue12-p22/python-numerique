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

# %% [markdown]
# 3. lors de la lecture du fichier de données `titanic.csv`  
#    1. gardez uniquement les colonnes `cols` suivantes `'PassengerId'`, `'Survived'`, `'Pclass'`, `'Name'`, `'Sex'`, `'Age'` et `'Fare'`
#
#    1. mettez la colonne `PassengerId` comme index des lignes
#    1. besoin d'aide ? faites `pd.read_csv?`

# %%
# #pd.read_csv?

# %% [markdown]
# 4. affichez le type des colonnes de la dataframe  
# en utilisant l'attribut `dtypes` des objets `pandas.DataFrame`

# %% [markdown]
# 5. sur le même graphique, et en utilisant `matplotlib.pyplot.plot`
#    1. plotez avec le paramètre `'rs'` la colonne des ages en fonctions des index  
#    (`r` pour rouge et `s` pour le style de point ici square)  
#    1. plotez avec paramètre `'b.'` et sans indiquer les abscisses, la colonne des ages
#    1. que constatez-vous ?
#    <br>
#    1. si vous n'indiquez pas l'axe des abscisses de votre dessin que choisit `plt` ? 

# %% [markdown]
# ## tri des lignes d'une dataframe

# %% [markdown]
# le but de cet exercice est d'organiser les lignes d'une dataframe suivant l'ordre d'une ou de plusieurs colonnes.
#
# utilisez la méthode `df.sort_values()`

# %% [markdown]
# 0. rechargez la dataframe

# %% [markdown]
# 1. pour créer une **nouvelle** dataframe  
# dont les lignes sont triées dans l'ordre croissant des classes des passagers  
# on veut être sûr d'avoir une nouvelle dataframe sans considération de ce que retourne la fonction `sort_values`

# %% [markdown]
# 2. pour constater qu'elles sont triées, affichez les 3 premières lignes de la dataframe  
# vous devez voir que la colonne des `Pclass` est triée  
# que les lignes ont changé de place dans la table  
# et que leur indexation a été conservée

# %% [markdown]
# 3. triez la dataframe précédente dans l'ordre des ages des passagers  
# elle doit être modifiée sans utiliser d'affectation Python  
# (on veut faire ce qu'on appelle en informatique un *tri en place*)

# %% [markdown]
# 4. constater que les lignes de la dataframe sont triées  
# en affichant les 3 premières lignes de la dataframe

# %% [markdown]
# 5. plotez la colonne des ages de la  dataframe  
# Que constatez-vous ?

# %% [markdown]
# 6. plotez la colonne dans l'ordre des ages croissants

# %% [markdown]
# ## tri des lignes *égales* au sens d'un premier critère d'une dataframe

# %% [markdown]
# 0. rechargez la dataframe

# %% [markdown]
# 1. affichez les ages des passagers d'index `673` et `746`  
# que constatez-vous ?

# %% [markdown]
# 2. utilisez le paramètre `by` de `df.sort_values()`  
# afin d'indiquer aussi une seconde colonne - par exemple `Fare`  
# pour trier les lignes identiques au sens de la première colonne  
# rangez dans une nouvelle dataframe

# %% [markdown]
# 3. sélectionnez, dans la nouvelle dataframe, la sous-dataframe dont les ages ne sont pas définis  

# %% [markdown]
# 4. combien manque-il d'ages ?

# %% [markdown]
# 5. où sont placés ces passagers dans la data-frame triée ?  
# en début (voir avec `head`) ou en fin (voir avec `tail`) de dataframe ?

# %% [markdown]
# 6. trouvez le paramètre de `sort_values()`  
# qui permet de mettre ces lignes en début de dataframe lors du tri

# %% [markdown]
# 7. produire une nouvelle dataframe en ne gardant que les ages connus,
#    et triée selon les ages, puis les prix de billet

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

# %% [markdown] {"tags": ["level_intermediate"]}
# 2. affichez la dataframe

# %% [markdown] {"tags": ["level_intermediate"]}
# 3. triez la dataframe en place dans l'ordre de la ligne d'index `trois`

# %% [markdown] {"tags": ["level_intermediate"]}
# ## tri d'une dataframe selon l'index

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# en utilisant `pandas.DataFrame.sort_index` il est possible de trier une dataframe  
# dans l'axe de ses index de ligne (ou même de colonnes)  
# utilisez le même genre de dataframe qu'à l'exercice précédent

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# 1. créez et affichez cette dataframe  
#    par contre cette fois créez des colonnes dans un ordre non alphabétique, par exemple `dbace`

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# 2. trier la dataframe par index de ligne croissant  
# et affichez la dataframe

# %% [markdown] {"tags": ["level_intermediate"], "cell_style": "center"}
# 3. triez la dataframe par index de colonne croissant

# %% [markdown]
# ***
