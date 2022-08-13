import imp
import os
from platform import win32_edition

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (300,600)

class CardAnimation(MDApp):
    def build(self):
        return Builder.load_file("main_kv.kv")

CardAnimation().run()