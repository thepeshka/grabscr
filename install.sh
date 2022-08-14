#!/usr/bin/env bash

set -e

INSTALL_PATH="$HOME/.local/share/GrabSCR"
VERSION="0.0.5"

mkdir -p "$INSTALL_PATH"

cd "$HOME/.local/share"

wget -qO release.zip https://github.com/thepeshka/grabscr/releases/download/v$VERSION/GrabSCR-$VERSION.zip
unzip ./release.zip
rm -f ./release.zip

echo "Installer will ask you to enter password to create symbolic link so you can run GrabSCR anywhere in your system"
sudo ln -s "$INSTALL_PATH/GrabSCR" /usr/local/bin/grabscr
cp "$INSTALL_PATH/grabscr.desktop" ~/.local/share/applications/grabscr.desktop
cp "$INSTALL_PATH/icon.png" ~/.icons/grabscr.png

echo "GrabSCR successfully installed! Now you can use Application entry or grabscr command"
echo "Use $INSTALL_PATH/uninstall.sh to uninstall"
