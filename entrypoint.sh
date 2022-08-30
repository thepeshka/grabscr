#!/usr/bin/env bash

pyinstaller --add-data '/build/grabscr/icon.png:.' -n GrabSCR -p "/build/grabscr" -y /build/grabscr/main.py
appimage-builder
cp ./*.AppImage /build/appimage-dist
cp ./*.AppImage.zsync /build/appimage-dist