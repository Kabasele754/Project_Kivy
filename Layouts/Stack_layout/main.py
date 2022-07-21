import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# code to show how to use StackLayout
 
# import kivy module
import kivy
 
# this restricts the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")
   
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
   
# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button
 
# The StackLayout arranges children vertically
# or horizontally, as many as the layout can fit.
from kivy.uix.stacklayout import StackLayout

 

class StackExamen(StackLayout):
    # Different orientation
    # ['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl',
    #  [ 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']
    pass
 
# class in which we are creating StackLayout
class StackApp(App):
       
   pass
 
# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
if __name__ == '__main__':
    StackApp().run()