#!/usr/bin/env bash

set -e

INSTALL_PATH="$HOME/.local/share/GrabSCR"
VERSION="0.0.7"

mkdir -p "$INSTALL_PATH"

cd "$HOME/.local/share"

echo "Installing GrabSCR $VERSION into $INSTALL_PATH"

wget -qO release.zip https://github.com/thepeshka/grabscr/releases/download/v$VERSION/GrabSCR-linux-$VERSION.zip
unzip ./release.zip
rm -f ./release.zip

echo "Installer will ask you to enter password to create symbolic link so you can run GrabSCR anywhere in your system"
sudo ln -s "$INSTALL_PATH/GrabSCR" /usr/local/bin/grabscr
echo "Copying Desktop entry"
cp "$INSTALL_PATH/grabscr.desktop" ~/.local/share/applications/grabscr.desktop
echo "Copying icon"
cp "$INSTALL_PATH/icon.png" ~/.icons/grabscr.png
echo "Installing xclip if not installed"
which xclip || sudo apt-get install xclip

echo "GrabSCR successfully installed! Now you can use Application entry or grabscr command"
echo "Use $INSTALL_PATH/uninstall.sh to uninstall"
