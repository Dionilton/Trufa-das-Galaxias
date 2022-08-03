import dotenv
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivymd.uix.menu import MDDropdownMenu
import psycopg2 as pg
from sqlalchemy import create_engine
import pandas as pd
import os

dotenv.load_dotenv(dotenv.find_dotenv())

str_conn = os.getenv("str_conn")
engine = create_engine(str_conn)
sql_user = "SELECT user_id, usuario, senha, nome from tbusers"
sql_sabores = "SELECT sabor from tbsabores"
sql_pagamentos = "SELECT pagamento from tbpagamentos"

user_df = pd.read_sql_query(sql_user, con=engine)
sabores_df = pd.read_sql_query(sql_sabores, con=engine)
pagamentos_df = pd.read_sql_query(sql_pagamentos, con=engine)


class JanelaManage(ScreenManager):
    pass


class JanelaLogin(Screen):
    pass


class JanelaError(Screen):
    pass


class JanelaPrincipal(Screen):
    pass


class MeuApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.itemsSab = None
        self.itemsPag = None
        self.menuSab = None
        self.menuPag = None
        self.itemQtd = None

    def build(self):
        # self.root.transition = NoTransition()
        self.theme_cls.primary_palette = 'Purple'
        self.title = "Trufa das Galáxias - APP"
        self.itemsSab = sabores_df['sabor'].values.tolist()
        self.itemsPag = pagamentos_df['pagamento'].values.tolist()
        self.itemsQtd = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

        menu_itemsSab = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_release": lambda x=i: self.set_itemSab(x),
            } for i in self.itemsSab
        ]
        self.menuSab = MDDropdownMenu(
            caller=self.root.get_screen('principal').ids.drop_itemSab,
            items=menu_itemsSab,
            position="center",
            width_mult=6,
            background_color=[80 / 255, 210 / 255, 242 / 255, 1],
        )
        self.menuSab.bind()

        menu_itemsPag = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_release": lambda x=i: self.set_itemPag(x),
            } for i in self.itemsPag
        ]
        self.menuPag = MDDropdownMenu(
            caller=self.root.get_screen('principal').ids.drop_itemPag,
            items=menu_itemsPag,
            position="center",
            width_mult=6,
            background_color=[80 / 255, 210 / 255, 242 / 255, 1],
        )
        self.menuPag.bind()

        menu_itemsQtd = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_release": lambda x=i: self.set_itemQtd(x),
            } for i in self.itemsQtd
        ]
        self.menuQtd = MDDropdownMenu(
            caller=self.root.get_screen('principal').ids.drop_itemQtd,
            items=menu_itemsQtd,
            position="center",
            width_mult=6,
            background_color=[80 / 255, 210 / 255, 242 / 255, 1],
        )
        self.menuQtd.bind()

    def set_itemSab(self, text_item):
        self.root.get_screen('principal').ids.drop_itemSab.text = text_item
        self.menuSab.dismiss()

    def set_itemPag(self, text_item):
        self.root.get_screen('principal').ids.drop_itemPag.text = text_item
        self.menuPag.dismiss()

    def set_itemQtd(self, text_item):
        self.root.get_screen('principal').ids.drop_itemQtd.text = text_item
        self.menuQtd.dismiss()

    def isAuthenticated(self):
        user = self.root.get_screen('login').ids.user.text
        password = self.root.get_screen('login').ids.password.text
        if user in user_df['usuario'].values:
            data = user_df.loc[user_df.usuario == user]
            if password == data['senha'].values[0]:
                self.root.current = 'principal'
                self.root.get_screen('principal').ids.id_nome.text = f"Logado com: {data['nome'].values[0]}"
            else:
                self.root.get_screen('login').ids.msg.text = 'Usuário ou senha incorreto. Tente novamente!'
        else:
            self.root.get_screen('login').ids.msg.text = 'Usuário ou senha incorreto. Tente novamente!'

    def returnLogin(self):
        self.root.current = 'login'

    def cadastrarVenda(self):
        pass


MeuApp().run()
