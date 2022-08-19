#!/usr/bin/env bash

set -ex
rm -rf /build/GrabSCR.AppDir
cp -r /appdir /build/GrabSCR.AppDir
mkdir -p /build/GrabSCR.AppDir/opt
cp -r /build/app /build/GrabSCR.AppDir/opt/grabscr

appimagetool /build/GrabSCR.AppDir
mv ./GrabSCR-x86_64.AppImage /dist/GrabSCR-x86_64.AppImage
