# Notebooks du cours de Python Numérique

Ce dépôt contient une série de notebooks de cours à destination des élèves de première année.

# Installation

## Avec `pip`

Afin de simplifier l'installation avec pip, un fichier `requirements.txt` est fourni avec le projet

```bash
(PyNum) $ pip install -r requirements.txt
```

## Avec `conda` 

On installera Jupyter directement avec l'outil `conda` accessible depuis le terminal:

```bash
# Pour installer jupyter et jupytext
$ conda install jupyter jupytext
```

## Épilogue

Dans les deux cas, pour activer l'extension `toc2` (qui permet
d'afficher la table des matières, et met les numéros de sections),
faites enfin

```bash
# pour les numéros de section
$ jupyter nbextension enable toc2/main
```

# Environnements virtuels

Lorsqu'on travaille sur plusieurs projets, il est possible de créer un environnement virtuel afin d'isoler les dépendances installées: cela evitera qu'une modification apportée sur un projet impacte les autres projets par effet de bord.

## Avec `pip`

```bash
# ici j'utilise Python3.9 pour créer mon venv
$ python3.9 -mvenv --prompt 'PyNum' venv pip wheel
```

puis avant/chaque développement on pourra l'activer/le désactiver

```bash
# pour activer le venv
$ . ./venv/bin/activate

# puis pour le désactiver
(PyNum) $ deactivate
```

## Avec `conda`

Nous allons créer un environnement virtuel `conda` à partir du fichier `environment.yml` fourni:

```bash
$ conda env create -f environment.yml
```

Cette commande a généré un nouvel environnement nommé "pynum" comme on peut le voir via la sous-commande `env list` (les différents Paths peuvent changer...):

```bash
❯ conda env list
# conda environments:
#
base                  *  /Volumes/Tools/miniconda
pynum                    /Volumes/Tools/miniconda/envs/pynum
```

Pour utiliser cet environnement et à chaque fois que l'on voudra de ré-activer, on lancera la commande suivante:

```bash
# Pour activer l'environnement virtuel
$ conda activate pynum

# Pour désactiver l'environnement virtuel
$ conda deactivate
```
