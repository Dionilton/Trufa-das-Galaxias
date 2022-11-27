import os
from datetime import date, datetime

import dotenv
import pandas as pd
import psycopg2
import psycopg2 as pg
from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition, Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from plyer import gps
from sqlalchemy import create_engine

dotenv.load_dotenv(dotenv.find_dotenv())

str_conn = os.getenv('str_conn')
engine = create_engine(str_conn)
sql_user = 'SELECT user_id, usuario, senha, nome from tbusers'
sql_sabores = 'SELECT sabor from tbsabores'
sql_pagamentos = 'SELECT pagamento from tbpagamentos'

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


class JanelaSucesso(Screen):
    pass


class MeuApp(MDApp):
    def on_location(self, **kwargs):
        s = ' '
        seq = (str(kwargs['lat']), str(kwargs['lon']))
        self.stringGPS = s.join(seq)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flagExistGPS = None
        self.gps = None
        self.itemsSab = None
        self.itemsPag = None
        self.itemsQtd = None
        self.menuSab = None
        self.menuPag = None
        self.itemQtd = None
        self.stringGPS = None
        self.statusGPS = None
        self.statusMSG = None

    def build(self):
        # self.root.transition = NoTransition()
        # self.root.current = 'sucesso'
        Window.size = (360, 640)
        self.gps = gps
        self.statusGPS = ''
        self.statusMSG = ''
        self.theme_cls.primary_palette = 'Purple'
        self.title = 'Trufa das Galáxias - APP'
        self.itemsSab = sabores_df['sabor'].values.tolist()
        self.itemsPag = pagamentos_df['pagamento'].values.tolist()
        self.itemsQtd = [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
        ]

        try:
            gps.configure(
                on_location=self.on_location, on_status=self.on_status
            )
            self.flagExistGPS = 1
        except NotImplementedError:
            self.flagExistGPS = 0
            print(self.statusGPS)

        if self.flagExistGPS == 1:
            self.statusMSG = 'GPS Configurado'
        elif self.flagExistGPS == 0:
            self.statusMSG = 'Impossível confidurar o GPS'

        menu_itemsSab = [
            {
                'viewclass': 'OneLineListItem',
                'text': i,
                'on_release': lambda x=i: self.set_itemSab(x),
            }
            for i in self.itemsSab
        ]
        self.menuSab = MDDropdownMenu(
            caller=self.root.get_screen('principal').ids.drop_itemSab,
            items=menu_itemsSab,
            position='center',
            width_mult=6,
            background_color=[80 / 255, 210 / 255, 242 / 255, 1],
        )
        self.menuSab.bind()

        menu_itemsPag = [
            {
                'viewclass': 'OneLineListItem',
                'text': i,
                'on_release': lambda x=i: self.set_itemPag(x),
            }
            for i in self.itemsPag
        ]
        self.menuPag = MDDropdownMenu(
            caller=self.root.get_screen('principal').ids.drop_itemPag,
            items=menu_itemsPag,
            position='center',
            width_mult=6,
            background_color=[80 / 255, 210 / 255, 242 / 255, 1],
        )
        self.menuPag.bind()

        menu_itemsQtd = [
            {
                'viewclass': 'OneLineListItem',
                'text': i,
                'on_release': lambda x=i: self.set_itemQtd(x),
            }
            for i in self.itemsQtd
        ]
        self.menuQtd = MDDropdownMenu(
            caller=self.root.get_screen('principal').ids.drop_itemQtd,
            items=menu_itemsQtd,
            position='center',
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
                self.root.get_screen(
                    'principal'
                ).ids.id_nome.text = f"Logado com: {data['nome'].values[0]}"
                self.root.get_screen(
                    'sucesso'
                ).ids.id_nome2.text = f"Logado com: {data['nome'].values[0]}"
            else:
                self.root.get_screen(
                    'login'
                ).ids.msg.text = 'Usuário ou senha incorreto. Tente novamente!'
        else:
            self.root.get_screen(
                'login'
            ).ids.msg.text = 'Usuário ou senha incorreto. Tente novamente!'

    def returnLogin(self):
        self.root.get_screen('login').ids.user.text = ''
        self.root.get_screen('login').ids.password.text = ''
        self.root.get_screen('login').ids.msg.text = ''
        self.root.get_screen(
            'principal'
        ).ids.drop_itemSab.text = 'Escolha o sabor'
        self.root.get_screen(
            'principal'
        ).ids.drop_itemQtd.text = 'Escolha a quantidade'
        self.root.get_screen(
            'principal'
        ).ids.drop_itemPag.text = 'Escolha a forma de pagamento'
        self.root.get_screen('principal').ids.aviso.text = ''

        self.root.current = 'login'

    def cadastrarVenda(self):
        global engine
        if (
            self.root.get_screen('principal').ids.drop_itemSab.text
            != 'Escolha o sabor'
            and self.root.get_screen('principal').ids.drop_itemQtd.text
            != 'Escolha a quantidade'
            and self.root.get_screen('principal').ids.drop_itemPag.text
            != 'Escolha a forma de pagamento'
        ):
            venda = [
                self.root.get_screen('principal').ids.drop_itemSab.text,
                int(self.root.get_screen('principal').ids.drop_itemQtd.text),
                self.root.get_screen('principal').ids.drop_itemPag.text,
            ]
            data = date.today()
            data_em_texto = f'{data.month}/{data.day}/{data.year}'
            now = datetime.now()
            hora_texto = f'{now.hour}:{now.minute}:{int(now.second)}'
            venda.append(hora_texto)
            venda.append(data_em_texto)
            self.ligaGPS()
            venda.append(self.stringGPS)
            venda.append(
                self.root.get_screen('principal').ids.id_nome.text.split()[2]
            )
            print(venda) #para o desenvolvedor
            sql_venda = f"INSERT INTO tbvendas (sabor, quantidade, pagamento, hora, _data, _local, vendedor) VALUES ('{venda[0]}', {venda[1]}, '{venda[2]}', '{venda[3]}', '{venda[4]}', '{venda[5]}', '{venda[6]}');"
            print(sql_venda) #para o desenvolvedor

            try:
                engine.execute(sql_venda)
            except:
                engine = create_engine(str_conn)
                engine.execute(sql_venda)



            self.root.current = 'sucesso'

        else:
            self.root.get_screen(
                'principal'
            ).ids.aviso.text = 'selecione todos os campos'

    def novaVenda(self):
        self.root.get_screen(
            'principal'
        ).ids.drop_itemSab.text = 'Escolha o sabor'
        self.root.get_screen(
            'principal'
        ).ids.drop_itemQtd.text = 'Escolha a quantidade'
        self.root.get_screen(
            'principal'
        ).ids.drop_itemPag.text = 'Escolha a forma de pagamento'
        self.root.get_screen('principal').ids.aviso.text = ''

        self.root.current = 'principal'

    @mainthread
    def on_location(self, **kwargs):
        s = ' '
        seq = (str(kwargs['lat']), str(kwargs['lon']))
        self.stringGPS = s.join(seq)
        self.statusMSG = 'GPS enviou os dados'

    @mainthread
    def on_status(self, stype, status):
        self.statusGPS = f'type={stype}\n{status}'
        self.statusMSG = 'GPS enviou os dados'

    def ligaGPS(self):
        if self.flagExistGPS == 1:
            self.gps.start()
            self.statusMSG = 'GPS ligado, deu bom'
        else:
            self.statusMSG = 'Sem GPS- Erro1'
            self.root.get_screen('principal').ids.aviso.text = self.statusMSG


MeuApp().run()
