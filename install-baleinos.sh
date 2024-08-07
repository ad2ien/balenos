#!/bin/bash
set -e

USER_NAME=personne
PASSWORD=$USER_NAME

echo "// Welcome to Baleinos installation 🐳"

# if user don't exists
if id -u $USER_NAME > /dev/null 2>&1; then
  echo "Utilisateur créé : étape suivante"
else
  # create user and start firefox for the first time
  sudo adduser --quiet --disabled-password --shell /bin/bash --gecos $USER_NAME $USER_NAME
  echo "$USER_NAME:$PASSWORD" | sudo chpasswd

  sudo -i -u $USER_NAME bash << EOF
    firefox &
EOF
  echo "Démarrez un session en tant que '$USER_NAME'"
  echo "  - Démarrer / quitter / déconnecter"
  echo "  - Sélectionner '$USER_NAME' (mot de passe: '$PASSWORD')"
  echo "  - Démarrer / quitter / déconnecter / Se connecter en tant qu'admin"
  echo "  - Relancer ensuite ce script pour finir l'installation'"
  exit 0
fi

echo "Auto login"
echo "[Autologin]
User=$USER_NAME
Session=Lubuntu
" > sddm.conf
sudo cp -f sddm.conf /etc/sddm.conf

echo "copy assets, and set rights..."
sudo mkdir -p /home/$USER_NAME/baleinos-assets
sudo cp assets/* /home/$USER_NAME/baleinos-assets/
sudo cp assets/user-*.sh /home/$USER_NAME/
sudo chown -R $USER_NAME:$PASSWORD /home/$USER_NAME/
sudo chmod +x /home/$USER_NAME/user-install.sh
sudo chmod +x /home/$USER_NAME/user-config-firefox.sh

echo "Execute configuration scripts for the final user..."
sudo -i -u $USER_NAME ./user-install.sh
sudo -i -u $USER_NAME ./user-config-firefox.sh

echo "// Fin, so far... 👋"
