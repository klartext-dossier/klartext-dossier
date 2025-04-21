all: less

less: *.less
	lessc htmlbook.less htmlbook.css
	lessc htmlbook-syntax.less htmlbook-syntax.css

install: less
	cp *.css ../../dm/dm/Tools/css
	mkdir -p ../../dm/dm/Tools/less
	cp *.less ../../dm/dm/Tools/less