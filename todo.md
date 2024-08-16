# Baleinos TODO list

## General

- [x] how to contribute

## A scripter

- [x] créer user `personne` pas de groupe
- [x] add `User=personne` in `/etc/sddm.conf`
- [x] get user.js et paste in `/home/personne/snap/firefox/common/.mozilla/firefox/xxx.default`
- [x] Install Block Site addon
- [x] copy firefox.desktop to .config/autostart
- [x] copy .reset-session.sh
- [x] copy reset-session.desktop dans desktop
- [x] supprimer Image, public, Vidéos folders
- [x] supprimer tous les autres raccourcis desktop: user-home.desktop, network.desktop, lubuntu-manual.desktop
- [x] un bureau
- [x] Racourci reset session

### Admin config

- [x] Bookmarks
  - [x] Editer en tant qu’admin puis importer
  - [x] <https://gist.github.com/iafisher/d624c04940fa46c6d9afb26cb1bf222at>
  - [ ] bloquer edition de racourcis
  - [ ] icone pour admin app
  - [x] save `places.sqlite` somewhere
- [x] Homepage
- [ ] white or black list doc
- [ ] Baleinos admin markdown guide shortcut
- [ ] config homepage and search engine from admin

## Bouton reset session

- [x] vider session Firefox
- [x] reset Downloads and Documents folder
- [ ] warning message
- [ ] un icône pour le bouton reset

## Configuration Firefox

- [x] restrict user preferences / bookmarks / addons
- [x] homepage
- [x] toolbar / favorites / bookmarks
- [x] passwords
- [x] white / black list → Block Site addon
- [ ] clean interface : unwanted menus and stuffs
- [x] search engine
- [ ] firefox search drop down relou
  - [x] <https://mozilla.github.io/policy-templates/#managedbookmarks>
- [x] Install extension with policies <https://mozilla.github.io/policy-templates/#extensions>
- [ ] white et black list avec policies

## Config linux session

- [x] Firefox by default
- [x] don’t allow install or execute other stuff
- [x] auto login
- [ ] fond d'écran
- [ ] read only on critical files user.js
- [ ] ransacking tests

Protect everything but Download Documents?

- [x] Scripter configuration du bureau
  - [x] Racourcis vers reset session
  - [x] Un seul bureau

## user.js

<https://brainfucksec.github.io/firefox-hardening-guide>
[user.js](./user.js)

## Long range

- [ ] New linux distri with specific installer
