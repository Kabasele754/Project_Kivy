import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import io

from kivy.atlas import CoreImage
from kivy.core.image import Image as CoreImage
import sqlite3
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.properties import OptionProperty, StringProperty, DictProperty
from kivy.core.window import Window
Window.size = (350,550)

import sqlite3

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")





class Enregister(MDApp):
    nom = StringProperty("")
    image = StringProperty("")
    def build(self):
        return Builder.load_file("test_img_kv.kv")
    def readData(self,):
        try:
            conn = sqlite3.connect('Formulaire_sqlite/formulaire_etudiant.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_fetch_etudiant_query = """SELECT * from etudiand """
            cursor.execute(sql_fetch_etudiant_query)
            record = cursor.fetchall()
            for row in record:
                print("Id = ", row[0], "Name = ", row[1])
                name = row[1]
                photo = row[2]

                print("Storing employee image and resume on disk \n")
                photoPath = "Formulaire_sqlite/images\\" + name + ".jpg"
                writeTofile(photo, photoPath)
                data = io.BytesIO(photo)

                im = CoreImage(data, ext="jpg")
                self.nom = f'{self.nom}\n\n{row[1]}'
                #print(record)
                self.image = f'{self.image} {im.texture}'

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read blob data from sqlite table", error)
        finally:
            if conn:
                conn.close()
                print("sqlite connection is closed")

        

if __name__ == "__main__":
    Enregister().run()