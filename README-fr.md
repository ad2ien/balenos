# Balenos

![Gitmoji](https://img.shields.io/badge/gitmoji-%20%F0%9F%98%9C%20%F0%9F%98%8D-FFDD67.svg)
![License](https://img.shields.io/badge/license-GNU-blue.svg?logo=GNU)

Ce dépôt contient les assets, scripts et documentation d'une customisation de [Lubuntu](https://lubuntu.me/) conçue pour être utilisée par des structures qui souhaitent proposer à leurs utilisateurices une station auto-service d'accès à internet.

## Cas d'usage

### Pour les utilisateurices

- Pouvoir disposer d'un navigateur internet
  - respectant la vie privée
  - UX fluide grace à des performances correctes
- Avoir à disposition un bouton qui permet d'effacer toute trace de son passage

### Pour les admins

- Pouvoir utiliser un PC vieillissant
- Pouvoir configurer la station pour s'adapter au mieux au contexte d'utilisation. Tout en empêchant les utilisateurs finaux de modifier les réglages tels que:
  - les marques pages
  - la page d'accueil, outil de recherche par défaut...
- avoir la possibilité d'avoir des white ou black listes de sites
- pouvoir facilement ajouter des customisations, installer des application, changer l'interface...

## Comment ça marche ?

- le [script d'installation](install-balenos.sh) crée un utilisateur linux qui sera automatiquement connecté
- la barre des tâches et le bureau sont simplifiés
- un Firefox en navigation privé est lancé au démarrage
- sur le compte administrateur, [l'outil d'administration Balenos](admin-assets/balenos-admin-app/README.md) est installé

## Comment utiliser

- Installez Lubuntu <https://lubuntu.me/downloads/>
  - langue française
  - sans chiffrement du disque
  - créez un utilisateur `admin` avec un mot de passe sécurisé
- Connectez-vous avec l'utilisateur admin
- Copiez le contenu de ce dépôt dans le répertoire personnel d'admin
- Ouvrez un terminal `CTRL + ALT + T` et tapez `cd balenos`
- Exécutez `chmod +x install-balenos.sh && ./install-balenos.sh`
- Suivez les instructions

### Configurer Firefox

- Vous pouvez configurer la page d'accueil et le moteur de recherche grâce à [Balenos admin app](admin-assets/balenos-admin-app/README.md) un raccourcis est présent sur le Bureau
- Pour personnaliser davantage, utilisez le fichier `/etc/firefox/policies/policies.json` <https://mozilla.github.io/policy-templates/>

### Configurer les marque-pages

- connectez vous en tant qu'admin
- démarrez Firefox
- créez et organisez les raccourcis comme vous voulez qu'ils apparaissent pour les utilisateurices
- fermez Firefox
- lancez l'application d'administration _Balenos admin app_ et cliquez sur le bouton _transférer les marque-pages_

### Configurer le contrôle parental

Le script d'installation installe un système de contrôle parental : <https://gitlab.com/ctparentalgroup/CTparental/>. Il est possible d'affiner la blacklist depuis là : <https://admin.ct.local/>

## Point de vue juridique

L'avis de la Quadrature du net à ce sujet : <https://www.laquadrature.net/2018/01/31/guide_internet_libre_acces/>

## Comment contribuer ❤️

- Une étoile me ferait déjà bien plaisir ⭐
- Si ce repo peut vous être utile, je suis friand de vos idées et vos besoins spécifiques, peut-être par email : _contact_ at _ad2ien.dev_
- Vous pouvez aussi me demander de venir l'installer chez vous 😜
- Toute plainte ou demande de développement ou contribution peut être discutée dans la partie [issues](https://github.com/ad2ien/balenos/issues).
