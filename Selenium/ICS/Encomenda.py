import time, shutil, os, sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from faker import Faker
import random
from Criar import Coleta, Awb, Login
import platform

if  'windows' in platform.system():
    chromeDriver = '../windows'
else:
    chromeDriver = os.getcwd()+'/Selenium/mac'

driver = webdriver.Chrome(executable_path=chromeDriver)

try:

    fake = Faker('pt_BR')

    print('Precione ENTER caso deseje usar informação padrão')

    login = Login(driver)
    login.criar()

    pedido = str(time.time()).split('.')

    print('**************************************')
    print('ID Pedido: ', pedido[0])
    print('**************************************')

    awb = Awb(driver, fake, pedido[0], pedido[0])
    coleta = Coleta(driver, pedido[0])

    awb.criar()
    coleta.criar()

except Exception as error:
    driver.get_screenshot_as_file('print//error_exception.png')
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print('Erro: ',error)

driver.quit()
