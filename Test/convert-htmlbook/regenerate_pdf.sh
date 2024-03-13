#!/bin/bash

find . -name "*__o.html" | sed -e "s/o.html//" | xargs -iX python -m dm run -p html-to-pdf.dm -i Xo.html -o Xo.pdf