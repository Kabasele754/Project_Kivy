# RelativeLayout

RelativeLayout permet de définir des coordonnées relatives pour les enfants. Si vous voulez un positionnement absolu, utilisez le FloatLayout.

RelativeLayout se comporte comme le FloatLayout sauf que ses widgets enfants sont positionnés par rapport à la mise en page.

Lorsqu'un widget avec position = (0,0) est ajouté à un Relative Layout , le widget enfant se déplace également lorsque la position du RelativeLayout est modifiée. Les coordonnées des widgets enfants restent (0,0) car elles sont toujours relatives à la mise en page parent.