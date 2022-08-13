import imp
import os
from platform import win32_edition

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from MainScreen.main_screen import *
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (300,600)

class CardAnimation(MDApp):
    def build(self):
        return Builder.load_file("main_kv.kv")
    def on_enter(self, *args):
        if  self.root.ids.card_list.children:
            for i, source in enumerate(self.image_list):
                self.root.ids.card_list.add_widget(
                    MYCoolCard(
                        source=source,
                        tag=f"Tag {i}",
                        #on_release=self.controller.on_tap_card,
                    )
                )

CardAnimation().run()