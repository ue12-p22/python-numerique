NOTEBOOKS = $(shell git ls-files [0-9]*)

all: style

########## STYLE
# we need 2 forms:
# for jupyterbook, _static/style.css is a pure CSS file
# the local variant style.html is derived from the former
# but embedded in a <style> tag
style: _static/style.html

_static/style.html: _static/style.css
	(echo '<style>'; \
	cat $^ | sed -n '/^\/\*.*\*\//!p' | sed -n '/ \/\/.*/!p' | sed 's|/\*|\n&|g;s|*/|&\n|g' | sed '/\/\*/,/*\//d'; \
	echo '</style>') > $@



########## NORMALIZING
# is about applying applying the contents
# of .style and .license, and set nbhosting.title metadata
# nbnorm currently is not pip-installable
# and is a part of https://github.com/flotpython/tools
# -l1: use 1st cell as the the license cell
# -s2: use 2nd cell as the style cell
# -t h1: use the first header1 to fill in nbhosting.title
norm:
	nbnorm -l1 -s2 -t h1 $(NOTEBOOKS)


########## BOOK
book:
	jupyter-book build .



.PHONY: all norm style book
