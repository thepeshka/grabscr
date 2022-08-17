#!/usr/bin/env bash

docker-compose up --build
VERSION=$(python -c "import src; print(src.__version__)")
mv ./dist/GrabSCR-x86_64.AppImage ./dist/GrabSCR-$VERSION-x86_64.AppImage