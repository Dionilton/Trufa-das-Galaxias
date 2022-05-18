#!/usr/bin/env python
# coding: utf-8

# ### Insta Data Get - IDG
# 
# O IDG é uma automação para a coleta de dados do Instagram do TdG. Um dos objetivos dessa aplicação é
# obter dados como o número de seguidores e publicações diariamente, obtendo essas informações e atualizando a base de dados
# para que se possa fazer uma analise de dados, plotando gráficos e realizando análises estatísticas afim de se obter
# informações e conclusões valiosas que auxilie nas tomadas de decisões da instituição.
# 
# 

# In[91]:


#Passo1: Ler base de dados mais recente
import pandas as pd

tabela = pd.read_csv("DB_IDG_Teste.csv")
display(tabela)


# In[92]:


#Passo2: Obter dado mais atual(numero de seguidores e publicações)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import date

navegador = webdriver.Chrome()

navegador.get("https://www.instagram.com/")

username = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys("user@dom.com")
password.send_keys("***REMOVED***")
navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()

time.sleep(8)

navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div/span').click()
navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("hanyarts")
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div').click()
time.sleep(2)


n_seguidores = navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').get_attribute("title")
n_seguindo = navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div/span').text
n_publicacoes = navegador.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/div/span').text


n_seguidores = int(n_seguidores)
n_seguindo = int(n_seguindo)
n_publicacoes = int(n_publicacoes)

dia_atual = date.today()
dia = f'{dia_atual.day}/{dia_atual.month}/{dia_atual.year}'


# In[93]:


#Passo3: Adicionar o dado mais recente a tabela

new_line = {'Dia': dia, 'Seguidores': n_seguidores, 'Seguindo': n_seguindo, 'Publicações': n_publicacoes}
tabela = tabela.append(new_line, ignore_index=True)


# In[94]:


#Passo 4: Atualizar base de dado com a tabela no servidor de dados

tabela.to_csv("DB_IDG_Teste.csv")


# In[ ]:




