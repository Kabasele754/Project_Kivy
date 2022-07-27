# Popup

Le widget Popup est utilisé pour créer des popups. Par défaut, la popup couvrira toute la fenêtre « mère ». Lorsque vous créez un popup, vous devez au moins définir un Popup.title et un Popup.content.

Les boîtes de dialogue contextuelles sont utilisées lorsque nous devons transmettre certains messages évidents à l'utilisateur. Les messages à l'utilisateur via les barres d'état ainsi que pour les messages spécifiques qui doivent être mis en évidence peuvent toujours être transmis via des boîtes de dialogue contextuelles.

Gardez une chose à l'esprit que la taille par défaut d'un widget est size_hint=(1, 1).
Si vous ne voulez pas que votre popup soit en plein écran, vous devez donner des conseils de taille avec des valeurs inférieures à 1 (par exemple size_hint=(.8, .8)) ou désactiver le size_hint et utiliser des attributs de taille fixe.