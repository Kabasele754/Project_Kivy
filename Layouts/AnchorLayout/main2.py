# Sample Python application demonstrating the
# working of AnchorLayout in Kivy using .kv file

###################################################
  
# Module imports
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# to change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# creating the root widget used in .kv file
class Anchor_Layout(GridLayout):
	pass

# class in which name .kv file must be named Anchor_Layout.kv
class Anchor_LayoutApp(App):
	def build(self):
		# returning the instance of root class
		return Anchor_Layout()

# run the app
if __name__=='__main__':
	Anchor_LayoutApp().run()
