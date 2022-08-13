from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

Builder.load_file("MainScreen/main_screen.kv")

from kivy.properties import StringProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineListItem


class ElevationCard(MDCard, FakeRectangularElevationBehavior):
    pass


class MYCard(MDCard, FakeRectangularElevationBehavior):
    source = StringProperty()
    tag = StringProperty()


class MainScreenView(ThemableBehavior, MDScreen):
    image_list = [
        "https://picsum.photos/id/10/512/512",
        "https://picsum.photos/id/100/512/512",
        "https://picsum.photos/id/1000/512/512",
        "https://picsum.photos/id/1003/512/512",
        "https://picsum.photos/id/1006/512/512",
        "https://picsum.photos/id/1015/512/512",
        "https://picsum.photos/id/1016/512/512",
        "https://picsum.photos/id/1018/512/512",
        "https://picsum.photos/id/1021/512/512",
    ]

    def on_star(self, *args):
        for i in range(20):
             self.root.ids.card_list.add_widget(
                   OneLineListItem(text=f"Single-line item {i}")
                )
            
               
       
