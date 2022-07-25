import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App

class MainApp(App):
    pass

MainApp().run()