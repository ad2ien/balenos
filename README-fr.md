# Baleinos

Ce dépôt contient les assets, scripts et documentation d'une customisation de [Lubuntu](https://lubuntu.me/) conçue pour être utilisée par des structures qui souhaitent proposer à leurs utilisateurices une station auto-service d'accès à internet.

## Cas d'usage

### Pour les utilisateurices

- Pouvoir disposer d'un navigateur internet
  - respectant la vie privée
  - UX fluide grace à des performances correctes
- Avoir à disposition un bouton qui permet d'effacer toute trace de son passage

### Pour les admins

- Pouvoir utiliser un PC vieillissant
- Pouvoir configurer la station pour s'adapter au mieux dans au contexte d'utilisation. Tout en empêchant les utilisateurs finaux de modifier ces réglages:
  - éditer les marques pages
  - avoir la possibilité d'avoir des white ou black listes de sites
  - régler la page d'accueil, outil de recherche par défaut...

## Guide d'installation

- Installez Lubuntu <https://lubuntu.me/downloads/>
  - localisation française
  - sans chiffrement du disque
  - créez un utilisateur `admin` avec un mot de passe sécurisé

- Connectez-vous avec l'utilisateur admin
- Copiez le contenu de ce dépôt dans le répertoire personnel d'admin
- Ouvrez une console et `cd baleinos`
- Exécutez `chmod +x install-baleinos.sh && ./install-baleinos.sh`
- Suivez les instructions

## Configurer les raccourcis

- connectez vous en tant qu'admin
- démarrez Firefox
- créez et organisez les raccourcis comme vous voulez qu'ils apparaissent pour les utilisateurs
- fermez Firefox
- cliquez sur le raccourcis `Transfert de marque-pages` sur le bureau

## Listes blanche ou noires
