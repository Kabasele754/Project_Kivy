import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.metrics import dp

from database_etu import Database

db = Database('database_student.db')

class DataTableBox(MDBoxLayout):
    def __init__(self, **kwargs):
        super(DataTableBox, self).__init__(**kwargs)
        self.data_tables = MDDataTable(
            column_data=[
                ("Id", dp(15)),
                ("Name", dp(30)),
                ("Lastname", dp(30)),
                ("Firstname", dp(30)),
                ("Age", dp(30))
            ],
            use_pagination=True,
            rows_num=5,
            pos_hint= {'center_x':.5, 'center_y':.90}
        )
        self.data_tables.row_data = self.get_all_data()
        self.data_tables.bind(on_row_press=self.row_selected)
        self.add_widget(self.data_tables)
    def get_all_data(self):
        data = []
        for row in db.fetch_all():
            data.append(row)
        return data

    def row_selected(self, table, row):
        # get start index from selected row item range
        start_index, end_index = row.table.recycle_data[row.index]["range"]

        # populate form with selected record
        self.populate_form(row.table.recycle_data[start_index]["text"])

    def clear_form(self):
        self.root.ids.student_id.text = ''
        self.root.ids.name.text = ''
        self.root.ids.lastname.text = ''
        self.root.ids.firstname.text = ''
        self.root.ids.age.text = ''

    def populate_form(self, row_id):
        # retrieve row data from db using record_id
        # returned dataset tuple: (record_id, matter_name, file_name, description, location)
        row_data = db.get_record_by_id(row_id)

        self.root.ids.student_id.text = str(row_data[0])
        self.root.ids.name.text = row_data[1]
        self.root.ids.lastname.text = row_data[2]
        self.root.ids.firstname.text = row_data[3]
        self.root.ids.age.text = row_data[4]

    def add_record(self):# to save data
        self.root.ids.student_id.text = ''
        if self.root.ids.name.text == '' or self.root.ids.lastname.text == '' or self.root.ids.firstname.text == '' or self.root.ids.age.text == '':
            self.root.ids.student_id.text = 'Veuillez remplir tous les champs'
        else:
            name = self.root.ids.name.text
            lastname = self.root.ids.lastname.text
            firstname = self.root.ids.firstname.text
            age = self.root.ids.location.text
            db.insert(name, lastname, firstname, age)
            self.data_tables.row_data = self.get_all_data()
            self.clear_form()

    def update_record(self):
        if self.root.ids.student_id.text == '':
            pass
        else:
            id = self.root.ids.student_id.text
            name = self.root.ids.name.text
            lastname = self.root.ids.lastname.text
            firstname = self.root.ids.firstname.text
            age = self.root.ids.age.text
            db.update(id, name, lastname, firstname, age)
            self.data_tables.row_data = self.get_all_data()

    def delete_record(self):
        if self.root.ids.student_id.text == '':
            pass
        else:
            id = self.root.ids.student_id.text
            db.delete(id)
            self.data_tables.row_data = self.get_all_data()
            self.clear_form()
            
            
            
class StudentFormApp(MDApp):
    def build(self):
        screen = Builder.load_file('database.kv')
    
        return screen

    


if __name__ == '__main__':
    StudentFormApp().run()