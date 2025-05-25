all: package

package:
	hatch build
	
test:
	python -m pygments -x -l klartext_pygments/lexer.py:KlartextLexer test.kt
	
.PHONY: package test