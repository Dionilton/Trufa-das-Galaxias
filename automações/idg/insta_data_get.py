import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import date

tabela = pd.read_csv("tabela.csv")

navegador = webdriver.Chrome()

navegador.get("https://www.instagram.com/")
time.sleep(2)

username = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys("$USER_EMAIL")
password.send_keys("$USER_PASSWORD")
time.sleep(1)
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

new_line = {'Dia': dia, 'Seguidores': n_seguidores, 'Seguindo': n_seguindo, 'Publicações': n_publicacoes}
tabela = tabela.append(new_line, ignore_index=True)

tabela.to_csv("tabela.csv")

navegador.quit()
