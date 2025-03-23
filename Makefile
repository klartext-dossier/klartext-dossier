.PHONY: subdirs

subdirs:
	$(MAKE) -C klartext 
	$(MAKE) -C klartext_pygments
	$(MAKE) -C htmlbook install
	$(MAKE) -C mdx
	$(MAKE) -C dossier package test 

website:
	mkdocs build