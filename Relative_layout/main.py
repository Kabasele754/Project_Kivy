import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# Sample Python application demonstrating the
# working of RelativeLayout in Kivy
 
# import modules
import kivy
 
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
 
# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button
 
# This layout allows you to set relative coordinates for children.
from kivy.uix.relativelayout import RelativeLayout
 
# To change the kivy default settings
# we use this module config
from kivy.config import Config
     
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
 
# creating the App class
class MyApp(App):
 
    def build(self):
 
        # creating Relativelayout
        Rl = RelativeLayout()
 
        # creating button
        # a button 30 % of the width and 20 %
        # of the height of the layout and
        # positioned at (x, y), you can do
        # The position does not depend on window size
        # it just positioned at the given places:
        btn = Button(text ='Hello world',
                 size_hint =(.2, .2),
                 pos =(396.0, 298.0))
        btn1 = Button(text ='Hello world !!!!!!!!!',
                 size_hint =(.2, .2),
                 pos =(-137.33, 298.0))
 
        # adding widget i.e button
        Rl.add_widget(btn)
        Rl.add_widget(btn1)
                 
        # return the layout
        return Rl
 
# run the App
if __name__ == "__main__":
    MyApp().run()