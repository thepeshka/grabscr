#!/usr/bin/env bash

set -e

VERSION=0.0.2

pyinstaller --add-data 'icon.png:.' --add-data 'grabscr.desktop:.' --add-data 'uninstall.sh:.' -n GrabSCR -y grabscr.py
cd dist || exit
zip -r -o ./GrabSCR-$VERSION.zip ./GrabSCR
