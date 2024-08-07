#!/bin/bash
set -e

echo " -- Baleinos firefox config --"

# Firefox config
FIREFOX_FOLDER=$(ls ~/snap/firefox/common/.mozilla/firefox/ | grep .default)
echo "Firefox folder $FIREFOX_FOLDER"
FIREFOX_PATH="/home/$(whoami)/snap/firefox/common/.mozilla/firefox/$FIREFOX_FOLDER"
cp baleinos-assets/user.js $FIREFOX_PATH/user.js
cp baleinos-assets/addons.json $FIREFOX_PATH/addons.json
curl --output block_website-0.5.2.1.xpi https://addons.mozilla.org/firefox/downloads/file/4296891/block_website-0.5.2.1.xpi
cp block_website-0.5.2.1.xpi $FIREFOX_PATH/extensions/{54e2eb33-18eb-46ad-a4e4-1329c29f6e17}.xpi
