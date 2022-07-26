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
#     title: classes
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
# # classes

# %% [markdown] slideshow={"slide_type": "slide"}
# ## types prédéfinis et monde réel
#
# les types prédéfinis que l'on a vus jusqu'ici  
# i.e. nombres, chaines, containers  
# (pour rappel: `bool`, `int`, `float`, `str`, `list`, `set`, `dict`)  
# sont pratiques et puissants

# %% [markdown]
# **MAIS** souvent cela n'est pas suffisant
# pour traiter des problèmes réels

# %% [markdown] slideshow={"slide_type": "slide"}
# ## typiquement
#
# on a très souvent besoin de manipuler des données 'composites'  
# e.g. un ensemble de personnes, de villes, de compagnies aériennes  
# en termes de modèle de données, ce sont des 'enregistrements'  
# c'est-à-dire en fait des données composites

# %%
# une façon naive d'implémenter une donnée composite
# est d'utiliser un dictionnaire

personne = {'name': 'Dupont', 'age': 32}


# %% [markdown]
# utiliser un dictionnaire - ou un tuple - peut faire l'affaire  
# pour des applications simples  
# (c'est par exemple ce qu'on récupère d'un fichier JSON)  
# mais c'est vite un peu lourd et très limité

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## `class`  
# dans ces cas-là (et dans bien d'autres)  
# il est plus flexible de se définir **un nouveau type**  
# qui permette de créer des objets qui ont les propriétés en question  
# que dans ce contexte on appelle **des attributs**

# %% cell_style="split"
# voici comment définir
# une classe `User`

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# %% cell_style="split"
# une fois qu'on a défini une classe,
# on peut s'en servir pour créer
# des objets - on dit des instances
# de la classe

user1 = User("Lambert", 25)

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## instances

# %% [markdown]
# remarquez qu'ici
#
# * on a défini la méthode spéciale `__init__` avec **3** paramètres
# ```
# def __init__(self, name, age)
# ```
#
# * ce qui fait qu'on peut appeler (une fonction du nom de) la classe avec **2** paramètres
# ```
# User("Lambert", 25)`
# ```
#
# * car le **premier paramètre** est l'objet en cours de création !
#
# * et la phrase `self.name = name`  
#   signifie que l'on attache le paramètre `name`  
#   dans l'attribut `name` de l'objet en cours de création

# %% [markdown] slideshow={"slide_type": "slide"}
# ## affichage

# %% cell_style="split"
# si on ne fait rien de spécial,
# l'affichage est vraiment vilain
user1
# qui vous dit que user1 est un objet dans le module __main__
# qu'il est de de type User
# et où il est dans la mémoire de votre ordi
# mais ce n'est sûrement pas ce que vous voulez voir !

# %% cell_style="split"
# pour améliorer cela:
# vous définissez la représentation de vos objets de type User
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # définit comment afficher
    # les objets de cette classe
    def __repr__(self):
        return f"{self.name}, {self.age} ans"


# %%
user2 = User("Martin", 22)
user2


# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes

# %% [markdown]
# comme on l'a évoqué dans la section "objets, types et méthodes"  
# dans une classe on peut définir **des méthodes**  
# qui sont des fonctions qui s'appliquent sur un objet (de cette classe)

# %% cell_style="split"
# une implémentation très simple
# d'une file FILO
# premier entré dernier sorti

class Stack:

    def __init__(self):
        self.frames = []

    def push(self, item):
        self.frames.append(item)

    def pop(self):
        return self.frames.pop()

    def __repr__(self):
        return " > ".join(self.frames)


# %% cell_style="split"
# instance
stack = Stack()

stack.push('fact(3)')
stack.push('fact(2)')
stack.push('fact(1)')

stack

# %% cell_style="split"
stack.pop()

# %% cell_style="split"
stack

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes - suite

# %% [markdown]
# à nouveau, remarquez que la **définition** d'une méthode  
# prévoit un paramètre de plus que l'appel de la méthode  
# car `obj.methode(...)`  
# est équivalent à
# `methode(obj, ...)`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## intérêts de cette approche

# %% [markdown]
# * définir vos propres types de données
#
# * grouper les données qui vont ensemble dans un objet  
#   facile à passer à d'autres fonctions
#
# * invariants: garantir de bonnes propriétés  
#   si on utilise les objets au travers des méthodes  
#
# * organise les espaces de noms  
#   e.g. pas de conflit entre Class1.name et Class2.name
#
# * héritage - ne sera pas détaillé dans ce cours

# %% [markdown] slideshow={"slide_type": "slide"}
# ## objets et langage

# %% [markdown]
# le langage "connaît" bien sûr les types prédéfinis  
# c'-à-d qu'il sait "faire la bonne chose"  
# selon le type des objets qu'il manipule

# %% [markdown]
# exemples, selon le type de `obj` :  
#
# * `print(obj)`
# * opérateurs comme `obj + x`
# * itération `for item in obj`
# * `len(obj)`
# * test d'appartenance `x in obj`
# * indexation `obj[x]`
# * etc..

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## exemple - `if obj:`
#
# remarquez qu'on peut toujours écrire un test `if` (ou `while`)
# même si le sujet du test n'est pas un booléen

# %% cell_style="split"
if 0:
    print('bingo')

# %% cell_style="split"
if 2:
    print('bingo')

# %% cell_style="split"
if []:
    print('bingo')

# %% cell_style="split"
if [1]:
    print('bingo')


# %% [markdown] cell_style="center"
# la règle pour les types prédéfinis est que dans un test  
# `0`, `0.0`, `""`, `[]`, `set()`, `{}` sont considérés comme `False`  
# les autres valeurs sont considérées comme `True`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes spéciales

# %% [markdown]
# les méthodes spéciales sont toutes de la forme `__bidule__`  
# on en a déjà vu 2 : `__init__` et `__repr__`  
# le langage en prévoit plusieurs dizaines (optionnelles)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de méthode spéciale

# %% [markdown]
# **exemple**  
# lorsqu'un objet est utilisé dans un `if obj:`  
# il est d'abord converti en booléen par `bool(obj)`  
#
# pour redéfinir ce que cela veut dire sur une classe  
# on peut définir la méthode spéciale `__bool__`

# %% [markdown]
# dans l'exemple qui suit, je définis une classe `Person`  
# et je décide (uniquement à but pédagogique)  
# que l'instruction `if person:`  
# va s'exécuter avec les gens dont le nom n'est pas `nobody`

# %% cell_style="split" slideshow={"slide_type": "slide"}
# une classe jouet
# uniquement à but pédagogique ...

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # cette méthode est appelée lorsqu'on
    # a besoin de convertir un objet en booléen
    # e.g. quand on fera
    # if person:
    #    blabla
    def __bool__(self):
        return self.name != 'nobody'


# %% cell_style="split"
real_person = Person('Dupont', 32)
fake_person = Person('nobody', 0)

# %% cell_style="split"
if real_person:
    print('YES !')

# %% cell_style="split"
# dans ce cas il ne passe rien
# car notre instance est convertie en
# booléen et çca donne 'False'
if fake_person:
    print('NOPE')

# %%
# c'est-à-dire que
bool(real_person)

# %% cell_style="center"
bool(fake_person)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé
#
# * on définit une classe avec le mot clé `class`
# * avec les classes on peut étendre les types prédéfinis `int`, `str`, `list`, …
# * un objet dans une classe contient typiquement des attributs
# * une classe définit typiquement des méthodes
# * on accède aux attributs et méthodes avec la syntaxe  
#   `object.attribut`  ou `object.methode()`
#
# * grâce aux méthodes spéciales, on peut bien intégrer une classe dans le langage

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la classe `Quaternion` - avancés

# %% [markdown] slideshow={"slide_type": ""}
# **En option**
#
# on peut aussi redéfinir les opérateurs arithmétiques  
# comme `+` et `*` avec les  
# méthodes spéciales `__add__` et `__mul__`
#
# Application: une micro-classe qui implémente les quaternions
#
# * https://fr.wikipedia.org/wiki/Quaternion
# * le corps non commutatif engendré sur $\mathbb{R}$
#   par trois éléments $i, j, k$ tels que
#
#   $$i^2 = j^2 = k^2 = ijk = -1$$
#
# * un quaternion s'écrit donc
#
#   $q = a + bi + cj + dk$ avec $(a, b, c, d) \in \mathbb{R}^4$

# %% slideshow={"slide_type": "slide"}
class Quaternion:

    def __init__(self, a, b, c, d):
        self.implem = (a, b, c, d)  
    # c'est la partie intéressante
    def __add__(self, other):
        """defines q1 + q2)"""
        return Quaternion(*(x+y for x, y in zip(self.implem, other.implem)))  
    def __mul__(self, other):
        """defines q1 * q2"""
        a1, b1, c1, d1 = self.implem
        a2, b2, c2, d2 = other.implem
        a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
        b = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
        c = a1 * c2 + c1 * a2 + d1 * b2 - b1 * d2
        d = a1 * d2 + d1 * a2 + b1 * c2 - c1 * b2
        return Quaternion(a, b, c, d)  
    def __eq__(self, other):
        """implements q1 == q2"""
        return self.implem == other.implem  
    def __repr__(self):
        a, b, c, d = self.implem
        return f"({a}, {b}, {c}, {d})"


# %% cell_style="split" slideshow={"slide_type": "slide"}
q0 = Quaternion(0, 0, 0, 0)
q1 = Quaternion(1, 0, 0, 0)
q_1 = Quaternion(-1, 0, 0, 0); q_1

# %% cell_style="split"
i = Quaternion(0, 1, 0, 0)
j = Quaternion(0, 0, 1, 0)
k = Quaternion(0, 0, 0, 1)
k

# %% cell_style="split"
i * i

# %% cell_style="split"
i*i == j*j == k*k == i*j*k == q_1

# %% cell_style="split"
q = Quaternion(1, 2, 3, 4)

# %% cell_style="split"
q * q

# %% cell_style="split"
q * i

# %% cell_style="split"
i * q

# %% [markdown] slideshow={"slide_type": "slide"}
# limitations pour cette version rustique :
#
# * manque des opérations
# * égalité sans doute trop stricte (arrondis)
# * ne sait pas interagir avec `int` ou `float`
# * affichage
# * ...

    # %% slideshow={"slide_type": "skip"}
    # pour affichage
    labels = ['', 'i', 'j', 'k']  
    # un code possible pour un affichage plus élégant

    # affichage
    def __repr__(self):
        # on prépare des morceaux comme '3', '2i', '4j', '5k'
        # mais seulement si la dimension en question n'est pas nulle
        parts = (f"{x:.1f}{label}" for x, label in zip(self.implem, labels) if x)

        # on les assemble avec un + au milieu
        full = " + ".join(parts)

        # si c'est vide c'est que self est nul
        return full if full != "" else "0"

        # ce qui donnerait aussi en version un peu plus condensée
        # mais beaucoup moins lisible
        # return (" + ".join(f"{x:.2f}{label}" for x, label in zip(self.implem, labels) if x) or "0")
