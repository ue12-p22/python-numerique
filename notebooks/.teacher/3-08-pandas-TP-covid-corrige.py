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
#     title: "TP sur les donn\xE9es coronavirus"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import IPython

# %% [markdown]
# # TP sur les données coronavirus

# %% [markdown] tags=["framed_cell"]
# ## les données de Johns Hopkins
#
# <br>
#
# les données sur le corona virus
#
# * sont publiées par le département *Center for Systems Science and Engineering* (CSSE)
# * de l'Université Johns Hopkins
# * sur le dépôt github <https://github.com/CSSEGISandData/COVID-19>
# * dans un format brut, détaillé et touffu  
#   (un peu trop compliqué pour l'utiliser ici)

# %%
# le repo github
official_url = "https://github.com/CSSEGISandData/COVID-19"

# %% [markdown] tags=["framed_cell"]
# ## autre jeu de donnée intéressant
#
# <br>
#
# un dépôt de *seconde main* <https://github.com/pomber/covid19>
#
# * consolide les données du CSSE
# * en un unique fichier `timeseries.json`
# * mis à jour quotidiennement
# * le fichier est en format `json`(JavaScript Object Notation)

# %%
# le repo avec le fichier json
json_url = "https://pomber.github.io/covid19/timeseries.json"

# %% [markdown] tags=["framed_cell"]
# ## le format `json`
#
# <br>
#
# nous avons vu le `csv`
#
# * un format de données très simple décrivant une table
# * les éléments séparés par un caractère (`,` ou `;`...)
# * pouvant contenir des identificateurs, des chaînes de caractères et des nombres
#
# <br>
#
# `json` est un format de données bien plus structuré avec
#
# * object (`dict`), `list`, nombre, `str` (with " only), `false`,  `true`, `null`
# * les `list` sont les tableaux python
# * les `dict` sont les dictionnaires `Python`  
#   permettant de décrire des objets `{attribut1:valeur1, attribut2:valeur2,...}`
#
# <br>
#
# par exemple, la liste des animaux avec leur vitesse et leur longévité sera, en `json`
#
# ```python
# [
#     {"name":"snail",    "speed":0.1,  "lifespan":2.0},
#     {"name":"pig",      "speed":17.5, "lifespan":8.0},
#     {"name":"elephant", "speed":40.0, "lifespan":70.0},
#     {"name":"rabbit",   "speed":48.0, "lifespan":1.5},
#     {"name":"giraffe",  "speed":52.0, "lifespan":25.0},
#     {"name":"coyote",   "speed":69.0, "lifespan":12.0},
#     {"name":"horse",    "speed":88.0, "lifespan":28.0}
#  ]
# ```
#
# ou sous une autre forme, toujours en `json`
#
# ```python
# {"speed":
#      {"snail":0.1,
#       "pig":17.5,
#       "elephant":40.0,
#       "rabbit":48.0,
#       "giraffe":52.0,
#       "coyote":69.0,
#       "horse":88.0},
#   "lifespan":
#       {"snail":2.0,
#        "pig":8.0,
#        "elephant":70.0,
#        "rabbit":1.5,
#        "giraffe":25.0,
#        "coyote":12.0,
#        "horse":28.0}
# }
# ```

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ## format `json` pour le covid
#
# <br>
#
# le fichier https://pomber.github.io/covid19/timeseries.json contient un objet `dict` dont
#
# * les clés sont les pays du monde
# * chaque valeur est une liste de `dict`  
#   chacun décrivant **une** mesure de covid avec les 4 clés: `date`, `confirmed`, `deaths` et `recovered`
#
# ```python
# {
#   "Afghanistan": [
#     {
#       "date": "2020-1-22",
#       "confirmed": 0,
#       "deaths": 0,
#       "recovered": 0
#     },
#     {
#       "date": "2020-1-23",
#       "confirmed": 0,
#       "deaths": 0,
#       "recovered": 0
#     },
#     {
#       "date": "2020-1-24",
#       "confirmed": 0,
#       "deaths": 0,
#       "recovered": 0
#     }, ...
# ```

# %% [markdown]
# ## récupération des données `json` du covid

# %% [markdown] tags=["framed_cell"]
# ### récupération avec `requests`
#
# <br>
#
# le module `requests` permet de *récupérer* des fichiers sur Internet  
# utiliser cette approche permet de toujours avoir des **données récentes**  
# **mais** demande une bonne connexion à Internet  
# sinon allez à la slide (l'encadré) suivante qui utilise des données figées
#
# <br>
#
# `requests` n'est pas dans la librairie standard  
# il faut donc l'installer comme d'habitude avec `pip`  
# (on fait comment déjà ?)
#
# <br>
#
# une fois que c'est fait on peut l'importer
#
# ```python
# import requests
# ```
#
# <br>
#
# avec la fonction `requests.get` on envoie la *requête* d'une URL  
# et on reçoit une réponse  
# **attention** la requête suivante (`requests.get`) demande une bonne connexion  
# ou beaucoup de patience...
#
# ```python
# json_url = "https://pomber.github.io/covid19/timeseries.json"
# response = requests.get(json_url)
# ```
#
# <br>
#
# on peut vérifier que l'échange s'est bien passé
#
# ```python
# response.ok
# -> True
# ```
#
# <br>
#
# la méthode `json()` sur l'objet `Response` décode le format JSON  
# et renvoie les données prêtes pour des traitements en Python  
#
# ```python
# by_country = response.json()
# ```
#
# <br>
#
# on voit bien une structure Python de **`dict`** et de `list`  
# correspondant au contenu du fichier `json` vu ci-dessus
#
# ```python
# by_country
# -> {'Afghanistan': [
#       {'date': '2020-1-22', 'confirmed': 0, 'deaths': 0,'recovered': 0},
#       {'date': '2020-1-23', 'confirmed': 0, 'deaths': 0, 'recovered': 0},
#       {'date': '2020-1-24', 'confirmed': 0, 'deaths': 0, 'recovered': 0},
#     ...
# ```
#
# <br>
#
# si votre connexion ne vous permet pas la requête  
# voir la prochaine cellule de cours

# %%
# pensez à bien installer le module requests

import requests
json_url = "https://pomber.github.io/covid19/timeseries.json"
by_country = None

# %%
# mettez cette variable à True si vous avez une bonne connexion
good_connection = False
#good_connection = True

# %%
# le code UNIQUEMENT SI VOUS AVEZ UNE BONNE CONNEXION INTERNET

if good_connection:
    response = requests.get(json_url)
    print(response.ok)

    by_country = response.json()

    print(type(by_country))

else:
    print('pas bonne connexion - pas grave...')

# %% [markdown] tags=["framed_cell"]
# ### chargement avec lib `json`
#
# <br>
#
# si l'accès Internet n'est pas possible, nous exposons une copie des données  
# faite il y a quelque temps, dans le fichier `covid-frozen.json`
#
# <br>
#
# le module `json` de la librairie standard permet de *lire* des fichiers en format json  
# on l'importe
#
# ```python
# import json
# ```
#
# <br>
#
# après avoir ouvert un fichier en lecture en `python`  
# la fonction `json.load` lit le contenu dans un objet `python`
#
# ```python
# json_file = 'covid-frozen.json'
#
# with open(json_file) as f:
#     by_country = json.load(f)
# ```
#
# <br>
#
# on a une structure Python de `dict` et de `list`
#
# ```python
# by_country
# -> {'Afghanistan': [
#       {'date': '2020-1-22', 'confirmed': 0, 'deaths': 0, 'recovered': 0},
#       {'date': '2020-1-23', 'confirmed': 0, 'deaths': 0, 'recovered': 0},
#       {'date': '2020-1-24', 'confirmed': 0, 'deaths': 0, 'recovered': 0},
#     ...
# ```

# %%
if by_country is not None:
    print('on utilise les données déjà chargées')
else:
    import json
    json_file = 'covid-frozen.json'

    with open(json_file) as f:
        by_country = json.load(f)

    print(type(by_country))


# %%
# regardons un peu la première clé de ce dictionnaire

# les 4 premières clés
list(by_country.keys())[:4]

# %% [markdown]
# ## dataframe globale - données covid *monde*

# %% [markdown] tags=["framed_cell"]
# ### exercice (version avancé)
#
# il s'agit de construire une **unique** dataframe contenant toutes les données covid *monde*  
# à partir de l'objet python `by_country`
#
# vous devez obtenir quelque chose comme cela
#
# ```python
#           date  confirmed  deaths  recovered      country
# 0    2020-1-22          0       0          0  Afghanistan
# 1    2020-1-23          0       0          0  Afghanistan
# 2    2020-1-24          0       0          0  Afghanistan
# 3    2020-1-25          0       0          0  Afghanistan
# 4    2020-1-26          0       0          0  Afghanistan
# ..         ...        ...     ...        ...          ...
# ???  2021-8-29     124437    4401          0     Zimbabwe
# ???  2021-8-30     124581    4416          0     Zimbabwe
# ???  2021-8-31     124773    4419          0     Zimbabwe
# ???   2021-9-1     124960    4438          0     Zimbabwe
# ???   2021-9-2     125118    4449          0     Zimbabwe
#
# [115050 rows x 5 columns]
# ```
#
# **attention**
#
# * les `???` peuvent être différents suivant ce que vous faites
# * `115050` dépend de la date à laquelle le fichier a été récupéré  
#   (et de combien de données étaient alors disponibles)
#
# **indications**
#
# * les élèves avancés peuvent travailler sans indications supplémentaires
# * pour les autres élèves, la cellule suivante vous propose une méthode pas-à-pas

# %%
# votre code
# rangez votre résultat dans la variable global_df

# global_df = ...

# %%
# prune-cell
all_dfs = []
for country, records in by_country.items():
    df = pd.DataFrame(records)
    df['country'] = country
    all_dfs.append(df)

global_df = pd.concat(all_dfs)
global_df.shape

# %%
# prune-cell
global_df.head()

# %%
# prune-cell
global_df.tail()

# %%
# prune-cell
# on peut essayer de tirer profit de pd.concat(keys=)

# on fabrique une df par pays et on met tout dans une liste
country_dfs = [pd.DataFrame(records) for records in by_country.values()]
# qu'on peut passer à concat
global_df1 = pd.concat(country_dfs, keys=by_country.keys())

# mais ça met le pays dans l'index, donc la suite ne fonctionnerait
# plus exactement pareil

global_df1.head()

# %% [markdown] tags=["framed_cell"]
# ### exercice (méthode pas-à-pas)
#
# **exercice (méthode pas-à-pas)** de construction de la dataframe globale
#
# nous allons commencer par créer les dataframes de 2 pays `'France'` et `'Italy'`  
# puis les concaténer en une unique dataframe globale  
# et ensuite généraliser à tous les pays
#
# **rappel** l'objet Python `by_country` est un `dict` dont:
#
# * les clés `keys()` sont les noms des pays
# * les valeurs `values()` sont des séries temporelles (`list`) d'observations sur le covid  
# * chaque observation est un objet exprimé sous la forme d'un `dict`  
#   avec 4 mesures indiquées par les attributs `'date'`, `'confirmed'`, `'deaths'` et `'recovered'`  
#   en `2021-8-31` au `Zimbabwe` on a `124773` cas confirmés, `4419` morts et `0` guéris
# 1. prenez la clé `'France'`  
# construisez la dataframe à partie de la valeur de cette clé  
# (la liste des enregistrements temporels de cas de covid)
# <br>
#
# 1. quelles sont les colonnes de cette dataframe ?  
# combien y-a-t-il d'entrées (de mesures différentes)
# <br>
#
# 1. vous remarquez que cette dataframe ne contient plus l'information sur le pays  
# ajoutez à cette dataframe une colonne de nom `'country'` contenant `'France'` à chaque ligne
# <br>
#
# 1. faites de même avec la clé `'Italy'`  
# et utilisez la fonction `pandas.concat` pour concaténer les deux dataframes
# <br>
#
# 1. généralisez et construisez une dataframe avec tous les pays  
# vous devez utiliser un `for` python

# %%
# votre code

# %%
# prune-cell France et Italy

country_dfs = []

# 1.
country = 'France'
df = pd.DataFrame(by_country[country])

# 2.
print('columns (1)', df.columns)

# 3.
df['country'] = country
print('columns (2)', df.columns)
print('shape for France', df.shape)
country_dfs.append(df)

# 4. 
country = 'Italy'
df = pd.DataFrame(by_country[country])
df['country'] = country
print('shape for Italy', df.shape)
country_dfs.append(df)
df_fr_it = pd.concat(country_dfs)
print('shape for france+italy', df_fr_it.shape)

# 5.
country_dfs = []

for country, records in by_country.items():
    country_df = pd.DataFrame(records)
    country_df['country'] = country
    country_dfs.append(country_df)
    
global_df2 = pd.concat(country_dfs)
print('global shape', global_df2.shape)

# %%
# prune-cell où on vérifie l'égalité des deux méthodes
np.all(global_df == global_df2) # si True, les 2 dataframes sont identiques

# %% [markdown]
# ***

# %% [markdown]
# ## index de la dataframe globale

# %% [markdown]
# ### les index ne sont pas forcément uniques
#
# si vous avez appelé `pd.concat()` sans paramètre particulier  
# vous pouvez sans doute observer ceci:

# %% tags=["raises-exception"]
# si on essaie d'accéder à la ligne d'index 0
# on remarque qu'en fait on obtient .. plein de lignes
global_df.loc[0]

# %% [markdown] tags=["framed_cell"]
# **les index ne sont pas toujours uniques** 
#
# <br>
#
# ce qui s'est passé c'est que :  
# chacune de nos dataframe par pays a été construite à partir d'un index **séquentiel**  
# i.e. un `RangeIndex` qui commence à chaque fois à 0  
# et lors du `concat` on a conservé ces valeurs  
# ce qui crée une multitude de lignes indexées par 0 (un par pays) 
#
# <br>
#
# c'est un trait de `pandas`  
# contrairement aux dictionnaires Python - où une clé est forcément unique  
# il est possible de **dupliquer plusieurs entrées dans les index**  
# ligne ou colonne - d'une dataframe
#
# <br>
#
# même si ça n'est en général pas souhaitable  
# c'est souvent commode de pouvoir le faire  
# pendant la phase de construction / mise au point de la dataframe  
# quitte à adopter par la suite un index plus approprié  
# (comme on va le faire bientôt)

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ## les dates

# %% [markdown] tags=["framed_cell"]
# ### les dates en `pandas`
#
# <br>
#
# si les valeurs des dates sont de simples `str` - chaînes de caractères  
# vous ne pourrez pas leur appliquer de fonctionnalités spécifiques aux dates
#
# <br>
#
# la fonction `pandas.to_datetime` permet de transformer  
# une chaîne de caratères contenant une date en un objet de type date
#
# <br>
#
# ```python
# d = pd.to_datetime('2020-12-22')
# ```
#
# sur lequel vous pouvez appliquer des fonctions spécifiques aux dates
#
# ```python
# d.year # 2020
# d.month # 12
# d.day # 22
# ```

# %%
# le code
d = pd.to_datetime('2020-12-22')
print(d.year,  # 2020
      d.month, # 12
      d.day)   # 22

# %% [markdown] tags=["framed_cell"]
# ### les formats de dates en `pandas`
#
# <br>
#
# sans indications précises, `pandas` a inféré le format de la date  
# `'2020-1-2'` sera-il ainsi le 2 janvier  
# et non le premier février
#
# <br>
#
# il est beaucoup plus sûr de passer à `pandas.to_datetime`  
# le format de vos dates
#
# <br>
#
# en utilisant `'%Y'` pour l'année, `%m` pour le mois et `'%d'` pour le jour  
# on exprime le format des dates dans une chaîne de caractères
#
# <br>
#
# `'2020-1-2'` avec le format `'%Y-%m-%d'` donnera le 2 janvier 2020  
# `'2020-1-2'` avec le format `'%Y-%d-%m'` donnera le 1 février 2020  
#
# <br>
#
# ```python
# pd.to_datetime('2020-1-2', format='%Y-%d-%m').day
#     -> 1
# ```

# %%
# sans indication ça peut être ambigu
pd.to_datetime('2020-1-2').day

# %%
# c'est parfois nécessaire de bien préciser le format
pd.to_datetime('2020-1-2', format='%Y-%d-%m').day

# %%
# mais sinon c'est très flexible 
pd.to_datetime('15 july 2021'), pd.to_datetime('aug 2021'), pd.to_datetime('2021')

# %%
# mais c'est très flexible 
pd.to_datetime('15 july 2021 08:00')

# %% [markdown] tags=["framed_cell"]
# ### convertissons nos dates
#
# <br>
#
# reprenons à partir de la dataframe globale
#
# 1. quel est le type des colonnes ?
# 1. que pensez-vous du type de la `'date'` ?  
#    pensez-vous que ce soit adapté pour trier ?  
#    même question pour calculer la durée entre 2 événements ?  
#    comment pourrait-on s'y prendre pour améliorer ça ?
#
# 1. regardez la fonction `pandas.to_datetime`  
#    sachant que l'année s'écrit `%Y`, le mois `%m` et le jour `%d`  
#    écrivez le format qui décrirait une date comme `'2020-1-22'`
#
# 1. créez une nouvelle `Series` déduite de la colonne `date`  
#    et qui utilise un type plus adapté aux calculs sur les dates
#    quel est le type de la nouvelle colonne ?
#    
# 1. remplacez dans la dataframe globale la colonne `date` par la précédente  
#    (le mieux est sans doute de conserver le même nom, mais ce n'est pas indispensable)

# %%
# votre code

# %%
# prune-cell

# 1. et 2.
print(global_df.dtypes)

global_df.date.dtype

# %%
# prune-cell

# 3. 
format = '%Y-%m-%d'

# 4.
proper_date = pd.to_datetime(df['date'], format=format)
# le type est np.datetime64
proper_date

# %%
# prune-cell 5.
global_df['date'] = proper_date
global_df.dtypes

# %% [markdown] tags=["framed_cell"]
# ## un index plus idoine
#
# à présent on va pouvoir choisir un index un peu plus adapté à nos données
#
# 1. nous avons vu la notion de *MultiIndex*  
#    quel serait d'aprés vous un bon choix pour indexer la dataframe globale ?
# 1. voyez-vous un moyen d'utiliser `pivot_table()` pour construire une nouvelle  
#    dataframe qui contienne essentiellement les mêmes informations  
#    mais avec un multi-index qui soit pertinent dans le contexte  
#    **variante** on peut aussi utiliser `set_index()`  
#    pour aboutir au même résultat
#    

# %%
# votre code

# %%
# prune-cell

# 1.
# on veut utiliser comme index un couple
# (country, date)
# de cette façon on aura bien unicité de l'index
# et les valeurs restant dans la dataframe (hors index)
# sont les 3 grandeurs qui nous intéressent:
# confirmed, deaths et recovered

# 2. 
clean_df = global_df.pivot_table(
    values=['confirmed', 'deaths', 'recovered'],
    index=['country', 'date'],
    # on a déjà choisi plusieurs valeurs,
    # si on choisissant aussi plusieurs colonnes
    # on aurait un multiindex, ce n'est pas ce qu'on veut
    columns=[],
)

clean_df

# %%
# prune-cell 2. (avec set_index)
clean_df = global_df.set_index(['country', 'date'])
# NB qu'on aurait pu passer à set_index le paramètre inplace=True
clean_df

# %% [markdown] tags=["framed_cell"]
# ### accéder via un *MultiIndex*
#
# 1. extrayez de la dataframe la série des 3 mesures  
#    faites en France le 1er Janvier 2021
# 1. (avancé - pas vu en cours)  
#    essayez de trouver/deviner comment extraire de
#    cette dataframe toutes les données relatives à la France
# 1. même question pour la France et l'Italie

# %%
# prune-cell 1.
clean_df.loc[('France', '1 jan 2021')]

# %%
# prune-cell 2.
clean_df.loc['France']

# %%
# prune-cell 3.
clean_df.loc[['France', 'Italy']]

# %% [markdown] tags=["framed_cell", "level_intermediate"]
# ### un exemple de slicing (très) avancé
#
# <br>
#
# pour illustrer la puissance de pandas, et la pertinence de notre choix d'index  
# voyons comment utiliser du **slicing** (*très très avancé*)  
# pour extraire cette fois les données relatives à
#
# * deux pays au hasard - disons `France` et `Italy`
# * à la période 1er Juillet - 15 Août 2021 inclus
#
# <br>
#
# pour ça on va tirer profit de la structure de l'index  
# et aussi de la puissance du type `datetime64`
#
# <br>
#
# on va fabriquer :
#
# * `countries`: une liste de pays - c'est facile
# * `time_slice`: un slice sur le temps  
#   qui en temps normal pourrait s'écrire `'july 2021' : '15 august 2021'`  
#   (bornes inclusives puisque .loc[])
#
# * un slice sur les colonnes  
#   mais au fait on les veut toutes, on peut utiliser `:` 
#   
# <br>
#
# l'idée serait ensuite d'écrire simplement
#
# ```python
# clean_df.loc [ (countries, time_slice), :]
# ```
#
# <br>
#
# tout ça fonctionne très bien, sauf pour la création de `time_slice`  
# qui, pour de sombres raisons de syntaxe, ne peut pas se faire ici  
# avec la notation `start:stop` (parce que pas dans des `[]`)  
# du coup on utilise la fonction *builtin* `slice()` pour créer `time_slice`

# %% tags=["level_intermediate", "raises-exception"]
# ce qui nous donne le code suivant
# plutôt subtil, mais vraiment puissant

### pour slicer sur les deux composantes de l'index

# NB: si on voulait tous les pays on pourrait faire
# countries = slice(None)
# qui est équivalent à utiliser :: 
# sauf qu'à nouveau ce n'est pas possible syntaxiquement ici
countries = ['France', 'Italy']
time_slice = slice('july 2021', '15 aug 2021')

clean_df.loc[
    # les lignes: c'est un 2-index donc on peut passer 2 slices
    (countries, time_slice),
    # les colonnes: on les veut toutes
    :]

# %% [markdown]
# ***

# %% [markdown]
# ## dessinons

# %% [markdown] tags=["framed_cell"]
# ### plot d'une dataframe
#
# <br>
#
# plutôt que d'utiliser directement la mécanique de `matplotlib.pyplot`  
# ce qui a tendance à être fastidieux  
# il est préférable d'utiliser les méthodes comme `plot()`  
# mais **directement** sur la dataframe
#
# <br>
#
# la logique est alors de dessiner autant de courbes que de colonnes  
# et de plus pandas se charge de tous les labels  
# bref c'est recommandé

# %%
# illustration
# 3 colonnes donc 3 courbes
# 4 lignes donc 4 points sur chaque courbe
df = pd.DataFrame(
    {'a': [0, 10, 20, 30], 'b': [5, 10, 15, 25], 'c': [30, 15, 5, 0]},
    index = ['early', 'before', 'now', 'predicted'],
)
df

# %%
df.plot();

# %% [markdown] tags=["framed_cell"]
# ### sur un pays
#
# <br>
#
# du coup on a souvent seulement besoin de **mettre en forme** les données pour  
# qu'elles puissent être directement plottées par cet algorithme simple
#
# <br>
#
# imaginons que dans notre cas on veuille comparer sur un graphique  
# l'évolution d'une ou plusieurs des 3 mesures  
# (`deaths`, `confirmed` et `recovered`) entre plusieurs pays  
#
# <br>
#
# disons par exemple les mesures `deaths` et `confirmed`  
# entre `France`, `Italy` et `Germany`  
# il nous faut donc construire une dataframe qui a  
# six colonnes - le produit cartésien des 2 mesures et 3 pays  
# et autant de lignes que de dates - indexé par les dates  
#
# <br>
#
# mais avant de réfléchir à comment faire ça, 
# commençons par le cas simple d'un seul pays, au moins  
# pour valider l'idée générale
#
# 1. affichez sur un graphique les 3 mesures pour la France au cours du temps
# 1. idem avec seulement 2 mesures `deaths` et `confirmed` 
#

# %%
# votre code

# %%
# prune-cell 1.
# pas forcément super pertinent de comparer 
# les 3 mesures sur un même graphique mais 
# l'idée générale semble fonctionner

clean_df.loc['France'].plot();

# %%
# prune-cell 2.
clean_df.loc['France', ['deaths', 'confirmed']].plot();

# %% [markdown] tags=["framed_cell"]
# ### plusieurs pays
#
# <br>
#
# il nous reste maintenant à traiter le cas de plusieurs pays
#
# <br>
#
# 1. extrayez les données pour les 2 mesures et les 3 pays (appelons là `df3`)
# 1. essayez de plotter la dataframe (je vous signale le paramètre `rot=45`  
#    qu'on peut passer à `df.plot()` pour améliorer la lisibilité)  
#     qu'est ce qui ne va pas malgré cela ?

# %%
# votre code

# %%
# prune-cell
df3 = clean_df.loc[['France', 'Italy', 'Germany'], ['deaths', 'confirmed']]
df3.plot(rot=45);

# %% [markdown] tags=["framed_cell"]
# ### mise en forme des données 
#
# <br>
#
# quelle est la forme de `df3` ?  
# à ce stade vous devriez avoir 2 colonnes,  
# et en gros 3 fois plus de lignes que dans un pays
#
# <br>
#
# alors qu'on avait dit qu'on voulait 6 colonnes, et autant 
# de lignes que dans un pays (autant que de jours de mesure)
#
# <br>
#
# pour obtenir cette forme (qui bien sûr contient toujours autant de données)  
# on veut faire un découpage qui ressemble à ceci
#
# <img src="media/unstacking.png" width="400px">

# %% [markdown]
# ***

# %% [markdown] tags=["framed_cell"]
# ### `df.unstack()`
#
# <br>
#
# c'est justement le propos de la méthode `unstack()` sur la dataframe  
# qui fonctionne en déplaçant un niveau d'index  
# de l'index des lignes vers l'index des colonnes
#
# <br>
#
# dans notre cas précis nous avons  
# . **en lignes** un multi-index à deux niveaux `country` et `date`  
# . et **en colonnes** un index simple (un niveau) de 2 colonnes
#
# <br>
#
# et nous pourrions obtenir ce qu'on cherche si on pouvait  
# en quelque sorte "faire passer" le niveau d'index `country`  
# de la direction des lignes à celle des colonnes  
#
# <br>
#
# comme le niveau d'index `country` est le premier  
# donc d'indice 0, on va appeller
#
# ```python
# df3.unstack(0)
# ```
#
# <br>
#
# et vous pouvez constater que nous avons à présent  
# . **en lignes** un seul niveau d'index - les dates  
# . **en colonnes** deux niveaux, les 2 mesures x les 3 pays

# %% tags=["raises-exception"]
# le code

df6 = df3.unstack(0)
df6


# %% [markdown]
# ### ne reste qu'à plotter

# %% tags=["raises-exception"]
# que du coup il n'y a plus qu'à plotter
df6.plot(figsize=(12, 5));

# %% [markdown] tags=["level_intermediate", "framed_cell"]
# ### extra
#
# les rapides peuvent écrire une fonction `extract()` qui prend en paramètres 
#
# * les pays concernés
# * les mesures concernées
# * et en option pour les plus forts, les dates de début et de fin
#
# et qui retourne une dataframe prête à être affichée comme on l'a fait plus haut
