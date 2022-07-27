# Image Widget:

Le widget Image est utilisé pour afficher une image. Pour utiliser le widget image vous devez avoir importé : 

```from kivy.uix.image import Image, AsyncImage (pas nécessaire lorsque vous travaillez avec un fichier .kv)```
car le module kivy.uix.image possède toutes les fonctionnalités liées aux images.

Les images peuvent être chargées dans l'application via deux types :

1. Chargement synchrone : chargement de l'image à partir du système (doit provenir du dossier dans lequel les fichiers .py et .kv sont enregistrés) 

2. Chargement asynchrone : pour charger une image de manière asynchrone (par exemple à partir d'un serveur Web externe) 