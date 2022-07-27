from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition


class JanelaGerenciadora(ScreenManager):
    pass


class JanelaLogin(Screen):
    pass


class JanelaError(Screen):
    pass


class JanelaPrincipal(Screen):
    pass


class MeuApp(MDApp):
    def build(self):
        self.root.transition = NoTransition()
        self.theme_cls.primary_palette = 'Yellow'

    def isAuthenticated(self):
        if 7 > 12:
            self.root.current = 'principal'
        else:
            self.root.current = "error"


MeuApp().run()
