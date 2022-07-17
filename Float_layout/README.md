# Floatlayout

Floatlayout nous permet de placer les éléments relativement en fonction de la taille et de la hauteur actuelles de la fenêtre, en particulier dans les mobiles, c'est-à-dire Floatlayout nous permet de placer les éléments en utilisant quelque chose appelé position relative. Cela signifie plutôt que de définir la position spécifique ou les coordonnées, nous placerons tout en utilisant le pourcentage par rapport à la taille de la fenêtre. Lorsque nous modifions les dimensions de la fenêtre, tout ce qui est placé dans la fenêtre ajustera sa taille et sa position en conséquence. Cela rend l'application plus fiable et évolutive à la taille de la fenêtre.

Remarque : FloatLayout respecte les propriétés pos_hint et size_hint de ses enfants.

La première chose que nous devons faire pour utiliser un FloatLayout est de l'importer.

```from kivy.uix.floatlayout import FloatLayout```