#!/bin/bash
set -e

echo " -- Baleinos user install --"

# Desktop environment
mkdir -p ~/.config/autostart
mv baleinos-assets/firefox.desktop ~/.config/autostart/firefox.desktop
mv baleinos-assets/reset-session.sh ~/reset-session.sh
chmod +x ~/reset-session.sh
mv baleinos-assets/reset-session.desktop ~/Desktop/reset-session.desktop

# configure tray
cp baleinos-assets/panel.conf ~/.config/lxqt/

# TODO not locale agnostic, osef! 
rm -rf ~/Images
rm -rf ~/Musique
rm -rf ~/Vidéos
rm -rf ~/Modèles

rm -f ~/Desktop/user-home.desktop 
rm -f ~/Desktop/network.desktop
rm -f ~/Desktop/lubuntu-manual.desktop
