import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class ExempleGrid(GridLayout):
    pass

class GridApp(App):
    pass

if __name__=="__main__":
    GridApp().run()