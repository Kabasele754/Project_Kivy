# Floatlayout

Floatlayout nous permet de placer les éléments relativement en fonction de la taille et de la hauteur actuelles de la fenêtre, en particulier dans les mobiles, c'est-à-dire Floatlayout nous permet de placer les éléments en utilisant quelque chose appelé position relative. Cela signifie plutôt que de définir la position spécifique ou les coordonnées, nous placerons tout en utilisant le pourcentage par rapport à la taille de la fenêtre. Lorsque nous modifions les dimensions de la fenêtre, tout ce qui est placé dans la fenêtre ajustera sa taille et sa position en conséquence. Cela rend l'application plus fiable et évolutive à la taille de la fenêtre.

Remarque : FloatLayout respecte les propriétés pos_hint et size_hint de ses enfants.

La première chose que nous devons faire pour utiliser un FloatLayout est de l'importer.

```from kivy.uix.floatlayout import FloatLayout```



### Remarque : Maintenant, si vous modifiez la taille de la fenêtre, sa position et sa taille changent également. Cette mise en page peut être utilisée pour une application. La plupart du temps, vous utiliserez la taille de la fenêtre.

Placements dynamiques 
Maintenant, il manque quelque chose ou le code ci-dessus n'est pas parfait, vous pouvez le dire. Nous devons encore ajouter le placement des boutons.

### Nous avons 2 propriétés pour créer un placement dynamique :

1) pos_hint: fournit un indice de position
Nous pouvons définir jusqu'à 6 clés, c'est-à-dire qu'il prend des arguments sous forme de dictionnaire.
pos_hint = {"x":1, "y":1, "gauche":1, "droite":1, "haut":1, "bas":1}

2) size_hint : fournit un indice de taille
Contient deux arguments, à savoir la largeur et la hauteur

### Noter:

Vous ne pouvez utiliser que des valeurs comprises entre 0 et 1 pour size_hint et pos_hint. Où 0 = 0 % et 1 = 100 %.

Le système de coordonnées en kivy fonctionne en bas à gauche ! Cela sera important lors du placement de nos objets. (c'est-à-dire (0, 0) est le coin inférieur gauche).


Code pour implémenter le positionnement dynamique :

```# To change the kivy default settings 
# we use this module config 
from kivy.config import Config 
    
# 0 being off 1 being on as in true / false 
# you can use 0 or 1 && True or False 
Config.set('graphics', 'resizable', True) 
  
# creating the App class
class MyApp(App):
  
    def build(self):
  
        # creating Floatlayout
        Fl = FloatLayout()
  
        # creating button
        # a button 30 % of the width and 50 %
        # of the height of the layout and
        # positioned at 20 % right and 20 % up
        # from bottom left, i.e x, y = 200, 200 from bottom left:
        btn = Button(text ='Hello world', size_hint =(.3, .5),
                     background_color =(.3, .6, .7, 1),
                    pos_hint ={'x':.2, 'y':.2 })
  
        # adding widget i.e button
        Fl.add_widget(btn)
  
        # return the layout
        return Fl
  
# run the App
if __name__ == "__main__":
    MyApp().run()
```
