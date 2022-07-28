import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from  kivymd.app import MDApp

class MainApp(MDApp):
    #theme_cls = ThemeManager()
    pass

# Pour lancer l'application
if __name__=='__main__':
    MainApp().run()