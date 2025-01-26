all: less

less: *.less
	lessc htmlbook.less htmlbook.css
	lessc htmlbook-syntax.less htmlbook-syntax.css

install: less
	cp *.css ../dossier/dm/Tools/css
	mkdir -p ../dossier/dm/Tools/less
	cp *.less ../dossier/dm/Tools/less