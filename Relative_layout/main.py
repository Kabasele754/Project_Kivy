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
class Relative_Layout(App):
      
    def build(self):
  
        # creating Relativelayout 
        rl = RelativeLayout()
        
        # creating button
        # size of button is 20 % by hight and width of layout
        # position is bottom left i.e x = 0, y = 0
        b1 = Button(size_hint =(.2, .2),
                    pos_hint ={'x':0, 'y':0},
                    text ="B1")
          
        # position is bottom right i.e right = 1, y = 0
        b2 = Button(size_hint =(.2, .2),
                    pos_hint ={'right':1, 'y':0},
                    text ="B2")
  
        b3 = Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.5, 'center_y':.5},
                    text ="B3")
  
        b4 = Button(size_hint =(.2, .2),
                    pos_hint ={'x':0, 'top':1},
                    text ="B4")
  
        b5 = Button(size_hint =(.2, .2),
                    pos_hint ={'right':1, 'top':1},
                    text ="B5")
          
          
  
        # adding button to widget
        rl.add_widget(b1)
        rl.add_widget(b2)
        rl.add_widget(b3)
        rl.add_widget(b4)
        rl.add_widget(b5)
      
          
        # returning widget
        return rl
# run the App 
if __name__  == "__main__":
    Relative_Layout().run()