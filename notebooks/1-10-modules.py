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
#     title: modules
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
# # modules

# %% [markdown] slideshow={"slide_type": "slide"}
# ## bibliothèque standard
#
# un grand nombre d'outils installés d'office  
# pour des tâches très variées
# [voir liste complète](https://docs.python.org/3/library/#the-python-standard-library)  
#
#
# cette boite à outils est exposée au travers de **modules**  
# que l'on peut charger dans son appli grâce au mot-clé `import`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `import`

# %% cell_style="split"
# import permet de charger un code
import math

# %% cell_style="split"
# cela définit une variable, ici 'math'
# qui est une référence
# vers un objet module
math

# %% cell_style="split"
type(math)

# %% cell_style="split"
# cet objet possède des attributs
# auxquels on peut accéder
# avec la notation module.attribut

math.pi

# %% [markdown] slideshow={"slide_type": "slide"}
# ## autres formes

# %% cell_style="split"
# avec cette forme on ne définit pas la variable math
# mais directement la variable pi

from math import pi
pi

# %% cell_style="split"
# ici on n'a importé que le nom 'pi'
# et donc 'cos' n'est pas défini
# mais grâce au 'import math'
# on peut y accéder par math.cos

math.cos(pi)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## installation de librairies tierces
#
# si on a besoin d'installer un module  
# qui ne fait pas partie de la bibliothèque standard :
#
# * répertoire disponible sur <https://pypi.org/>
# * installation à faire avec l'outil `pip`  
#   (se lance depuis le terminal)

# %% slideshow={"slide_type": "slide"}
# cette astuce avec le ! me permet
# d'appeler une commande normalement destinée au terminal
# mais depuis Python

# !pip install nbautoeval

# %%
import nbautoeval

# %% [markdown] slideshow={"slide_type": "slide"}
# ## c'est quoi un module ?

# %% [markdown]
# un module est un objet Python qui correspond à un fichier (ou répertoire) source  
# depuis cet objet vous pouvez accéder à des **attributs**  
# avec la notation `module.attribut`  
#   (qui est *btw* la même notion que, par ex., `str.capitalize`)    
# le module a autant d'attributs que d'objets globaux dans le code source  
# dans le cas d'un répertoire les attributs référencent d'autres modules

# %% cell_style="split" slideshow={"slide_type": "slide"}
# regarder le contenu
# !cat mod.py

# %% cell_style="split"
import mod

# tous les noms dans le module (y compris les noms "internes")
dir(mod)

# %% cell_style="split"
# pour afficher tous les attributs du module
# et une fois le bruit éliminé
[x for x in dir(mod) if '__' not in x]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## notion de point d'entrée

# %% [markdown]
# votre programme Python est toujours exécuté par un interpréteur  
# qui "commence" quelque part: c'est le point d'entrée

# %% [markdown] cell_style="split"
# si vous lancez  
# ```bash
# $ python3 foo.py
# ```

# %% [markdown] cell_style="split"
# le point d'entrée dans ce cas est
# (le module correspondant à) `foo.py`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## recherche des modules
#
# Python recherche les modules dans plusieurs d'endroits (répertoires)
#
# * le répertoire qui contient le point d'entrée  
# * en option, la variable d'environnement `PYTHONPATH`
# * là où sont installés les morceaux de la librairie standard
#
# conseil : évitez de bidouiller `PYTHONPATH`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## organisation de votre code
#
# cela signifie que pour commencer,  
# on peut sans souci couper son code en fichiers  
# et les mettre tous dans le même répertoire

# %% [markdown] slideshow={"slide_type": ""}
# c'est une pratique courante et recommandée  
# il faut apprendre à découper  
# notamment pour augmenter la réutilisabilité

# %% [markdown] slideshow={"slide_type": "slide"}
# ## librairies utiles
#
# liste largement non exhaustive
#
# * gestion des fichiers: `from pathlib import Path`  
# * génération de nombres aléatoires `import random`
# * télécharger depuis Internet: `import requests`
# * ouverture de fichiers au format JSON: `import json` (standard)
#
# * Python scientifique: `numpy`, `pandas`, `matplotlib`, ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ## module `pathlib`

# %% [markdown]
# fait partie de la librairie standard  
# permet de faire des calculs sur les fichiers  
#
# * lister les fichiers présents
# * calculs sur les chemins et noms de fichier  
# * accéder aux métadata (taille, date, ...)

# %% cell_style="center" slideshow={"slide_type": "slide"}
# ici Path correspond à une classe
# on verra la théorie très bientôt
from pathlib import Path

# on recherche dans le répertoire courant '.'
# les fichiers/répertoires d'extension '.ipynb'
local_files = Path('.').glob('*.ipynb')

# observons les fichiers trouvés
for file in local_files:
    print('name', file.name)
    print('stem', file.stem)
    print('suffix', file.suffix)
    print('absolute()', file.absolute())
    print('size', file.stat().st_size)
    break

# %% [markdown] slideshow={"slide_type": "slide"}
# ## module `random`

# %% [markdown]
# une fois que vous avez le nom du module,  
# il vous suffit de consulter [la doc
# complète](https://docs.python.org/3/library/random.html)  
# pour cela taper dans google `python random module`  
# (nous reviendrons sur ce module lors de l'étude des librairies numériques)

# %% cell_style="split"
import random

# entre 0 et 1
random.random()

# %% cell_style="split"
# un entier entre deux bornes
# inclusivement
random.randint(0, 10)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## module `requests`

# %% [markdown]
# télécharger du contenu depuis une URL  
# accéder à l'entête http
# plus flexible que l'équivalent dans la librairie standard `urllib2`

# %% slideshow={"slide_type": "slide"}
import requests

url = ""
url = "https://github.com/timeline.json"

request = requests.get(url)

print(f"code de retour HTTP: {request.status_code}")

# %% cell_style="split"
raw_content = request.text
# une chaine de caractères
type(raw_content)

# %% cell_style="split"
# le début de cette chaine
raw_content[:120]
# son contenu est en format json (voir slide suivante)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## module `json`
#
# le cas qu'on vient de voir est très fréquent  
# JSON est un format texte (compatible réseau donc Internet)  
# mais qui conserve un minimum de structure :
# permet de transmettre listes et dictionnaires

# %% cell_style="split"
# pour décoder le JSON qu'on a lu
# et qui est dans la str raw_content
import json

decoded = json.loads(raw_content)
type(decoded) # la chaîne contenait un dict Pyhon

# %% cell_style="split"
# cette fois on a un peu
# de structure
for k, v in decoded.items():
    print(f"{k}\n\t{v[:20]}...")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## gestion de fichiers

# %% cell_style="center"
# pour écrire dans un fichier
with open("tutu.txt", "w") as writer:
    for i in range(4):
        print(f"i={i}", file=writer)

# %% [markdown] cell_style="center"
# `with open...` ouvre le fichier `tutu.txt` en écriture `"w"`  
#   et crée la variable `writer` de type `File`  
# `writer` n'est visible que dans le `with`  
# `print(..., file=writer)` écrit dans ce fichier  
# `with` ferme le fichier à la sortie  
# (nous allons maintenant lire ce fichier)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fichiers - suite

# %% cell_style="split"
# à l'envers, on relit le fichier
with open('tutu.txt') as reader:
    for line in reader:
        print(line, end="")


# %% [markdown] cell_style="split"
# sans préciser le mode d'ouverture  
# `open` ouvre le fichier en lecture  
# l'objet `reader` est **itérable**
#
#
# la variable `line` contient une fin de ligne  
# pas besoin que `print` en rajoute une

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exercice
#
# écrire une fonction `json_random()` qui retourne :
#
# * une chaine de caractères
# * qui correspond à l'encodage en JSON
# * d'une liste contenant - au hasard - entre 2 et 5 valeurs numériques
# * elles-mêmes tirées au hasard dans l'intervalle $[2 .. 5]$

 # %% cell_style="center"
 # n'oubliez pas d'importer les modules
# dont vous avez besoin
def random_json():
    """
    returns a JSON-encoded of a list
    of 2 to 5 values between 2 and 5
    """
    # votre code ici
    pass


# %%
from check_random_json import check_random_json

check_random_json(random_json)
