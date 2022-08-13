from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

Builder.load_file("MainScreen/main_screen.kv")

from kivy.properties import StringProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.app import MDApp


class ElevationCard(MDCard, FakeRectangularElevationBehavior):
    pass


class MYCard(MDCard, FakeRectangularElevationBehavior):
    source = StringProperty()
    tag = StringProperty()

class MYCoolCard(MDCard, FakeRectangularElevationBehavior):
    source = StringProperty()
    tag = StringProperty()

class MainScreenView(ThemableBehavior, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        #self.model.add_observer(self)
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
    
    def on_enter(self, *args):
        if  self.ids.card_list.children:
            for i, source in enumerate(self.image_list):
                self.ids.card_list.add_widget(
                    MYCoolCard(
                        source=source,
                        tag=f"Tag {i}",
                        #on_release=self.controller.on_tap_card,
                    )
                )
                
