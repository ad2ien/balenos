#!/bin/bash
set -e

USER_NAME=personne
PASSWORD=$USER_NAME

# if user don't exists
if id -u $USER_NAME > /dev/null 2>&1; then
  echo "Utilisateur, créé : étape suivante"
else
  # create user
  sudo adduser --quiet --disabled-password --shell /bin/bash --gecos $USER_NAME $USER_NAME
  echo "$USER_NAME:$PASSWORD" | sudo chpasswd
  echo "Démarrez un session en tant que '$USER_NAME'"
  echo "  - Démarrer / quitter / déconnecter"
  echo "  - Sélectionner '$USER_NAME' (mot de passe: '$USER_NAME')"
  echo "  - Démarrer Firefox"
  exit 0
fi

# Create sddm.conf file
echo "[Autologin]
User=$USER_NAME
Session=Lubuntu
" > sddm.conf

sudo cp -f sddm.conf /etc/sddm.conf

# Firefox config
FIREFOX_FOLDER=$(sudo ls /home/$USER_NAME/snap/firefox/common/.mozilla/firefox/ | grep .default)
FIREFOX_PATH="/home/$USER_NAME/snap/firefox/common/.mozilla/firefox/$FIREFOX_FOLDER"
echo "Firefox path $FIREFOX_PATH"
sudo cp assets/user.js $FIREFOX_PATH
curl --output block_website-0.5.2.1.xpi https://addons.mozilla.org/firefox/downloads/file/4296891/block_website-0.5.2.1.xpi
sudo cp block_website-0.5.2.1.xpi $FIREFOX_PATH/extensions/

# Desktop environment
sudo mkdir -p /home/$USER_NAME/.config/autostart
sudo cp assets/firefox.desktop /home/$USER_NAME/.config/autostart/firefox.desktop
sudo cp assets/reset-session.sh /home/$USER_NAME/reset-session.sh
sudo cp assets/reset-session.desktop /home/$USER_NAME/desktop/reset-session.desktop

# configure tray
sudo cp assets/panel.conf /home/$USER_NAME/.config/lxqt/

# TODO not locale agnostic, osef! 
sudo rm -rf /home/$USER_NAME/Images
sudo rm -rf /home/$USER_NAME/Musique
sudo rm -rf /home/$USER_NAME/Vidéos
sudo rm -rf /home/$USER_NAME/Modèles

sudo rm -f /home/$USER_NAME/desktop/user-home.desktop 
sudo rm -f /home/$USER_NAME/desktop/network.desktop
sudo rm -f /home/$USER_NAME/desktop/lubuntu-manual.desktop
