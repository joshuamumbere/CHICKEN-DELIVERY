from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import sqlite3


Window.size = (350, 600)

class MyApp(MDApp):
    def build(self):
        con = sqlite3.connect("users.db")

        c = con.cursor()
        c.execute("CREATE TABLE if not exists Items(item_name text)")
        c.execute("CREATE TABLE if not exists users(fname text,lname text, contact text)")

        c.commit()
        c.close()
        db_display = Builder.load_file("koko_db.kv")
        return db_display

    def submit(self):
        con = sqlite3.connect("users.db")
        c = con.cursor()
        c.execute("INSERT INTO users VALUES (:fname, :lname, :contact)", {
    "fname": self.root.ids.name.text,
    "lname": self.root.ids.lname.text,
    "contact": self.root.ids.contact.text,
})
        self.root.ids.item.text = f'{self.root.ids.fname.text} has been added'
        # self.root.ids.item.text = "item successfully inserted into db"
        self.root.ids.item_name.text = ""
        self.root.ids.name.text = ""
        self.root.ids.laddress.text = ""
        self.root.ids.contact.text = ""
        con.commit()
        con.close()

    def show_users(self):
        con = sqlite3.connect("users.db")
        c = con.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        user_data = ""
        for user in users:
            user_data = f'{user_data}\n {user[0]} {user[1]} {user[2]}'
            self.root.ids.item.text = f'{user_data}'
        con.commit()
        con.close()

    def toggle_password_visibility(self, password_field, checkbox):
        print("Toggle password visibility called")
        password_field.password = not checkbox.active
        print("Password visibility:", not checkbox.activate)

if __name__ == "__main__":
    MyApp().run()
