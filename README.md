# Baleinos

![Gitmoji](https://img.shields.io/badge/gitmoji-%20%F0%9F%98%9C%20%F0%9F%98%8D-FFDD67.svg)
![License](https://img.shields.io/badge/license-GNU-blue.svg?logo=GNU)

🇫🇷 [Guide en francais](README-fr.md) 🥖

This repo holds assets, scripts and documentation of a [Lubuntu](https://lubuntu.me/) customization meant to be used by french administration or associations that want to offer their users a self attending station for administrative procedures.

## Use cases

### For the users

- be able to use a web browser
  - that respects privacy
  - that has a smooth UX thanks to good performance
- has a button somewhere to delete all traces of the user's visit.

### For the admins

- to be able to use an aging PC
- be able to configure the station to best suit the context of use while preventing end-users from modifying the settings like:
  - bookmarks
  - home page, default search tool...
- be able to set white or black lists of websites
- easily do some further customization : install apps, change UI...

## How does it work?

- the [install script](install-baleinos.sh) creates a linux user that will be auto logged in.
- the taskbar and desktop is simplified
- a private Firefox is launched at startup
- on the admin account, [Baleinos admin tool](admin-assets/baleinos-admin-app/README.md) is installed

## How to use

### Install

- Install lubuntu <https://lubuntu.me/downloads/>
  - french locale
  - no encryption
  - create `admin` user with a secured password

- login to admin
- copy the content of this repo in admin home directory
- start a terminal and `cd baleinos`
- run `chmod +x install-baleinos.sh && ./install-baleinos.sh`

### Configure Firefox

- You can configure the homepage and search engine thanks to [Baleinos admin app](admin-assets/baleinos-admin-app/README.md)
- To customize further use the file `/etc/firefox/policies/policies.json` <https://mozilla.github.io/policy-templates/>

### Configure bookmarks

- log in as admin
- start Firefox
- create and organize bookmarks as you want them to appear to users
- close Firefox
- launch the administration application _Baleinos admin app_ and click on _transférer les marque-pages_ button

## How to contribute ❤️

- A star would cheer me up ⭐
- If this repo can be of any use to you, I would really value your insights and specific requirements, maybe by email : _contact_ at _ad2ien.dev_
- Any complain or dev request can be discussed in the issues
