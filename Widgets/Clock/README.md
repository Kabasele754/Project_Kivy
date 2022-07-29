# Clock Object

L'objet Horloge vous permet de programmer un appel de fonction dans le futur ; une ou plusieurs fois à des intervalles spécifiés. 

Vous pouvez obtenir le temps écoulé entre la planification et l'appel du rappel via l'argument dt :

```
# define callback
def my_callback(dt):
    pass
 
# clock.schedule_interval with time specified
Clock.schedule_interval(my_callback, 0.5)
 
# clock.schedule_once with time specified
Clock.schedule_once(my_callback, 5)
 
# call my_callback as soon as possible.
Clock.schedule_once(my_callback)
```

Remarque : Si le rappel renvoie False, la planification sera annulée et ne se répétera pas. 
 

En cela, nous allons créer le kivy le chronomètre et nous créons 3 boutons dans celui-ci qui sont le démarrage, la pause, la reprise.
 

Il est bon d'utiliser le module intégré kivy tout en travaillant avec l'horloge et : 
à partir de kivy.clock import Clock


Un projet sur Kivy. Les utilisateurs de l'application doivent pouvoir sélectionner la date (jour.mois.année comme 06.03.2015) à partir de widgets conviviaux comme DatePickerCtrl et CalendarCtr l de wxPython.

Il y a CalendarWidget (comme CalendarCtrl de wxPython) et DatePicker (comme DateOickerCtrl de wxPython) et les ai placés dans un module python externe nommé KivyCalendar.

pip install KivyCalendar