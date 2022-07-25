import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# Program to explain how to add carousel in kivy

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


# Create the App class
class CarouselApp(App):
    def build(self):
        # Add carousel
        # And add the direction of swipe
        carousel = Carousel(direction='right')

        # Adding 10 slides
        for i in range(10):
            src = "http://placehold.it/480x270.png&text=slide-%d&.png"% i
            # using Asynchronous image
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel


# Run the App
CarouselApp().run()