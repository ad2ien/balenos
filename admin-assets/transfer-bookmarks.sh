#!/bin/bash
set -e

# This Baleinos script transfers the current places.sqlite to the defined $USER firefox session
# Will probably only work for Lubuntu

TARGET_USER=personne
echo "🐳 copy bookmarks for user $TARGET_USER..."


# get firefox paths
SRC_FIREFOX_FOLDER=$(ls ~/snap/firefox/common/.mozilla/firefox/ | grep .default)
echo "Source Firefox folder $SRC_FIREFOX_FOLDER"
SRC_FIREFOX_PATH="/home/$(whoami)/snap/firefox/common/.mozilla/firefox/$SRC_FIREFOX_FOLDER"

DEST_FIREFOX_FOLDER=$(sudo ls /home/$TARGET_USER/snap/firefox/common/.mozilla/firefox/ | grep .default)
echo "Destination Firefox folder $DEST_FIREFOX_FOLDER"
DEST_FIREFOX_PATH="/home/$TARGET_USER/snap/firefox/common/.mozilla/firefox/$DEST_FIREFOX_FOLDER"

echo "Backup places.sqlit.bkp"
sudo cp -f $DEST_FIREFOX_PATH/places.sqlite $DEST_FIREFOX_PATH/places.sqlite.bkp
sudo cp $SRC_FIREFOX_PATH/places.sqlite $DEST_FIREFOX_PATH/places.sqlite
sudo chown $TARGET_USER:$TARGET_USER $DEST_FIREFOX_PATH/places.sqlite

echo "start firefox..."
sudo -i -u $TARGET_USER firefox &

echo "done ✅"
