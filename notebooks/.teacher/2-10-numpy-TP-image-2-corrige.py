# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     cell_metadata_json: true
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
#     title: suite du TP simple avec des images
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")

# %% [markdown]
# # suite du TP simple avec des images
#
# merci à Wikipedia et à stackoverflow
#
# **le but de ce TP n'est pas d'apprendre le traitement d'image  
# on se sert d'images pour égayer des exercices avec `numpy`  
# (et parce que quand on se trompe ça se voit)**

# %%
import numpy as np
from matplotlib import pyplot as plt

# %% [markdown] {"tags": ["framed_cell"]}
# **notions intervenant dans ce TP**
#
# sur les tableaux `numpy.ndarray`
#
# * `reshape()`, tests, masques booléens, *ufunc*, agrégation, opérations linéaires sur les `numpy.ndarray`
# * les autres notions utilisées sont rappelées (très succinctement)
#
# pour la lecture, l'écriture et l'affichage d'images
#
# * utilisez `plt.imread`, `plt.imshow`
# * utilisez `plt.show()` entre deux `plt.imshow()` dans la même cellule
#
# **note**
#
# * nous utilisons les fonctions de base sur les images de `pyplot` par souci de simplicité
# * nous ne signifions pas là du tout que ce sont les meilleures  
# par exemple `matplotlib.pyplot.imsave` ne vous permet pas de donner la qualité de la compression  
# alors que la fonction `save` de `PIL` le permet
#
# * vous êtes libres d'utiliser une autre librairie comme `opencv`  
#   si vous la connaissez assez pour vous débrouiller (et l'installer), les images ne sont qu'un prétexte
#
# **n'oubliez pas d'utiliser le help en cas de problème.**

# %% [markdown]
# ## Création d'un patchwork

# %% [markdown]
# 1. Le fichier `rgb-codes.txt` contient une table de couleurs:
# ```
# AliceBlue 240 248 255
# AntiqueWhite 250 235 215
# Aqua 0 255 255
# .../...
# YellowGreen 154 205 50
# ```
# Le nom de la couleur est suivi des 3 valeurs de ses codes `R`, `G` et `B`  
# Lisez cette table en `Python` et rangez-la dans la structure qui vous semble adéquate.
# <br>
#
# 1. Affichez, à partir de votre structure, les valeurs rgb entières des couleurs suivantes  
# `'Red'`, `'Lime'`, `'Blue'`
# <br>
#
# 1. Faites une fonction `patchwork` qui  
#
#    * prend une liste de couleurs et la structure donnant le code des couleurs RGB
#    * et retourne un tableau `numpy` avec un patchwork de ces couleurs  
#    * (pas trop petits les patchs - on doit voir clairement les taches de couleurs  
#    si besoin de compléter l'image mettez du blanc  
#    (`numpy.indices` peut être utilisé)
# <br>
# <br>   
# 1. Tirez aléatoirement une liste de couleurs et appliquez votre fonction à ces couleurs.
# <br>
#
# 1. Sélectionnez toutes les couleurs à base de blanc et affichez leur patchwork  
# même chose pour des jaunes  
# <br>
#
# 1. Appliquez la fonction à toutes les couleurs du fichier  
# et sauver ce patchwork dans le fichier `patchwork.jpg` avec `plt.imsave`
# <br>
#
# 1. Relisez et affichez votre fichier  
#    attention si votre image vous semble floue c'est juste que l'affichage grossit vos pixels
#    
# vous devriez obtenir quelque chose comme ceci
# <img src="patchwork-all.jpg" width="200px">

# %%
# votre code

# %% {"scrolled": false}
# prune-cell 1.
colors_dict = dict()
with open('rgb-codes.txt', 'r') as f:
    for line in f:
        name, r, g, b = line.split()
        colors_dict[name] = [int(r), int(g), int(b)]

# %%
# prune-cell 2.
for c in ['Red', 'Lime', 'Blue']:
    print(c, colors_dict[c])


# %% [markdown]
# prune-cell 3
#
# pour calculer le rectangle qui contient n couleurs
#
# n | rect | `int(sqrt(n))` |
# -|-|-|
# 1 | 1x1 | 1
# 2 | 1x2 | 1
# 3 | 2x2 | 1
# 4 | 2x2 | 2
# 5 | 2x3 | 2
# 6 | 2x3 | 2
# 7 | 3x3 | 2
# 8 | 3x3 | 2
# 9 | 3x3 | 3
# 10 | 3x4 | 3
# 11 | 3x4 | 3
# 12 | 3x4 | 3
# 13 | 4x4 | 3
# 14 | 4x4 | 3
# 15 | 4x4 | 3
# 16 | 4x4 | 4
# 17 | 4x5 | 4

# %%
# prune-cell 3
def rectangle_size(n):
    ''' calcule la taille du rectangle
        pour ranger n couleurs '''
    c = int(np.sqrt(n-1))+1 
    if (c-1)*c >= n:
        return c-1, c 
    else:
        return c, c

def patchwork (col_list, col_dict, side=5, background='White'):
    ''' create an image with a patchwork of the col_list colors
        the image contains l*c patches
        each patch is a square of side pixels
        the patchwork can have more patches than colors
        the color of additional patches will be background (white by defaut) '''
    # we compute the number of lines and columns of the patchwork
    l, c = rectangle_size(len(col_list))

    # we create the ndarray of the colors
    # (each color has an indice from 0 to len(col_list)-1)
    colormap = np.array([col_dict[background]]*l*c, dtype=np.uint8)
    # we assign the array with the colors
    # (additional colors will the backgroud color)
    colormap[0:len(col_list)] = [col_dict[k] for k in col_list]
    
    # the image is a rectangle of (l*side, c*side) of pixels
    # we compute its indices
    i, j = np.indices((l*side, c*side))
    # we pass the indices in the patchwork of l*c patches (i.e. //side)
    I, J = i//side, j//side
    # c*I+J transforms I and J in the corresponding color indices of colormap
    # note that we index the colormap array by a bigger array of indices
    # it is done by vectorization
    return colormap[c*I+J]

colors = [
    'DarkBlue', 'AntiqueWhite', 'LimeGreen',
    'NavajoWhite', 'Tomato', 'DarkGoldenrod',
    'LightGoldenrodYellow', 'OliveDrab',
]
plt.imshow(patchwork(colors, colors_dict, side=50));

# %%
# prune-cell 4.
import random
k = 19
im = patchwork(random.sample(list(colors_dict.keys()), k),
                     colors_dict,
                     side=10)

plt.imshow(im);

# %%
# prune-cell 5.
for s in ['white', 'red']: #, 'blue', 'medium', 'light', 'brown'
    colors = [k for k in colors_dict.keys() if s in k.lower()]
    print(f'{len(colors)} "{s}" colors')
    plt.imshow(patchwork(colors, colors_dict))
    plt.show()

# %%
# prune-cell 6.
im_all = patchwork(list(colors_dict.keys()), colors_dict, side=100)
plt.imshow(im_all);

# %%
# prune-cell 7.
plt.imsave('patchwork-all.jpg', im_all)
plt.show()
pat = plt.imread('patchwork-all.jpg')
plt.imshow(pat);

# %% [markdown]
# ## Somme des valeurs RGB d'une image

# %% [markdown]
# 0. Lisez l'image `les-mines.jpg`
#
# 1. Créez un nouveau tableau `numpy.ndarray` en sommant **avec l'opérateur `+`** les valeurs RGB des pixels de votre image  
#
# 2. Affichez l'image (pas terrible), son maximum et son type
#
# 3. Créez un nouveau tableau `numpy.ndarray` en sommant **avec la fonction d'agrégation `np.sum`** les valeurs RGB des pixels de votre image
#
# 4. Affichez l'image, son maximum et son type
#
# 5. Pourquoi cette différence ? Utilisez le help `np.sum?`
#
# 6. Passez l'image en niveaux de gris de type entiers non-signés 8 bits  
# (de la manière que vous préférez)
#
# 7. Remplacez dans l'image en niveaux de gris,   
# les valeurs >= à 127 par 255 et celles inférieures par 0  
# Affichez l'image avec une carte des couleurs des niveaux de gris  
# vous pouvez utilisez la fonction `numpy.where`
#
# 8. avec la fonction `numpy.unique`  
# regardez les valeurs différentes que vous avez dans votre image en noir et blanc

# %%
# votre code

# %%
# prune-cell 0.
import numpy as np
from matplotlib import pyplot as plt

im = plt.imread('les-mines.jpg')

# 1.

# NOT GOOD !
gr0 = im[:, :, 0] + im[:, :, 1] + im[:, :, 2]


# 2.
print(f"type={gr0.dtype}, max={gr0.max()}") # uint8 -> overflow
# image pas correcte à cause des overflows
plt.imshow(gr0, cmap='gray')
plt.show()

# %%
# prune-cell 3.

# de la manière précédente vous ne pouvez pas obtenir les valeurs
# en niveaux de gris des pixels de l'image, il faudrait faire:
# gr2 = im[:, :, 0]/3 + im[:, :, 1]/3 + im[:, :, 1]/3
# print(gr2.dtype, gr2.max())

gr1 = (np.sum(im, axis=2))

# prune-cell 4.
print(f"type={gr1.dtype}, max={gr1.max()}") # int64 ok


# prune-cell 5.
# # np.sum?
# dtype : dtype, optional
#     The type of the returned array and of the accumulator in which the
#     elements are summed.  The dtype of `a` is used by default unless `a`
#     has an integer dtype of less precision than the default platform
#     integer.  In that case, if `a` is signed then the platform integer
#     is used while if `a` is unsigned then an unsigned integer of the
#     same precision as the platform integer is used.
    
# 6.
plt.imshow(gr1/3, cmap='gray')
plt.show()

# %% {"scrolled": false}
# prune-cell 6.bis

gr2 = (im[:, :, 0]/3 + im[:, :, 1]/3 + im[:, :, 1]/3).astype(np.uint8)
plt.imshow(gr2, cmap='gray')
plt.show()

# prune-cell 7.
gr3 = gr2.copy()
gr3[gr3>=127] = 255
gr3[gr3<127] = 0

# prune-cell 7. avec where
gr3 = np.where(gr2>128, 255, 0)
plt.imshow(gr3, cmap='gray')
plt.show()

# prune-cell 8.
print(np.unique(gr3))



# %% [markdown]
# ## Image en sépia

# %% [markdown]
# Pour passer en sépia les valeurs R, G et B d'un pixel  
# (encodées ici sur un entier non-signé 8 bits)  
#
# 1. on transforme les valeurs `R`, `G` et `B` par la transformation  
# `0.393 * R + 0.769 * G + 0.189 * B`  
# `0.349 * R + 0.686 * G + 0.168 * B`  
# `0.272 * R + 0.534 * G + 0.131 * B`  
# (attention les calculs doivent se faire en flottants pas en uint8  
# pour ne pas avoir, par exemple, 256 devenant 0)  
# 1. puis on seuille les valeurs qui sont plus grandes que `255` à `255`
# 1. naturellement l'image doit être ensuite remise dans un format correct  
# (uint8 ou float entre 0 et 1)

# %% [markdown]
# **Exercice**
#
# 1. Faites une fonction qui prend en argument une image RGB et rend une image RGB sépia  
# la fonction `numpy.dot` doit être utilisée (si besoin, voir l'exemple ci-dessous) 
#
# 1. Passez votre patchwork de couleurs en sépia  
# Lisez le fichier `patchwork-all.jpg` si vous n'avez pas de fichier perso
# 2. Passez l'image `les-mines.jpg` en sépia   

# %%
# votre code

# %% {"scrolled": true}
# INDICE:

# exemple de produit de matrices avec `numpy.dot`
# le help(np.dot) dit: dot(A, B)[i,j,k,m] = sum(A[i,j,:] * B[k,:,m])

i, j, k, m, n = 2, 3, 4, 5, 6
A = np.arange(i*j*k).reshape(i, j, k)
B = np.arange(m*k*n).reshape(m, k, n)

C = A.dot(B)
# or C = np.dot(A, B)

A.shape, B.shape, C.shape

# %%
# prune-cell 1. pas à pas
SEPIA=np.array([[0.393, 0.349, 0.272],
                [0.769, 0.686, 0.534],
                [0.189, 0.168, 0.131]])

img = plt.imread('les-mines.jpg') # dtype = uint8
print(img.dtype)
print(img.shape, SEPIA.shape) # (i, j, 3) (m, 3)

img_SEPIA = img.dot(SEPIA)
# ou img_SEPIA = np.dot(img, SEPIA)
print(img_SEPIA.dtype) # floats64

print(img_SEPIA.min(), img_SEPIA.max()) # de 0 à 344.505

# plt.imshow demande un type correct
# soit uint8 (donc des valeurs entre 0 et 255)
# soit float64 avec des valeurs entre 0 et 1
# (et pas entre 0 et 344.505)
# on doit donc seuiller au dessous de 255 et passer en uint8
img_SEPIA[img_SEPIA>255] = 255
img_SEPIA = img_SEPIA.astype(np.uint8)

plt.imshow(img_SEPIA);


# %%
# prune-cell 1. avec dot()
# dans ce cas de figure on peut aussi bien utiliser
# np.dot ou @ (aka np.matmul)
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html

def sepia(im, SEPIA=np.array([[0.393, 0.349, 0.272],
                              [0.769, 0.686, 0.534],
                              [0.189, 0.168, 0.131]])):
# les deux marchent
    result = np.dot(im, SEPIA) 
#    result = im @ SEPIA
    result[result>255] = 255
    return result.astype(np.uint8)

plt.imshow(
    sepia(plt.imread('les-mines.jpg')));

# %% [markdown]
# prune-cell: comment ça marche ?
#
# la doc dit que
# > `dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])`
#
# dans notre cas:
#
# * a.dim = 3 (`a.shape = lines, cols, 3`), et 
# * b.dim = 2, (`b.shape = 3, 3`), ce qui donne
#
# > `dot(image, SEPIA)[i, j, canal] 
#   = sum(image[i, j, :] * SEPIA[:, canal])`  
#   cqfd $\diamond$

# %% {"cell_style": "center"}
# prune-cell 2.

file = 'patchwork-all.jpg'
im = plt.imread(file)
plt.imshow(sepia(im));

# %%
# prune-cell 3.

im_sepia = sepia(plt.imread('les-mines.jpg'))
plt.imshow(im_sepia)
plt.imsave('les-mines-sepia.jpg', im_sepia)

# %% [markdown]
# ## Exemple de qualité de compression

# %% [markdown]
# 1. Importez la librairie `Image`de `PIL` (pillow)   
# (vous devez peut être installer PIL dans votre environnement)
# 1. Quelle est la taille du fichier 'les-mines.jpg' sur disque ?
# 1. Lisez le fichier 'les-mines.jpg' avec `Image.open` et avec `plt.imread`  
#
# 3. Vérifiez que les valeurs contenues dans les deux objets sont proches
#
# 4. Sauvez (toujours avec de nouveaux noms de fichiers)  
# l'image lue par `imread` avec `plt.imsave`  
# l'image lue par `Image.open` avec `save` et une `quality=100`  
# (`save` s'applique à l'objet créé par `Image.open`)
#
# 5. Quelles sont les tailles de ces deux fichiers sur votre disque ?  
# Que constatez-vous ?
#
# 6. Relisez les deux fichiers créés et affichez avec `plt.imshow` leur différence  

# %%
# votre code

# %%
# prune-cell 1.
from PIL import Image

file = "les-mines.jpg"

# prune-cell 2. - en bash
# %ls -l $file

# prune-cell 2. - en Python pour cross-platform
from pathlib import Path
print(f"{file} {Path(file).stat().st_size} bytes")

# prune-cell 3.
imPLT = plt.imread(file)
imPIL = Image.open(file)
np.all(np.isclose(imPLT, imPIL))

# %%
# prune-cell 4.
plt.imsave(f'{file}-PLT.jpg', imPLT) # no quality
imPIL.save(f'{file}-PIL.jpg', quality=100)

# prune-cell 5.
for ext in ['PLT', 'PIL']:
    print(f"{ext} {Path(f'{file}-{ext}.jpg').stat().st_size} bytes")

# %% {"scrolled": true}
# prune-cell 6.
imPLT_PLT = plt.imread(f"{file}-PLT.jpg")
imPLT_PIL = plt.imread(f"{file}-PIL.jpg")
print(np.all(np.isclose(imPLT_PLT, imPLT_PIL)))
plt.imshow(imPLT_PLT - imPLT_PIL);
