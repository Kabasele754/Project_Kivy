import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# for kivymd only
# download the kivymd date widget module from here 
# https://gist.github.com/kengoon/d064ad49f4aa2212897afd69f97578dc

from datepicker import DatePicker
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout


class MyApp(MDApp):

    def build(self):
        box = BoxLayout(padding=dp(20))
        box.add_widget(DatePicker())
        return box


if __name__ == '__main__':
    MyApp().run()
    
    
# for kivy or kivymd
# follow the solved version from here 
#https://stackoverflow.com/questions/13714074/kivy-date-picker-widget#