# Project Kivy

[![PyPI version](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/kivymd)](https://pepy.tech/project/kivymd)
[![YouTube](https://img.shields.io/static/v1?label=subscribe&logo=youtube&logoColor=ff0000&color=brightgreen&message=4k)](https://www.youtube.com/channel/UCFB47iDhNgB4bBHT7sEj21Q)


Kivy est une plate-forme indépendante car elle peut être exécutée sur Android, IOS, Linux et Windows, etc. Kivy vous offre la possibilité d'écrire le code pour une fois et de l'exécuter sur différentes plates-formes. Il est essentiellement utilisé pour développer l'application Android, mais cela ne signifie pas qu'il ne peut pas être utilisé sur les applications Desktops.


Pour utiliser Kivy, vous avez besoin de Python . Plusieurs versions de Python peuvent être installées côte à côte, mais Kivy doit être installé pour chaque version de Python que vous souhaitez utiliser Kivy.

## Installation

Maintenant que python est installé, ouvrez la ligne de commande et assurez-vous que python est disponible en tapant . Ensuite, procédez comme suit pour installer.python --version

1. Assurez-vous d'avoir le dernier pip et la dernière molette :

```python -m pip install --upgrade pip wheel setuptools```

2. Installez les dépendances (ignorez gstreamer (~120 Mo) si vous n'en avez pas besoin, consultez les dépendances de Kivy ) :

```python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew```

```python -m pip install kivy.deps.gstreamer```

### Noter

Si vous rencontrez une MemoryError lors de l'installation, ajoutez après l' installation de pip une option –no-cache-dir .

Pour Python 3.5+, vous pouvez également utiliser le backend angle au lieu de glew. Celui-ci peut être installé avec :

```python -m pip install kivy.deps.angle ```

3. Installez Kivy :

```python -m pip install kivy```

