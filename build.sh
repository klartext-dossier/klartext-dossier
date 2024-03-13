#!/bin/bash

set -e -v

TOPDIR=$PWD
export PYTHONPATH=$TOPDIR/Source:$TOPDIR/Test
TOOLS=$TOPDIR/Source/dm/Tools

FAIL="False"

cd $TOOLS/css
lessc htmlbook.less htmlbook.css
lessc htmlbook-syntax.less htmlbook-syntax.css

cd $TOPDIR/Source
python setup.py bdist_wheel

cd $TOPDIR/Test/convert-htmlbook
behave -D toolsdir=$TOOLS --junit --junit-directory $TOPDIR/Test/test-reports --no-logcapture --no-capture-stderr --no-capture

cd $TOPDIR/Test/convert-klartext
behave -D toolsdir=$TOOLS --junit --junit-directory $TOPDIR/Test/test-reports --no-logcapture --no-capture-stderr --no-capture

cd $TOPDIR/Test/convert-markdown
behave -D toolsdir=$TOOLS --junit --junit-directory $TOPDIR/Test/test-reports --no-logcapture --no-capture-stderr --no-capture

cd $TOPDIR/Test/run-pipeline
behave -D toolsdir=$TOOLS --junit --junit-directory $TOPDIR/Test/test-reports --no-logcapture --no-capture-stderr --no-capture

cp $TOPDIR/Source/dist/dossier-*-py3-none-any.whl $TOPDIR/Source/docker

cd $TOPDIR
