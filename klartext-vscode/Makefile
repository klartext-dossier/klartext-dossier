all: package

package:
	vsce package
	mkdir -p dist
	cp klartext-*.vsix dist/
	
.PHONY: package