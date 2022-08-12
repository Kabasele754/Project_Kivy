import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import kivy
kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.video import Video

# check what formats are supported for your targeted devices
# for example try h264 video and acc audo for android using an mp4
# container


class VideoPlayerApp(App):

    def build(self):
        video = Video(source='myvideo.mp4')
        video.state = 'play'
        video.options = {'eos': 'loop'}
        
 
        video.allow_stretch = True
        return video


if __name__ == '__main__':
    VideoPlayerApp().run()