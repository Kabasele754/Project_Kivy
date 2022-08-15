import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.lang.builder import Builder


class canvasCallApp(App):
    def build(self):
    		return Builder.load_file("canvas.kv")

if __name__ == '__main__':
    canvasCallApp().run()