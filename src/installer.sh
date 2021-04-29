#!/bin/sh

pyinstaller calc_main.py -F
cp -f ./specfile/calc_main.spec calc_main.spec
pyinstaller calc_main.spec
cp -f ./dist/ttcalc ../installer/usr/bin
rm -rf dist
rm -rf build
rm calc_main.spec
cd ..
dpkg --build ./installer
mv installer.deb topteamcalc-1.0.deb
mv topteamcalc-1.0.deb ./installer

