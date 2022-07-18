# RelativeLayout

RelativeLayout permet de définir des coordonnées relatives pour les enfants. Si vous voulez un positionnement absolu, utilisez le FloatLayout.

RelativeLayout se comporte comme le FloatLayout sauf que ses widgets enfants sont positionnés par rapport à la mise en page.

Lorsqu'un widget avec position = (0,0) est ajouté à un Relative Layout , le widget enfant se déplace également lorsque la position du RelativeLayout est modifiée. Les coordonnées des widgets enfants restent (0,0) car elles sont toujours relatives à la mise en page parent.


1. Cette disposition fonctionne de la même manière que FloatLayout, mais les propriétés de positionnement (x, y, center_x, right, y, center_y et top) sont relatives à la taille de la disposition et non à la taille de la fenêtre.

2. En réalité quel que soit le positionnement absolu et relatif, les widgets sont déplacés lorsque la position de la mise en page change.
Lorsque le widget avec position=(0, 0) est ajouté à RelativeLayout, maintenant, si la position de RelativeLayout est modifiée, le widget enfant se déplacera également. Les coordonnées du widget enfant restent les mêmes, c’est-à-dire (0, 0) car elles sont toujours relatives à la disposition parent.

3. Les touches pos_hint disponibles (x, center_x, right, y, center_y et top) sont utiles pour l’alignement sur les bords ou le centrage.

## Par exemple :
```pos_hint : {‘center_x’:.5, ‘center_y’:.5}``` alignerait un widget au milieu, quelle que soit la taille de la fenêtre.


## Remarque :

Cette disposition vous permet de définir des coordonnées relatives pour les enfants. Si vous voulez un positionnement absolu, utilisez le FloatLayout. Dans RelativeLayout, la taille et la position de chaque widget enfant doivent être données. Cela fait également le placement dynamique.


We can do relative positioning by:

pos_hint: provide hint of position

We can define upto 8 keys i.e. it takes arguments in form of dictionary.

```pos_hint = {“x”:1, “y”:1, “left”:1, “right”:1, "center_x":1, "center_y":1,“top”:1, “bottom”:1("top":0)}```

## Remarque :

Floatlayout et les RelativeLayout deux prennent en charge le positionnement absolu et relatif selon que pos_hint ou pos est utilisé. Mais si vous voulez un positionnement absolu, utilisez le FloatLayout.

#### Implémentation de l’approche à l’aide de pos :

Il attribue simplement la position au bouton. Comme Relativelayout cela ne dépend pas de la taille de la fenêtre, il est maintenant fixé à cette position si vous réduisez la taille de la fenêtre, il peut disparaître au lieu de s’ajuster.