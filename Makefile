.PHONY: subdirs website

subdirs:
	$(MAKE) -C klartext 
	$(MAKE) -C klartext-pygments
	$(MAKE) -C klartext-vscode
	$(MAKE) -C htmlbook install
	$(MAKE) -C mdx
	$(MAKE) -C dossier package test

website:
	mkdocs build