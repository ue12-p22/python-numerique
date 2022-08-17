NOTEBOOKS = $(shell git ls-files .teacher/[1-9]*)

all: style

include Makefile.style

include Makefile.norm

include Makefile.prune

########## BOOK
book:
	jupyter-book build .



.PHONY: all norm style prune book
