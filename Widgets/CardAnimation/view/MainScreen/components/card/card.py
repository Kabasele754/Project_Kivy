from kivy.properties import StringProperty

from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
Builder.load_file("View/MainScreen/components/card/card.kv")


class ElevationCard(MDCard, FakeRectangularElevationBehavior):
    pass


class HeroCard(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
