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

Notre Ci est faite de façon à ce que chacun sur sa branch puisse push ces commits. 
De là, la CI est déclanchée, si les tests sont ok, il y aura une merge automatique de nos branch feature à la branch dev. Puis après un recontrôle du CI une merge bauto de la branch dev à dans le main. 