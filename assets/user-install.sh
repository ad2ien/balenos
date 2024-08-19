#!/bin/bash
set -e

echo " -- Balenos user install --"

# Desktop environment
mkdir -p ~/.config/autostart
mv balenos-assets/firefox.desktop ~/.config/autostart/firefox.desktop
mv balenos-assets/reset-session.sh ~/reset-session.sh
chmod +x ~/reset-session.sh
mv balenos-assets/reset-session.desktop ~/Desktop/reset-session.desktop

# configure tray
cp balenos-assets/panel.conf ~/.config/lxqt/

# TODO not locale agnostic, osef! 
rm -rf ~/Images
rm -rf ~/Musique
rm -rf ~/Vidéos
rm -rf ~/Modèles

rm -f ~/Desktop/user-home.desktop 
rm -f ~/Desktop/network.desktop
rm -f ~/Desktop/lubuntu-manual.desktop
