#!/usr/bin/env bash

INSTALL_PATH="$HOME/.local/share/GrabSCR"

echo "Installer will ask you to enter password to remove symbolic link"
sudo rm -f /usr/local/bin/grabscr
echo "Remove desktop entry"
rm -f ~/.local/share/applications/grabscr.desktop
echo "Remove icon"
rm -f ~/.icons/grabscr.png

set -e
echo "Remove installation"
rm -rf $INSTALL_PATH

echo "GrabSCR successfully uninstalled!"
