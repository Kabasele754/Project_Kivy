# Sample Python application demonstrating
# the working of AnchorLayout in Kivy
  
# Module imports
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
  
# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App
  
# The AnchorLayout aligns its children to a border
# (top, bottom, left, right) or center
from kivy.uix.anchorlayout import AnchorLayout
  
# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the childrens at the desired location.
from kivy.uix.boxlayout import BoxLayout
  
# creates the button in kivy 
# if not imported shows the error
from kivy.uix.button import Button

from kivy.lang import Builder

Builder.load_file("anchor.kv")
  

class ExempleAnchor(AnchorLayout):
    pass
  
  
# A Kivy app demonstrating the working of anchor layout

class AnchorLayoutApp(App):
      
    def build(self):
     
        # Anchor Layout1
        layout = ExempleAnchor()
      
        return layout 
  
# creating the object root for AnchorLayoutApp() class  
root = AnchorLayoutApp()
# Run the Kivy app
root.run()