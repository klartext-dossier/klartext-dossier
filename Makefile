.PHONY: subdirs

subdirs:
	$(MAKE) -C klartext 
	$(MAKE) -C htmlbook install
	$(MAKE) -C mdx
	$(MAKE) -C dossier package test 

website:
	mkdocs build -f klartext/mkdocs.yml && mv klartext/site docs/klartext
	mkdocs build -f mdx/mkdocs.yml
	# mkdocs build -f dossier/mkdocs.yml