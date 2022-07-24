import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# Sample spinner app in kivy to change the
# kivy default settings we use this module config
from kivy.config import Config
  
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
  
# Program to Show how to create a switch
# import kivy module   
import kivy 
     
# base Class of your App inherits from the App class.   
# app:always refers to the instance of your application  
from kivy.app import App
   
# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 
kivy.require('1.9.0')
  
# The Label widget is for rendering text. 
from kivy.uix.label import Label
  
# Spinner is a widget that provides a
# quick way to select one value from a set.
# like a dropdown list
from kivy.uix.spinner import Spinner
  
# module consist the floatlayout 
# to work with FloatLayout first 
# you have to import it 
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
  
  
# Make an App by deriving from the App class
class SpinnerExample(App):
  
    # define build 
    def build(self):
  
        
        return Builder.load_file("spiner.kv")
  
  
# Run the app
if __name__ == '__main__':
    SpinnerExample().run() 