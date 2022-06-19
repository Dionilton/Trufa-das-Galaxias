# Insta Data Get - IDG

Aplicação para coleta de dados do perfil do Instagram institucional por meio de Web Scraping ultilizando a biblioteca Selenium.

## Pré-Requisitos

Você precisa ter o Python instalado em sua máquina, a versão 3.5 ou superiores. Recomendo também a instalação do Jupyter que vem integrado com o pacote Anaconda. Nele já vem instalada bibliotecas importantes para essa aplicação como o Pandas.

## Instalando as bibliotecas 

Usando o interpretador Python de sua aplicação ou caso esteja usando o Jupyter pode-se usar uma célula auxiliar apenas para as instalações das bibliotecas.
Instale o Selenium:

```Python
!pip install selenium
```

Caso não esteja usando o Jupyter, você também vai precisar instalar o Pandas:

```Python
!pip install pandas
```

Caso for torna sua versão do projeto público, recomento fortemente o uso do python-dotenv para gerenciamento das varáveis de ambiente que pussui dados sensíveis.
Instalando o python-dotenv:

```Python
!pip install python-dotenv
```

## Configurações para o funcionamento do Selenium

Para que o Selenium funcione perfeitamente, além da instalação da biblioteca, ele utiliza o Webdrive do navegador para controlá-lo. Cade nevegador possui o seu Webdrive, e você precisa [baixá-lo](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) e colocá-lo na mesma pasta que está o interpretador Python da sua aplicação, se estiver usando o Windows e o Jupyter, normalmente ele fica no path: C:\Users\usuario\anaconda3.

Pronto, feito tudo isso, basta ajustar o código com suas especificações de XPATH, usuário e senha, e está pronto para rodar a aplicação.

Vale ressaltar também, que essa aplicação ainda não está pronta e segue em fase de testes para que seja feito os devidos ajustes e correção de bugs.
