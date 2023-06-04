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
#     title: "Python-num\xE9rique - introduction"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %% [markdown] tags=["framed_cell"]
# **Note**: cette cellule doit s'afficher entourée d'un cadre  
# si ce n'est pas le cas et pour un rendu optimal, installez la librairie `nb-courselevels`  
# ```bash
# pip install nb-courselevels
# ```

# %% [markdown]
# # Python-numérique - introduction

# %% [markdown]
# ## contenu de ce notebook (sauter si déjà acquis)
#
# <br>
#
# comprendre que des objets qui semblent aussi différents qu'une matrice, une table de mesures hétérogènes, une série temporelle, une image...
#
# <br>
#
# sont en fait une même structure de données
#
# <br>
#
# que celle-ci n'existe pas en `python`
#
# <br>
#
# d'où le recours à la librairie `numpy`

# %% [markdown] tags=["framed_cell"]
# ## objectifs de Python-numérique
#
# <br>
#     
# vous êtes désormais capables de lire et d'écrire du code **python simple**
#
# <br>
#     
# vous savez le mettre en œuvre dans un **notebook**
#     
# <br>
#
# nous allons maintenant aborder le cours de **Python-numérique**
#     
# <br>
#     
# il s'agit des fonctionnalités de base de **data-science**
#     
# <br>
#     
# issues de librairies python comme `numpy`, `pandas`, `matplotlib.pyplot`...
#
#     
# <br>
#
# commençons par **importer** ces librairies dans Python
#     
# ```python
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
# ```
#     
# <br>
#     
# il peut être nécessaire de les installer avec `pip install numpy pandas matplotlib`  
# ou `!pip install numpy pandas matplotlib` dans une cellule de vos notebooks
#   
# <br>
#     
# et regarder la version de ces librairies
#     
# ```python
# np.__version__
# pd.__version__
# ```

# %%
# #!pip install numpy pandas matplotlib

# %%
# manière classique d'importer les librairies de data-science
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# %%
# vérifier les versions de ces librairies

print(f'numpy version {np.__version__}')
print(f'pandas version {pd.__version__}')

import matplotlib as mpl # la version de matplotlib
print(f'matplotlib version {mpl.__version__}')

# %% [markdown] tags=["framed_cell"]
# ## les données
# <br>
#     
# qui dit data-science dit **données**
#     
# <br>
#     
# données qui seront **manipulées** dans des programmes Python
#     
# <br>
#     
# pour les manipuler, il faut tout d'abord les **lire** et les **stocker** en mémoire
#
# <br>
#     
# en data-science on peut avoir de **très grandes quantités** de données
#
# * le stockage des données en mémoire doit être **optimisé**  
#     (en **espace mémoire** et en **temps d'accès** à cet espace mémoire)
# <br>
#     
# * afin que les calculs prennent le **moins de temps possible**
#     
#
# <br>
#     
# mais avant de parler de cela, regardons les différentes formes de données que nous voulons manipuler :

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ## différents formats de données
#
# <br>
#     
# -------------------------------------------------------- 
#    1. des **vecteurs** et **matrices** numériques classiques
#
# <img src='media/matrice.png' width=400></img>
#
# <br>
#
# -------------------------------------------------
# 2. des **tables** d'observations où
#
#    * chaque **observation** (*lignes*)...
#    
#    * ...est décrite par une ou plusieurs **mesures** (*colonnes*)
#    
#    * la première ligne indique, dans cet exemple, les noms des colonnes
#    
#      Quelles sont ces différentes **mesures** ?  
#      certaines, *SibSp* et *Parch*, sont impossibles à comprendre sans les **meta-data** de la table
#
# <img src='media/titanic.png' width="1000"></img>
#
# <br>
#    
# ---------------------------------
# 3. des **séries temporelles**
#
#    * on affiche ici les valeurs cumulées des infections au covid de janvier à août 2020 en France
#    
# <img src='media/corona-france.jpg' width="500"></img>
# https://www.data.gouv.fr/fr/datasets/coronavirus-covid19-evolution-par-pays-et-dans-le-monde-maj-quotidienne/
#  
# <br>
#     
# ----------------------------------
# 4. des images
#
# <img src='media/les-mines.jpg' width="500">
#
# <br>
#  
# ----------------------------------
# 5. des sons (musique, voix)  
#
# ----------------------------------
# 6. **etc.**

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### la matrice
# <br>
#     
# pour la matrice, on peut imaginer une représentation Python comme celle-là
#
# <br>
#     
# ```python
# matrice = [
#     [1, 2, 3, 4, 5], 
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]   
# ```
#
# <br>
#     
# mais pour transposer la sous-matrice ... c'est moins facile  
# et on ne va pas coder une fonction qui doit déjà exister !

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### table d'observations
# <br>
#     
# la table (des passagers du Titanic), est donnée dans un fichier, voici les 5 premières lignes
#    
# <br>
#
# ```
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
# 2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
# 3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
# 4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
# ...
# ```
#
# <br>
#
# que remarquez-vous ?
#
# * en première ligne - les noms des mesures (les colonnes de la table)  
#     
#     
# * puis une observation par ligne
#  
#     
# * les valeurs des mesures sont séparées par des `','`
#     
#     
# * certaines valeurs sont manquantes `',,'`
#     
#     
# * on voit des entiers, des réels (format US donc la virgule des décimales
#     est représentée par un `.`)...
#     
#     
# * ce format est donc un tableau en 2 dimensions de données hétérogènes  
# (des réels, des chaînes de caractères, des entiers...)
#     
# <br>
#
# ce format s'appelle un `CSV` pour **C**omma-**S**eparated-**V**alues   
# (fichier `titanic.csv`)

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### la série temporelle
# <br>
# <br>
#     
# pour la série, on a aussi un fichier `CSV`, `corona-par-pays.csv`
#     
# <br>
#     
# ```
# #Vous pouvez utiliser ces données sans problème
# #une référence à https://coronavirus.politologue.co sera appréciable
# Date;Pays;Infections;Deces;Guerisons;TauxDeces;TauxGuerison;TauxInfection
# 2020-08-17;Andorre;989;53;863;5.36;87.26;7.38
# 2020-08-17;Émirats Arabes Unis;64312;364;57694;0.57;89.71;9.72
# 2020-08-17;Afghanistan;37596;1375;27166;3.66;72.26;24.09
# ...
# ```
# <br>
#     
# que remarquez-vous ?
#     
# * il ressemble au précédent
#     
#     
# * on a deux lignes de commentaires (commençant par `#`)
#     
#     
# * les noms des colonnes sont dans la troisième ligne  
#     
#     
# * les deux premières mesures sont la date et le pays
# puis on voit 6 mesures reliées au covid
#     
#     
# * dans chaque ligne, on a la valeur de ces 6 mesures pour une date et un pays
#     
#     
# * les dates ont le format `year-month-day`
#     
#     
#     
# * les séparateurs sont des `';'`
#     
#
# * les réels sont en format US
#     
#     
# * ce format est aussi une table en 2 dimensions de données hétérogènes  
# (dates, identificateurs, réels...)

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### l'image
#
# <br>
#    
# pour l'image on a le fichier, en format `jpg`, `les-mines.jpg`
#     
# <br>
#     
# on sait que l'image est constituée de $533$ lignes et $800$ colonnes de pixels
#     
# <br>
#     
# et que chaque pixel est représenté par ses 3 valeurs `RGB` RedGreenBlue
#
# <br>
#     
# voici les valeurs des premiers pixels de l'image
#     
# ```python
# [[[150, 106, 33], [143, 105, 0], [ 58, 31, 4], [135, 45, 36], [229, 131, 84], [153, 158, 200]...    ]]
# ```
#     
# <br>
#        
# on devine les trois dimensions (les trois `[[[`)
#     
# <br>
#
# les valeurs des pixels RGB
#
# * ici, des entiers prenant 256 valeurs
# * $2^8$ valeurs de 0 à 255  
# * pour les stocker il suffit donc d'entiers non-signés sur 8 bits  
#   (0 est `00000000` et 255 est `11111111`)
#     
# <br>

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ## représenter ces données en mémoire
#
# ### notre problème
#
# <br>
#    
# représenter ces données dans la mémoire de l'ordinateur afin de les analyser
#     
# * ces données semblent assez différentes : matrice, tables de passagers, série temporelle, image...  
#     
# * nous souhaitons pourtant leur appliquer le même genre de fonctions
#     
# <br>
#     
# comme un `max` ou un `min`
#
# * le passager le plus agé ou le plus jeune du titanic
# * les pixels les plus clairs ou les plus foncés
# * les minima ou maxima des lignes de la matrice
#   
#   
# <br>
#     
# comme des `plot` (boxplot, histogramme,  plot 2D...)
#     
# <br>
#     
# comme de petites statistiques (moyenne, écart-type...)  
#     
# <br>
#     
# il faut leur trouver une **forme commune**

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### ces données sont des tableaux multi-dimensionnels
# <br>
#    
#     
# on a des tableaux **homogènes**
#     
# * la matrice est un tableau d'entiers, en 2 dimensions, de taille $5 \times 4$
#     
#     
# * l'image est un tableau d'entiers, en 3 dimensions, de taille $533 \times 800 \times 3$
#     
# <br>
#     
# et des tableaux **hétérogènes**
#     
# * la table des passagers du Titanic est un tableau 2D de taille $891 \times 9$
#     
#         
# * la série temporelle est un tableau 2D de taille $33342 \times 8$
#     
#
# * les colonnes sont des séries de valeurs de même type
#     
#     
# * toutes  les colonnes n'ont pas le même type

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### pas de type Python adéquat
#
# **structures de ces données ?**
#
# <br>
#     
# Python ne possède pas de type adapté à ces tableaux multi-dimensionnels 
#     
# <br>
#     
# depuis 2006, une librairie numérique `numpy` est *développée* pour cela
#     
# <br>
#
# non intégrée au core-langage Python par souci de maintenance du code
#
# <br>
#     
# elle est LA librairie numérique incontournable de Python
#     
# <br>
#
# elle étend Python avec la manipulation de tableaux multi-dimensionnels
#
# <br>
#     
# c'est une bibliothèque libre et open source
#     
# <br>
#     
# `SciPy` (ScientificPython) pour le calcul scientifique est fondée sur `numpy`

