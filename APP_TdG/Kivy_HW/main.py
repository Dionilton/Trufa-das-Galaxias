from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


class JanelaManage(ScreenManager):
    pass


class HelloWorld(Screen):
    pass


class MeuApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.title = "Trufa das Galáxias - APP"

    def ola(self):
        self.root.get_screen("hw").ids.ola.text = "Olá Mundo!"
        self.theme_cls.primary_palette = 'Purple'


MeuApp().run()
