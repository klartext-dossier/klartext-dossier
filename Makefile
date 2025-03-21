.PHONY: subdirs

subdirs:
	$(MAKE) -C klartext 
	$(MAKE) -C htmlbook install
	$(MAKE) -C mdx
	$(MAKE) -C dossier package test 

website:
	mkdocs build