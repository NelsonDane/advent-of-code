# Makefile for C#

CSC = mcs
SOURCE = $(wildcard *.cs)
EXE = $(SOURCE:.cs=.exe)

.PHONY: all
all: $(EXE)

%.exe: %.cs
	$(CSC) -out:$@ $<

.PHONY: e
e: $(EXE)
	mono $(EXE) e

.PHONY: r
r: $(EXE)
	mono $(EXE)

.PHONY: clean
clean:
	rm -f $(EXE)

.PHONY: all clean
