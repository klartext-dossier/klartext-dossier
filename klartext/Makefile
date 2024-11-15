all: package test

package:
	python -m build --sdist
	python -m build --wheel

test:
	py.test test
	mkdir -p build/test-reports	
	(export PYTHONPATH=../../klartext:../../mdx; cd test; behave --junit --junit-directory ../build/test-reports --no-logcapture --no-capture-stderr --no-capture)
	
.PHONY: package test