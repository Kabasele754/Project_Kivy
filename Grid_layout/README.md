# Gridlayout

Gridlayout est la fonction qui crée les enfants et les organise dans un format matriciel. Il prend l'espace disponible (carré) et divise cet espace en lignes et colonnes, puis ajoute les widgets en conséquence aux cellules ou grilles résultantes.

Nous ne pouvons pas placer explicitement les widgets dans une colonne/ligne particulière. Chaque enfant se voit attribuer une position particulière déterminée automatiquement par la configuration de la mise en page et l'index de l'enfant dans la liste des enfants. Une mise en page de grille doit contenir au moins des contraintes d'entrée, c'est-à-dire des colonnes et des lignes. Si nous ne lui spécifions pas les colonnes ou les lignes, la mise en page vous donne une exception. 

### Colonne et ligne 
Maintenant, les colonnes représentent la largeur et les lignes représentent la hauteur, tout comme la matrice. 

1. La taille initiale est donnée par les propriétés col_default_width et row_default_height. Nous pouvons forcer la taille par défaut en définissant la propriété col_force_default ou row_force_default. Cela forcera la mise en page à ignorer les propriétés width et size_hint des enfants et à utiliser la taille par défaut.

2. Pour personnaliser la taille d'une seule colonne ou ligne, utilisez cols_minimum ou rows_minimum.

3. Il n'est pas nécessaire de donner à la fois des lignes et des colonnes, cela dépend de l'exigence. Nous pouvons fournir les deux ou n'importe qui en conséquence.
