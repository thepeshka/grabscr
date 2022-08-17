#!/usr/bin/env bash

set -ex

cp -r /src /build/src
pyinstaller --add-data 'src/icon.png:.' -n GrabSCR -p /build/src -y /build/src/main.py

rm -rf /build/GrabSCR.AppDir
cp -r /appdir /build/GrabSCR.AppDir
mkdir -p /build/GrabSCR.AppDir/opt
cp -r /build/dist/GrabSCR /build/GrabSCR.AppDir/opt/grabscr

appimagetool /build/GrabSCR.AppDir
mv ./GrabSCR-x86_64.AppImage /dist/GrabSCR-x86_64.AppImage
