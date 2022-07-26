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
#     title: fonctions
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
# # fonctions

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le mot clé `def`
#
# on définit une fonction avec le mot-clé `def`

# %% cell_style="split"
# remarquez:
# . l'indentation
# . le mot clé return
# . le docstring  
def P(x):
    """
    la fonction P implémente
    le polynôme
    que l'on étudie
    """
    return x**2 + 3*x + 2


# %% cell_style="split"
# un appel
P(10)

# %% cell_style="split"
P(100)

# %% cell_style="split"
# le docstring est rangé
# dans la fonction
help(P)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## syntaxe

# %% [markdown]
# en Python, les sauts de ligne et la présentation (indentation)  
# **font partie de la syntaxe**  
# c'est différent d'autres langages comme C++, Java, Javascript, ...  
# ce choix est fait pour **augmenter la lisibilité**  
# car on n'a alors pas besoin de sucre syntaxique comme `begin .. end` ou autres `{ .. } `

# %% [markdown] slideshow={"slide_type": "slide"}
# ## syntaxe - illustration  
#
# c'est l'indentation qui détermine la structure  
# l'usage est d'indenter de **4 espaces**  
# et de ne **pas utiliser** de tabulations (trop variables)

# %% [markdown] cell_style="split"
# ```c++
# // en Javascript
# // on écrirait
# function foo(i) {
#     if (i <= 0) {
#         fonction1(i);
#         fonction2(i);
#     } else {
#         fonction3(i);
#     }
# }
# ```

# %% [markdown] cell_style="split"
# ```python
# # en Python ce serait
# def foo(i):
#     if i <= 0:
#         fonction1(i)
#         fonction2(i)
#     else:
#         fonction3(i)
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `return`

# %% [markdown]
# une fonction est censée retourner quelque chose  
#
#     resultat = fonction(arguments)
#
# avec `return` on indique ce qui est le résultat  
# l'exécution de la fonction **s'arrête** à ce moment-là  
# si pas de `return`, le retour est `None`

# %% cell_style="split" slideshow={"slide_type": "slide"}
# une fonction incomplète
def broken_abs(n):
    if n <= 0:
        return -n


# %% cell_style="split"
# avec un négatif  
broken_abs(-10)

# %% cell_style="split"
# ici la fonction retourne None
# du coup le notebook n'affiche rien
broken_abs(10)


# %% cell_style="split"
# une version correcte devrait faire plutôt
def fixed_abs(n):
    if n <= 0:
        return -n
    return n


# %% cell_style="split"
# on ignore la dernière ligne
# puisqu'on est arrivé au return
fixed_abs(-10)

# %% cell_style="split"
# et maintenant ca marche avec les positifs
fixed_abs(10)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## variables locales

# %% [markdown]
# à l'intérieur d'une fonction on peut naturellement utiliser des variables  
# la **portée** de ces variables est **limitée à la fonction**  
# ici les deux variables `var` sont des entités **distinctes**

# %% cell_style="split"
var = "globale"

def polynom(n):
    """
    polynome 4.x3 + 3.x2 + 2x + 1
    sans mise à la puissance
    """
    var = n         # var = n
    resultat = 1
    resultat += 2 * var
    var = var * n   # var = n**2
    resultat += 3 * var
    var = var * n   # var = n**3
    resultat += 4 * var
    print(f"dans def: var = {var}")
    return resultat


# %% cell_style="split"
polynom(1)

# %% cell_style="split"
polynom(10)

# %% cell_style="split"
var


# %% [markdown] slideshow={"slide_type": "slide"}
# ## appels imbriqués / récursion

# %% [markdown] cell_style="center"
# bien sûr dans le code d'une fonction  
# on peut appeler d'autres fonctions  
# y compris la fonction courante : fonction **récursive**  (cf `fact.py`)

# %% [markdown] cell_style="center"
# lorsque `f` appelle `g`,  
# `f` est en quelque sorte *mise en suspens* pendant l'exécution de `g`  
# du coup il est nécessaire de conserver où en est `f`  
#
# * à quel point on en est dans `f`
# * la valeur des variables locales de `f`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pile d'exécution

# %% [markdown]
# c'est le propos de la pile d'exécution  
# qui conserve la trace des appels imbriqués  
#
# illustrons cela avec https://pythontutor.com/  
# un site qui est très utile pour visualiser l'exécution de code simple

# %% cell_style="center"
# une magie pour créer des cellules sous pythontutor.com

# %load_ext ipythontutor

# %% cell_style="center" slideshow={"slide_type": "slide"}
# %%ipythontutor height=500

def fact(n):
    if n <= 1:
        return n
    else:
        return n * fact(n-1)

# pour visualiser la pile d'exécution

x = fact(3)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exceptions

# %% [markdown]
# le mot-clé `raise` permet de **lever une exception**  
# cela a pour effet d'interrompre la fonction courante  
# et de **dépiler** les appels jusqu'à  
# trouver un `except` qui **attrape l'exception**

# %% cell_style="center" slideshow={"slide_type": "slide"}
# une fonction qui va faire raise
# mais pas tout de suite
def time_bomb(n):
    print(f"in time_bomb({n})")
    if n > 0:
        return time_bomb(n-1)
    else:
        raise OverflowError("BOOM")


# %% cell_style="split" slideshow={"slide_type": "slide"} tags=["raises-exception"]
# si personne n'attrape un raise
# le contrôle retourne à l'OS
# d'une manière très abrupte
def driver():
    time_bomb(1)
    print("will never pass here")

driver()


# %% [markdown] cell_style="split"
# ![uncaught](media/except-stack-uncaught.png)

# %% cell_style="split" slideshow={"slide_type": "slide"}
# cette fois tout est
# sous contrôle
def driver_try():
    try:
        time_bomb(2)
    except Exception as exc:
        print(f"OOPS {type(exc)}, {exc}")
    print("will do this")

driver_try()


# %% [markdown] cell_style="split"
# ![try](media/except-stack-try.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## clause `except`

# %% [markdown] cell_style="center"
# * la clause `raise` doit fournir un objet idoine  
#   (par exemple on ne peut pas faire `raise 1`)
#
# * doit être une instance d'un objet de type `BaseException`  
#   (ou de l'une de ses sous-classes)
#
# * la clause `except` permet de n'attraper  
#   qu'une partie des exceptions possibles
#   (par exemple, attraper toutes les erreurs d'entrées-sortie  
#    mais laisser passer les autres)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## passage d'arguments
#
# les mécanismes de définition et de passage de paramètres sont assez complexes (cf cours
# avancé)  
# pour cette introduction disons simplement qu'on peut définir des paramètres optionnels :

# %%
# une fonction qui accepte un ou deux arguments
def foo(obligatoire, optionnel=10):
    print(f"obligatoire={obligatoire} optionnel={optionnel}")


# %% cell_style="split"
# avec deux arguments
foo(100, 20)

# %% cell_style="split"
# ou avec un seul
foo(1000)

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## exercices - avancés

# %% [markdown] cell_style="center"
# https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w4/w4-s3-x1-pgcd  
# https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w4/w4-s3-x4-power

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# écrire une fonction qui calcule la puissance entière
#
# ```python
# def power(x, n):
#     """
#     retourne x à la puissance n
#     en O(log(n))
#     """
#     pass # votre code ici
# ```

# %% [markdown] cell_style="split"
# écrire une fonction qui calcule de pgcd
#
# ```python
# def pgcd(a, b):
#     """
#     retourne le pgcd de a et b
#     par convention on admet que
#     pgcd(0, n) == pgcd(n, 0) = n
#     """
#     pass
# ```
