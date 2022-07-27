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