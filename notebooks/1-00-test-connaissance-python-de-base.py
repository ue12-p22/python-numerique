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
#     title: test sur le langage Python
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %% [markdown] slideshow={"slide_type": "slide"}
# # test sur le langage Python

# %% [markdown] slideshow={"slide_type": "slide"}
# Les objectifs du cours de base sur Python
#
#    - être capable de lire et d'écrire du code simple
#       
#    - mettre en oeuvre ce code simple dans un notebook
#    
#    - ce *vernis* sur les concepts de **Python** vous permettra d'aborder les outils de base de *calcul scientifique* **numpy, pandas, matplotlib**
#    

# %% [markdown]
# Ce notebook jupyter propose une série d'exercices en **auto-évaluation** pour tester votre niveau en python. Ils sont présentés en 3 niveaux: ***débutant***, ***moyen*** et ***avancé***
#
#    1. Vous rencontrez des difficultés dans les exercices pour débutants ?  
#       Votre niveau en Python est **insuffisant.**  
#       Nous vous demandons d'**étudier les notebooks** de ce cours (intitulé *Python primer*) qui reprennent les notions essentielles du langage.  
#       Et surtout **inscrivez-vous aux tutorats**
#       
#    1. Vous faites le niveau débutant, mais sans plus ?
#       Votre niveau en Python est **pas terrible.**  
#       **Lisez les notebooks** de ce cours
#
#    1. Vous avez réussi tous les exercices pour débutants et la plupart des exercices pour moyens ?  
#       Votre niveau en python semble **suffisant.**  
#       Vous n'avez pas réellement besoin de revoir les autres notebooks  
#       Lisez simplement le notebook `un-tour-de-python`.
#
#    1. Vous avez réussi les exercices pour débutants, moyens et la plupart des exercices pour avancés ?  
#       Proposez-vous auprès de vos enseignants pour aider lors des tutorats.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## quelques définitions
#
# -----------------
#
#    * Python est un langage **orienté objet** :  toutes ses **données sont des objets**
#      
#      
#    * chaque objet a un **type**
#    
#    
#    * un *module* a un type, une *fonction* a un type, un *entier* a un type...
#    
#    
#    * le type de l'objet définit le **comportement des opérations** qu'on lui applique  
#      e.g. le **+** des chaînes de caractères ne se comporte pas comme le **+** des entiers
#      
#           
#    * le langage Python a un ensemble de types prédéfinis `int`, `str`...  
#      il vous permet aussi de définir vos propres types (c'est à ça que servent les classes)
#    
#    ----------------   
#    
#    * une **méthode** est une fonction qui s'appelle **à travers un objet**  
#      `'abc'.upper()` est la méthode *upper* du type *str* appliquée à la chaine `'abc'`
#      remarquez la différence avec l'appel d'une fonction classique comme `print('abc')`

# %% [markdown]
# ## expressions
#
# **débutants**
#    1. afficher le type et la valeur de l'expression `x % 2 == 0` où `x` est un nombre
#    1. mettez cette expression dans la condition d'un `if` qui affiche si `x` est pair ou impair
#

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ##  chaînes de caractères
#
# **débutants**
#
#    1. créer une chaîne de caractères
#    1. imprimer la chaîne et sa longueur
#    
# **moyens**
#
#    1. créer une autre chaîne de caractères
#    1. concaténer les deux chaînes
#    1. mettre le résultat en majuscule
#
# **avancés**
#
#    1. créer une chaîne multi-lignes
#    1. afficher la chaîne ainsi que sa longueur en utilisant une f-string
#    1. découper la chaîne pour obtenir une liste des lignes
#    1. découper chaque ligne en une liste de mots sans ponctuation

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## indexation et slicing de chaînes de caractères
#
# **débutants**
#
#    1. créer la chaîne de caractères:  `j'adore python et numpy !`
#    1. accéder au premier et au dernier caractère de la chaîne `j` et `!`
#    
# **moyens**
#
#    1. découper la chaîne pour ne garder que `adore`
#    1. tester si le caractère 'w' est dans la chaîne
#    
# **avancés**
#
#    1. découper la chaîne pour ne garder que "aoe"
#    1. copier la chaîne complète (par slicing)
#    1. renverser la chaîne pour obtenir: `! ypmun te nohtyp eroda'j`

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonctions
#
# **débutants**
#
#    1. faites une fonction *foo* qui prend deux paramètres dont le dernier est optionnel et vaut $0$ par défaut, et dont le corps ne fait rien
#    
# **moyens**     
#    1. ajouter un docstring à la fonction (un docstring est un message de help)
#    1. faites une fonction qui affiche les termes de la suite entière suivante  
#    - $n\in \mathbb{N^*}$
#    - $u_0 = n$
#    - $u_{p+1}={\begin{cases}{\dfrac {u_{p}}{2}}&{\mbox{si }}u_{p}{\mbox{ est pair,}}\\3u_{p}+1&{\mbox{si }}u_{p}{\mbox{ est impair.}}\end{cases}}$  
#    on l'arrête quand $u_n$ vaut $1$  
#    faites une version récursive et une version itérative de cette fonction
#
# **avancé**
#
#    1. à la place d'afficher les termes de la suite $u_n$, votre fonction récursive en renvoie la liste
#    1. ajouter les cas d'erreurs à votre fonction récursive
#    1. faites une fonction qui prend un nombre variable d'arguments et qui les parcourt en affichant leur valeur
#    1. faites une fonction qui prend un nombre variable d'arguments nommés et qui les parcourt en affichant leur valeur

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exceptions
#
# **débutants**
#
#    1. diviser un entier par *0* que constatez-vous ?
#    1. rattraper l'exception afin que le programme ne soit pas arrêté
#    
# **moyens**  
#    1. rattraper toutes les exceptions

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## listes (`list`)
#
# **débutants**
#
#    1. construire une liste contenant un entier, une chaînes de caractères, un flottant
#    1. modifier le premier élément de la liste; est-ce qu'on peut remplacer l'entier par un élément d'un autre type ?
#    1. ajouter en fin de liste un élément - par exemple un booléen
#    1. enlever le dernier élément de la liste
#    
# **moyens**   
#    
#    1. tester si un élément est dans la liste
#    1. afficher un par un tous les éléments de la liste 
#    1. fabriquer une liste qui contient deux fois les éléments de la liste; par exemple si votre liste contient les él´ments `1, "pi", 3.14` vous devez produire `1, "pi", 3.14, 1, "pi", 3.14`
#    
# **avancés**
#    1. slicer la liste de manière à n'en garder qu'un élément sur 2 à partir du début
#    1. créer une nouvelle liste contenant la première liste
#    1. en partant d'une liste d'entiers quelconques, la trier dans le sens croissant ou décroissant
#

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## tuples
#  
# **débutants**
#    1. créer un tuple
#    1. le modifier
#    1. que se passe-t-il ?
#    
# **moyens**
#    1. pourquoi ? 

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## dictionnaires (`dict`)
#
# **débutants**
#    1. créer un dictionnaire correspondant à des personnes; dans le dictionnaire, la clé est le nom de la personne, et la valeur donne son âge
#
# **moyens**
#    1. afficher le type d'un dictionnaire
#    1. tester si une personne est dans le dictionnaire et si oui augmenter son age de 1 an
#    
# **avancés**   
#    1. Afficher la liste des clés du dictionnaire
#    1. Afficher avec un **for** les noms et l'age de toutes les personnes du dictionnaire
#    1. Puis-je utiliser une `str` comme clé d'un dictionnaire ?
#    1. Puis-je utiliser un objet de type `list` comme clé d'un dictionnaire ? Pourquoi ?  
#    Une idée pour *contourner* le problème ?

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## ensembles (`set`)
#
# **débutants**
#    1. créer un ensemble vide
#    1. ajoutez lui les valeurs `'red'`, `'blue'`, `'red'`, `12`, `3.14`
#    1. créer un ensemble avec les valeurs `'red'`, `'blue'`
#    1. supprimer la valeur `'red'` du premier ensemble
#    1. faites l'intersection des deux ensemble
#
# **moyens**
#    1. Parcourez l'ensemble en affichant le type des éléments
#    1. Puis-je mettre l'objet `[13, 17]` dans l'ensemble ? Pourquoi ?

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## références
#
#    - en programmation, on manipule très souvent des **références** vers des objets
#    - par exemple:
#
#       * quand on passe un argument à une fonction
#       * cela crée une nouvelle référence vers un objet existant
#       * et en tous cas en Python, on ne **copie pas** l'objet
#    - cela permet d'éviter les copies inutiles
#    - mais on peut ainsi accéder à un objet de plusieurs manières: **références partagées**

# %% [markdown] slideshow={"slide_type": "slide"}
# **débutants**
#
# 1. on exécute le code suivant
#
#     ```python
#     def foo(liste):
#         liste.append(4)
#
#     L = [1, 2, 3]
#     foo(L)
#     print(len(L))
#     ```
#
#     quelle est la valeur affichée ? pourquoi ?

# %% [markdown]
# **moyens**
#
# 1. on exécute le code suivant
#
#     ```python
#     L = [1, 2, 3]
#     L2 = [L, L, L]
#     L2[0][0] = 100
#     print(L2[2][0])
#     ```
#     
#     quelle est la valeur affichée ? pourquoi ?
#     
# 1. à quoi sert l'opérateur `is` ? quelle est la différence avec l'opérateur `==` ?  
#    par exemple que va imprimer le code suivant ?
#    ```
#    L1 = [1, 2, 3]
#    L2 = L1
#    L3 = [1, 2, 3]
#    print('avec ==', L1 == L2, L1 == L3)
#    print('avec is', L1 is L2, L1 is L3)
#    ```

# %% [markdown] slideshow={"slide_type": "slide"}
# **avancé**
#
# 1. on veut créer une liste avec un seul élément qui est .. *la liste elle-même !*  
#    c'est-à-dire telle que `L[0] is L`
#
#   1. est-ce possible ? si oui comment faire ?
#   1. comment s'affiche cet objet ? pourquoi ?

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## itérateurs simples
#
# **débutants**  
#    1. creer le `range` des 100 premiers entiers
#    1. quel est le type de l'objet **range** créé ?
#    1. itérer sur le `range` pour sommer les entiers
#    
# **moyens**   
#    1. à quoi sert la fonction `enumerate` ? 
#    1. utilisez-la pour afficher les éléments du dictionnaire de personnes avec leur rang (en commençant à 0)  
#       i.e. produire une sortie du genre de 
#       ```
#       rang 0 - paul: 20 ans
#       rang 1 - pierre: 32 ans
#       ...
#       ```
#    
# **avancé**  
#    1. quelle est la différence entre le `range` des 100 premiers entiers et la `list` des 100 premiers entiers ?
#    1. mettez tous les éléments du range au carré 
#      1. par une compréhension
#      1. et par une expression génératrice  
#      quelle est la différence ?
#    

# %%
# votre code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## classes
#
# **débutants**
#    1. implémentez une classe de personnes avec leur nom et leur age
#    1. faites une méthode pour augmenter l'âge d'une personne
#    
# **moyens**:
#    1. donnez la représentation sous la forme d'une `str` des objets de la classe
#       i.e. on veut par exemple que 
#       ```
#       >>> person = Person('paul', 20)
#       >>> str(person)
#       paul: 20 ans
#       ```
#    
# **avancés**   
#    1. écrivez une classe d'entiers `Integer` dont la valeur est 0 par défaut et programmez la méthode `+`  
#       i.e. on veut par exemple que 
#       ```python
#       >>> i1 = Integer(100)
#       >>> i2 = Integer(200)
#       >>> i1 + i2
#       Integer(300)
#       ```

# %% [markdown]
# ## help

# %% [markdown]
# **débutants**  
#    1. afficher la documentation des `int`
#    
# **moyens**  
#    1. ajouter la documentation à une fonction et affichez là
#    
# **avancés**  
#    1. ajouter la documentation à une classe, à une méthode dans une classe, affichez-les
#    1. comment s'y prend-on pour ajouter la documentation à un module ?

# %%
# votre code
