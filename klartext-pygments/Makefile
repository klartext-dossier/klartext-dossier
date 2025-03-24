all: package

package:
	hatch build
	
test:
	python -m pygments -x -l src/klartext-lexer.py:KlartextLexer test.kt
	
.PHONY: package test