PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR:=$(CURDIR)
INPUTDIR?=$(BASEDIR)/content
OUTPUTDIR?=$(BASEDIR)/output
CONFFILE?=$(BASEDIR)/pelicanconf.py
PUBLISHCONF?=$(BASEDIR)/publishconf.py

PORT?=8000
SERVER?=0.0.0.0

help:
	@echo 'Makefile for www.sigsegv.tech                                                    '
	@echo '                                                                                 '
	@echo 'Usage:                                                                           '
	@echo '   make html                                  (re)generate the web site          '
	@echo '   make clean                                 remove the generated files         '
	@echo '   make regenerate                            regenerate files upon modification '
	@echo '   make publish                               generate using production settings '
	@echo '   make serve [PORT=8000] [SERVER=0.0.0.0]    serve site at http://localhost:8000'
	@echo '                                                                                 '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT) $(SERVER)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

.PHONY: html help clean regenerate serve publish
