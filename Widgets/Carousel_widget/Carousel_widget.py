import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# The Image widget is used to display an image
# this module contain all features of images
from kivy.uix.image import AsyncImage

# The Carousel widget provides the
# classic mobile-friendly carousel
# view where you can swipe between slides
from kivy.uix.carousel import Carousel
from kivy.lang.builder import Builder

Builder.load_file('Carousel_widget.kv')


class CarouselExample(Carousel):
    pass


# Create the App class
class CarouselApp(App):
    def build(self):
       
        return CarouselExample()


# Run the App
CarouselApp().run()