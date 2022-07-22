# Button

Le bouton est une étiquette avec des actions associées qui sont déclenchées lorsque le bouton est enfoncé (ou relâché après un clic/touche). Nous pouvons ajouter des fonctions derrière le bouton et styliser le bouton.

## Ajout de fonctionnalités derrière le bouton.

L'un des problèmes courants est de savoir comment ajouter des fonctionnalités au bouton. Donc, pour ajouter des fonctionnalités, nous utilisons  la fonctionbind () , elle lie la fonction au bouton. bind() crée un événement qui est envoyé à callback().

L'un des problèmes les plus courants pour les nouveaux utilisateurs de Kivy est l'incompréhension du fonctionnement de la méthode bind, en particulier parmi les nouveaux utilisateurs de Python qui n'ont pas complètement formé leur intuition sur les appels de fonction.

Le fait est que la méthode bind ne connaît pas l'existence d'une fonction ou de ses arguments, elle ne reçoit que le résultat de cet appel de fonction. Comme dans le code donné lorsque le bouton est enfoncé, il imprime ce "bouton enfoncé" def dans le rappel de la fonction.

Dans le code donné à l'intérieur de bind(), nous utilisons on_pressparce que lorsque vous appuyez sur un bouton, il indique à la fonction que le bouton est enfoncé, la liaison utilise sa fonctionnalité. 