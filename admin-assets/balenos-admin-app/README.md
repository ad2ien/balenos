# Balenos admin app

Manage and edit Firefox policies in `/etc/firefox/policies/policies.json` <https://mozilla.github.io/policy-templates/> for ubuntu distributions

- Set homepage and search engine
- activate or deactivate Firefox policies for all users
- Transfer bookmarks to another user

## Dev

- This is python Qt application
- form.ui is edited with [QtCreator](https://doc.qt.io)

## Start

By running [./start_balenos_admin_tool.sh](start_balenos_admin_tool.sh) after `chmod +x start_balenos_admin_tool.sh`

## TODO

- [ ] doc inside the app
- [ ] better way to input sudo pw
- [ ] icon
- [ ] emojis on the UI 😿
- [ ] quit / about menu
- [ ] app name instead of "python" in task bar
- [ ] separate repo : test, lint, releases...
- [ ] admin should be able to backup and restore a config