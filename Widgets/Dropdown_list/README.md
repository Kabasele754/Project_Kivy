# La liste déroulante (Dropdown list)

Une liste déroulante peut être utilisée avec des widgets personnalisés. Il vous permet d'afficher une liste de widgets sous un widget affiché. Contrairement à d'autres toolkits, la liste des widgets peut contenir n'importe quel type de widget : boutons simples, images etc. Le positionnement de la liste déroulante est entièrement automatique : nous essaierons toujours de placer la liste déroulante d'une manière que l'utilisateur peut sélectionner un élément de la liste. Quelques points importants à garder à l'esprit lors de la création d'une liste déroulante :

Lors de l'ajout de widgets, nous devons spécifier la hauteur manuellement (en désactivant le size_hint_y) afin que la liste déroulante puisse calculer la zone dont elle a besoin.

Tous les boutons de la liste déroulante déclencheront la méthode déroulante DropDown.select(). Après avoir été appelé, le texte du bouton principal affichera la sélection de la liste déroulante.