# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt

# %%
import numpy as np

# %% [markdown]
# # exo `cadre`

# %%
c = np.ones(shape=(10, 10), dtype=bool)

# %%
plt.imshow(c);


# %%
def cadre(array, inplace=False):
    if not inplace:
        array = array.copy()
    h, w = array.shape
    array[1::h-3, :] = 0
    array[:, 1::w-3] = 0



# %%
cadre(c)

# %%
plt.imshow(c)
plt.savefig("cadre.png")

# %%
random = np.random.randint(0, 21, dtype=np.uint8, size=(6, 8))

# %%
plt.imshow(random);

# %%
cadre(random)
plt.imshow(random);

# %%
cadre(random, inplace=True)
plt.imshow(random);


# %% [markdown]
# ### tests
#
# * les petites dimensions <= 3
# * le dtype du résultat, si on a fait une copie

# %% [markdown]
# ## exo `cadre2`
#

# %%
# attention à préserver le type

def cadre2(array):
    rows, columns = array.shape
    result = np.zeros((rows+2, columns+2), dtype=array.dtype)
    result[1:-1, 1:-1] = array
    return result


# %%
# without using zeros or ones
def cadre2_bis(array):
    h, w = array.shape
    result = 128*np.empty((h+2, w+2), dtype=array.dtype)
    result[1:-1, 1:-1] = array
    print(f"{h=}")
    result[0::h+1, :] = 0
    result[:, 0::w+1] = 0
    return result


# %%
random2 = np.random.randint(0, 21, dtype=np.uint8, size=(4, 5))

# %%
plt.imshow(random2);

# %%
plt.imshow(cadre2(random2));


# %% [markdown]
# ### tests
#
# * vérifier que le type du résultat (qui cette fois est une copie) est le même que l'entrée
# * ça ne fait pas de mal de vérifier les cas 1 x n, n x 1, 1 x 1
#

# %% [markdown]
# # exo `anti_diagonal`

# %%
# l'idée c'est qu'une fois aplati, la diagonale
# correspond à une slice de pas n-1
# le début c'est n-1
# le dernier, c'est à une distance (n-1) de la fin du tableau
# soit 1-n
# MAIS attention que le pas de n-1 va être nul si n vaut 1

def anti_diagonal(L, dtype=None):
    kwds = {}
    if dtype is not None:
        kwds['dtype'] = dtype
    n = len(L)
    # avec une seule valeur, la formule générale
    # nous donne une slice avec un pas .. de 0
    # ça ne fonctionne pas, il faut traiter ce cas à part
    if n == 1:
        return np.array([L], **kwds)
    result = np.zeros(n*n, dtype = dtype)
    result[n-1 : 1-n : n-1] = L
    return result.reshape((n, n))


# %%
anti_diagonal([1, 2, 3, 4])

# %%
anti_diagonal([1, 2, 3])

# %%
# et cette fois
anti_diagonal([1, 2], dtype=np.uint8)

# %%
# et
anti_diagonal([1])


# %% [markdown]
# ## les générateurs

# %%
# une fonction génératrice
def squares(n):
    for i in range(n):
        yield i*2

squares1 = squares(5)

# %%
squares2 = (i**2 for i in range(1, 5))

# %%
type(squares1), type(squares2)

# %%
# on ne peut pas appeler len() ici car c'est un générateur
try:
    len(squares2)
except Exception as exc:
    print(f"OOPS, {type(exc)}: {exc}")

# %%
# et du coup
try:
    anti_diagonal(squares2)
except Exception as exc:
    print(f"OOPS, {type(exc)}: {exc}")

# %% [markdown]
# ### comment faire du coup ?
#
# comment pourrait-on arranger notre fonction pour qu'elle puisse fonctionner avec un générateur ?
#
# ```
#     L = list(L)    # ajouter cette ligne
#     n = len(L)
# ```
#
# *take home message*
# les types en Python (ici `list`) sont des usines à objet qui permettent de convertir dans le type en question

# %% [markdown]
# ### les générateurs sont des objets bizarres

# %%
squares2 = (x**2 for x in range(5))

# %%
# la première fois qu'on itère dessus, tout va bien
for x in squares2:
    print(x)

# %%
# par contre la deuxième fois, il est vide !
for x in squares2:
    print(x)

# %%
# par contre on peut avec un range()
# qui est techniquement un truc hybride, pas tout à fait un itérateur
r = range(4)

# %%
for i in r:
    print(x)

# %%
# on peut itérer plusieurs fois sur un range (ce n'est pas exactement un itérateur)

for i in r:
    print(x)
