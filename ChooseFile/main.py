import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
Builder.load_file("file_choose.kv")
 
 
class MyWidget(GridLayout):
 
 
    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]
 
 
        except:
            pass
 
 
 
class FileChooserWindow(App):
    def build(self):
 
        return MyWidget()
 
 
 
 
if __name__ == "__main__":
    window = FileChooserWindow()
    window.run()