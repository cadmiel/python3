import time, shutil, os, sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from faker import Faker
import random
from Criar import Coleta, Awb, Login

#driver = webdriver.Chrome('/Users/victor/Downloads/chromedriver_')

#driver = webdriver.Chrome(executable_path='../mac')
driver = webdriver.Chrome(executable_path='../windows')

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


    # # driver.set_page_load_timeout(30)

    # driver.find_element_by_xpath("//select[@name='servico']/option[text()='TI']").click()

#     opt = True
#     while opt == True:
#
#         driver.set_page_load_timeout(30)
#
#         if os.path.exists('print//'):
#             shutil.rmtree('print//')
#
#         os.mkdir('print//')
#
#         el = driver.find_element_by_name('identifier')
#         email = input('Digite seu email: ')
#         el.send_keys(email)
#         driver.get_screenshot_as_file('print//email.png')
#         el.send_keys(Keys.RETURN)
#
#         password = input('Digite sua senha: ')
#         el = driver.find_element_by_name('password')
#         el.clear()
#         el.send_keys(password)
#         driver.get_screenshot_as_file('print//password.png')
#         el.send_keys(Keys.RETURN)
#
#         time.sleep(1)
#
#         try:
#             txtError = driver.find_element_by_class_name('RxsGPe').text
#         except NoSuchElementException:
#             txtError = ''
#
#         time.sleep(5)
#
#         if len(txtError) >= 3:
#             print('Erro Autenticacao: ',txtError)
#             driver.get_screenshot_as_file('print//txtError.png')
#             driver.execute_script("window.history.go(-1)")
#
#         else:
#             time.sleep(3)
#             opt = False
#             driver.get_screenshot_as_file('print//success.png')
#
except Exception as error:
    driver.get_screenshot_as_file('print//error_exception.png')
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print('Erro: ',error)

driver.quit()
