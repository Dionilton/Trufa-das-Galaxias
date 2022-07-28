from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition


class JanelaManage(ScreenManager):
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
        self.title = "Login System Test"

    def isAuthenticated(self):
        user = self.root.get_screen('login').ids.user.text
        password = self.root.get_screen('login').ids.password.text
        print(user)
        print(password)


MeuApp().run()
