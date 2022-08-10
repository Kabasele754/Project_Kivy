import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
Window.size = (350,550)


class Enregister(MDApp):
    def build(self):
        return Builder.load_file("main_kv.kv")

if __name__ == "__main__":
    Enregister().run()