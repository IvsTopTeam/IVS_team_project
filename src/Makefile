MAIN=calc_main.py
LIBRARY=our_library.py
TESTS=LibraryTests.py
DOC=doc
PROFILE=stddev.py
INSTALL=installer.sh
INSTALLER=topteamcalc-1.0.deb
FILE_NAME=xnovak2x_xbubak01_xkozub06_xklime47

.PHONY:
	all
	setup
	pack
	clean
	test
	doc
	run
	profile
	installer


all: setup run

setup:
	sudo apt-get install python3-pip
	sudo -H pip3 install pyqt5
	sudo -H pip3 install pyqt5-sip
	sudo -H pip3 install pyinstaller


pack: clean

	mkdir -p ../../$(FILE_NAME)/repo
	cp -r ../. ../../$(FILE_NAME)/repo

	make doc
	mv ./$(DOC) ../../$(FILE_NAME)

	make installer
	mv ../installer/$(INSTALLER) ../../$(FILE_NAME)

	cd ../../ && zip -r $(FILE_NAME).zip $(FILE_NAME)

	rm -rf ../../$(FILE_NAME)


clean:
	rm -rf __pycache__ $(DOC)

cleanall: clean
	rm -rf ../../IVS_team_project

test: $(TESTS) $(LIBRARY)
	python3 $(TESTS)

doc: clean Doxyfile
	doxygen

run: $(MAIN)
	python3 $(MAIN)

profile: $(PROFILE)
	python3 $(PROFILE)

installer: $(INSTALL)
	chmod +x $(INSTALL)
	bash $(INSTALL)

