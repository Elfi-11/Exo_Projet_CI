# Projet-CI : 

# Collaborateur : 

Benjamin Mazars
François Talaban
Marina Estanco
Rémi Sauvere



# outil Git Hub ACtion, pourquoi?

*Avantages :

1 : Le projet est déjà sur le site Git Hub, du coup nous pouvons bénéficier de l'intégration native de Git Hub, ne nécessitant pas d'outil externe ;
2 : Support multiplateforme, prend en charge les environnments Linux, macOS et Windows ce qui permet de tester sous ces trois OS.
3 : Utilisation plus facile qu'un autre outil, car nous avons déjà les bases de Git Hub, permet de ne pas perdre de temps là dessus et les workflows sont configurés dans des fichiers YAML simples, ce qui correspond à notre projet.


*Inconvénient :
1 : Est payant pour les gros projets en cas que notre projet grossisse.
2 : Compléxicités des workflows dans le cas de gros projets, (encore une fois dans le cas ou il devrait grossir) car si complexes peuvent être difficiles à lire, en effet l'utilisation se fait par un seul fichier Yaml.
3 : Support limité, on s'enferme dans la logique git hub.




# Fonctionnement CI : 

Le pipeline CI/CD a été configuré pour automatiser le processus de validation du code et de fusion des branches, garantissant ainsi que les modifications apportées au projet sont validées avant d'être intégrées à la branche principale. Voici le fonctionnement détaillé du pipeline :

1 - Travail sur les branches individuelles
Chaque développeur travaille sur sa propre branche (généralement une branche feature/<nom> ou la branche dev), où il effectue des modifications et ajoute de nouvelles fonctionnalités. Une fois que les modifications sont prêtes à être validées, le développeur pousse ses commits vers la branche distante.

2 - Déclenchement automatique de la CI
Lorsqu'un commit est poussé sur la branche dev, le pipeline CI/CD est déclenché automatiquement. Voici les étapes clés qui se déroulent à chaque exécution du pipeline :

3 - Récupération du code : Le code de la branche dev est récupéré à l'aide de l'action actions/checkout. Cette étape assure que nous travaillons avec la dernière version de la branche.

4 - Configuration de l'environnement Python : L'environnement Python est configuré avec la version spécifiée (ici, 3.9) pour garantir que le code est exécuté dans un environnement propre et cohérent.

5 -Installation des dépendances : Si un fichier requirements.txt est présent dans le projet, les dépendances nécessaires sont installées via pip.

6 - Définition du chemin source : La variable d'environnement PYTHONPATH est définie pour s'assurer que les modules Python peuvent être correctement importés.

7 - Exécution des tests
Une suite de tests unitaires est exécutée à l'aide de la commande unittest. Les tests sont lancés à partir du répertoire test et tout échec est pris en compte. En cas d'échec, le pipeline continue d'exécuter les étapes suivantes pour isoler le problème.

8 - Fusion automatique des branches en cas de succès des tests
Si tous les tests passent avec succès, la branche dev est automatiquement fusionnée dans la branche main.

9 - Un merge fast-forward est effectué pour éviter un commit supplémentaire, garantissant ainsi que la branche main est mise à jour avec les dernières modifications.

10 - Le push vers main est effectué avec un x-access-token pour garantir l'authentification correcte lors de l'utilisation de GitHub Actions.

11 - Gestion des échecs
Si un test échoue :

Une branche d'échec est automatiquement créée à partir du commit fautif. Cette branche est nommée failures/<timestamp>, ce qui permet de facilement identifier et corriger le problème.
Le commit fautif est supprimé de la branche dev à l'aide d'un git reset --hard, et un push --force est effectué pour forcer la mise à jour de la branche dev sans le commit problématique.
Le lien pour la création d'une pull request est fourni, permettant de gérer les commits échoués et de les corriger si nécessaire.
Avantages du système CI/CD

Automatisation : Le processus est entièrement automatisé, permettant de valider le code sans intervention manuelle et de détecter rapidement les erreurs.
Stabilité de la branche main : Grâce au système de tests et à la fusion contrôlée, la branche main reste toujours stable et prête à être déployée.
Gestion des erreurs simplifiée : En cas d'échec des tests, le pipeline crée une branche dédiée pour isoler et corriger l'erreur sans perturber le flux de développement sur dev