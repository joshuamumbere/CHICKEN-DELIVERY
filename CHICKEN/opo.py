from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.animation import Animation
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton

Window.size = (350, 600)

class KoKoApp(MDApp):
    def build(self):
        dialog = None
        
        self.manager = ScreenManager()
        self.manager.add_widget(Builder.load_file("koko.kv"))
        self.manager.add_widget(Builder.load_file("login.kv"))
        self.manager.add_widget(Builder.load_file("list.kv"))
        self.manager.add_widget(Builder.load_file("middle.kv"))
        self.manager.add_widget(Builder.load_file("order.kv"))
        
        
        
        return self.manager
    
    def show_alert_dialog(self, item):
        dialog = MDDialog(
            title=f'Details for {item.text}',
            text=f'Item: {item.text}\nDiscount: {item.secondary_text}\nPrice: {item.tertiary_text}',
            buttons=[
                MDFlatButton(
                    text="Close",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )

if __name__ == '__main__':
    KoKoApp().run()
