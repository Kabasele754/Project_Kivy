import os


os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

"""
This is the file being picked up by `buildozer` as it's expecting a `main.py`
in the source directory.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera



class CameraApp(App):
    def build(self):
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800,800)
        self.camera_obj.play = True
        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        return layout


if __name__ == '__main__':
    CameraApp().run()