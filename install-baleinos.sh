#!/bin/bash
set -e

USER_NAME=personne
PASSWORD=$USER_NAME

# create user
sudo adduser --quiet --disabled-password --shell /bin/bash --gecos $USER_NAME $USER_NAME

echo "$USER_NAME:$PASSWORD" | sudo chpasswd

# Create sddm.conf file
echo "[Autologin]
User=$USER_NAME
Session=Lubuntu
" > sddm.conf

sudo cp -f sddm.conf /etc/sddm.conf

# Firefox config
curl --output block_website-0.5.2.1.xpi    https://addons.mozilla.org/firefox/downloads/file/4296891/block_website-0.5.2.1.xpi
sudo cp assets/user.js /home/$USER_NAME/snap/firefox/common/.mozilla/firefox/*.default/

sudo cp block_website-0.5.2.1.xpi /home/$USER_NAME/snap/firefox/common/.mozilla/firefox/*.default/extensions/

# Desktop environment
sudo cp assets/firefox.desktop /home/$USER_NAME/.config/autostart
sudo cp assets/reset-session.sh /home/$USER_NAME/
sudo cp assets/reset-session.desktop /home/$USER_NAME/desktop

# configure tray
sudo cp assets/panel.conf /home/$USER_NAME/.config/lxqt/

# TODO not locale agnostic, osef! 
sudo rm -rf /home/$USER_NAME/Images
sudo rm -rf /home/$USER_NAME/Musique
sudo rm -rf /home/$USER_NAME/Vidéos
sudo rm -rf /home/$USER_NAME/Modèles

sudo rm -r /home/$USER_NAME/desktop/user-home.desktop 
sudo rm -r /home/$USER_NAME/desktop/network.desktop
sudo rm -r /home/$USER_NAME/desktop/lubuntu-manual.desktop
