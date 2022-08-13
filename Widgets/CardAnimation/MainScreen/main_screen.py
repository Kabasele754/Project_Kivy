from MainScreen.components import HeroCard
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

Builder.load_file("MainScreen/main_screen.kv")


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

    def on_enter(self, *args):
        if not self.ids.hero_list.children:
            for i, source in enumerate(self.image_list):
                self.ids.hero_list.add_widget(
                    HeroCard(
                        source=source,
                        tag=f"Tag {i}",
                        on_release=self.controller.on_tap_card,
                    )
                )
