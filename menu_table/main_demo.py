import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.icon_definitions import md_icons
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("demo_tab.ky")

Window.size = (300, 500)


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MainScreen(Screen):
    def navigation_draw(self):
        print("Navigation")


class DemoApp(MDApp):
    #icons = list(md_icons.keys())[15:30]

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        screen = MainScreen()
        return screen

    def on_start(self):
        accueil = Tab(text=f"Accueil ")
        galery = Tab(text=f"Blog ")
        blog = Tab(text=f"Gallery ")
        self.root.ids.android_tabs.add_widget(accueil)
        self.root.ids.android_tabs.add_widget(galery)
        self.root.ids.android_tabs.add_widget(blog)

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()


DemoApp().run()