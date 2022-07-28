import dotenv
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd
import os

dotenv.load_dotenv(dotenv.find_dotenv())

str_conn = os.getenv("str_conn")
engine = create_engine(str_conn)
sql = "SELECT user_id, usuario, senha, nome from tbusers"

df = pd.read_sql_query(sql, con=engine)


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
        if user in df['usuario'].values:
            data = df.loc[df.usuario == user]
            if password == data['senha'].values[0]:
                self.root.current = 'principal'
            else:
                self.root.get_screen('login').ids.msg.text = 'Usuário ou senha incorreto. Tente novamente!'
        else:
            self.root.get_screen('login').ids.msg.text = 'Usuário ou senha incorreto. Tente novamente!'


MeuApp().run()
