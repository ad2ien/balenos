# Baleinos

🇫🇷 [Guide en francais](README-fr.md) 🥖

This repo holds assets, scripts and documentation of a [Lubuntu](https://lubuntu.me/) customization meant to be used by french administration or associations that want to offer their users a self attending station for administrative procedures.

## Features

### Users

- Be able to use a web browser
  - that respects privacy
  - Smooth UX thanks to good performance
- A button for deleting all traces of the user's visit.

### Admin

- To be able to use an aging PC
- Be able to configure the station to best suit the context of use while preventing end-users from modifying these settings:
  - edit bookmarks
  - white or black lists of websites
  - set home page, default search tool...

## Install guide

- Install lubuntu <https://lubuntu.me/downloads/>
  - french locale
  - no encryption
  - create `admin` user with a secured password

- login to admin
- copy the content of this repo in admin home directory
- start a terminal and `cd baleinos`
- run `chmod +x install-baleinos.sh && ./install-baleinos.sh`

## Configure bookmarks

- log in as admin
- start Firefox
- create and organize bookmarks as you want them to appear to users
- close Firefox
- click on the `Bookmarks transfer` shortcut on the desktop
