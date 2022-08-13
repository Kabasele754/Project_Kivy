import imp
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivy.lang.builder import Builder

class CardAnimation(MDApp):
    def build(self):
        return Builder.load_file("main_kv.kv")

CardAnimation().run()