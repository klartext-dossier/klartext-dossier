#!/bin/bash

find . -name "*__i.md" | sed -e "s/i.md//" | xargs -iX python -m dm run -p md-to-html.dm -i Xi.md -o Xo.html
find . -name "*__i.md" | sed -e "s/i.md//" | xargs -iX python -m dm run -p md-to-pdf.dm -i Xi.md -o Xo.pdf