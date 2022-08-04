import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button


class HomeScreen(Screen):
    grid_l = ObjectProperty(None)
    top_lbl = ObjectProperty(None)

    def search_btn_pressed(self):
        grid = self.grid_l
        grid.bind(minimum_height=grid.setter('height'),
                     minimum_width=grid.setter('width'))

        for i in range(3):
                layout = GridLayout(cols=1)
                print layout
                img = Image(source='kivy.png')
                print img
                lbl = Label(text='label')
                layout.add_widget(img)
                layout.add_widget(lbl)

                btn1 = Button(size_hint=(1, None))
                btn1.text = '%r' % i
                btn1.add_widget(layout)

                grid.add_widget(btn1)

# class in which we are creating the button
class ButtonApp(App):
	
	def build(self):
		
		btn = Button(text ="Push Me !")
		return btn

# creating the object root for ButtonApp() class
root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()
