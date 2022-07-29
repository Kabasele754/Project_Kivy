# Program to explain how to add carousel in kivy
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


# The Carousel widget provides the
# classic mobile-friendly carousel
# view where you can swipe between slides
from kivy.uix.carousel import Carousel

# The GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file('carousel1.kv')


# Create the Layout Class
class Carousel(GridLayout):
	pass

# Create the App class
class CarouselApp(App):
	def build(self):
		# Set carousel widget as root
		root = Carousel()

		# for multiple pages
		for x in range(10):
			root.add_widget(Carousel())
		return root


# run the App
if __name__ == '__main__':
	CarouselApp().run()
