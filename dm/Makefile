all: package

package:
	python -m build --sdist
	python -m build --wheel

test: 
	mkdir -p build/test-reports	
	(export PYTHONPATH=../../../klartext:../../../mdx:../..; cd test/convert-htmlbook; behave -D toolsdir=../../dm/Tools --junit --junit-directory ../../build/test-reports --no-logcapture --no-capture-stderr --no-capture)
	(export PYTHONPATH=../../../klartext:../../../mdx:../..; cd test/convert-markdown; behave -D toolsdir=../../dm/Tools --junit --junit-directory ../../build/test-reports --no-logcapture --no-capture-stderr --no-capture)
	(export PYTHONPATH=../../../klartext:../../../mdx:../..; cd test/convert-klartext; behave -D toolsdir=../../dm/Tools --junit --junit-directory ../../build/test-reports --no-logcapture --no-capture-stderr --no-capture)
	(export PYTHONPATH=../../../klartext:../../../mdx:../..; cd test/run-pipeline; behave -D toolsdir=../../dm/Tools --junit --junit-directory ../../build/test-reports --no-logcapture --no-capture-stderr --no-capture)

.PHONY: package test