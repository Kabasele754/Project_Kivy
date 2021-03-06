import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

"""
This is the file being picked up by `buildozer` as it's expecting a `main.py`
in the source directory.
"""
from kivy_garden.xcamera.main import main

if __name__ == '__main__':
    main()