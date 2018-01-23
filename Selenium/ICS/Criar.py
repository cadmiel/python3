import time, shutil, os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from faker import Faker
import random

class Login:

    def __init__(self, driver):
        self.driver = driver

    def criar(self):
        if os.path.exists('print//'):
            shutil.rmtree('print//')

        os.mkdir('print//')

        endPoint = input('endPoint: ').strip()

        if len(endPoint) == 0:
            endPoint = 'http://ics:8081/'

        self.driver.get(endPoint)

        username = self.driver.find_element_by_id('username')
        username.clear()

        user = input('login: ').strip()
        if len(user) == 0:
            user = 'teste'

        username.send_keys(user)
        self.driver.get_screenshot_as_file('print//username.png')

        pwd = self.driver.find_element_by_id('pwd')
        pwd.clear()

        password = input('senha: ').strip()
        if len(password) == 0:
            password = 'teste'

        pwd.send_keys(password)
        self.driver.get_screenshot_as_file('print//password.png')

        submit = self.driver.find_element_by_name('Submit')
        submit.submit()
        time.sleep(1)

        self.driver.maximize_window()

class Awb:

    def __init__(self, driver, fake, pedido, numero):
        self.driver = driver
        self.fake = fake
        self.pedido = pedido
        self.numero = numero

    def criar(self):
        self.driver.find_element_by_xpath('//*[@id="dhtmlgoodies_listItem0"]').click()
        time.sleep(1)

        self.driver.find_element_by_xpath("""//*[@id="dhtmlgoodies_listItem3"]""").click()
        time.sleep(1)

        select = Select(self.driver.find_element_by_name('reid'))
        select.select_by_index(1)
        time.sleep(2)

        select = Select(self.driver.find_element_by_name('cnpj_reid'))
        select.select_by_index(1)
        time.sleep(1)

        select = Select(self.driver.find_element_by_name('servico_reid'))
        select.select_by_index(1)
        time.sleep(1)

        select = Select(self.driver.find_element_by_name('tipoEntrega'))
        select.select_by_index(1)
        time.sleep(2)

        self.driver.find_element_by_name('pedido').send_keys(self.pedido)
        self.driver.find_element_by_name('natureza').send_keys(self.fake.last_name())
        select = Select(self.driver.find_element_by_name('qtyvolumes'))
        select.select_by_index(0)
        time.sleep(1)
        self.driver.find_element_by_name('cep').send_keys('20211110')

        cnpjList = [
            '62957659000198', '42765532000160', '40748786000144',
            '66969518000146', '99173675000108', '59392480000126',
            '46499568000108', '07017030000150', '80067414000177'
        ]

        self.driver.find_element_by_name('cpf').send_keys(random.choice(cnpjList))
        self.driver.find_element_by_name('nome').send_keys(self.fake.name())
        self.driver.find_element_by_name('isento').click()
        self.driver.find_element_by_name('enderecoNum').send_keys(self.numero)
        time.sleep(1)
        self.driver.find_element_by_id('tpDocFiscalNFo').click()
        time.sleep(1)
        self.driver.find_element_by_id('nfoTpDoc00').click()
        time.sleep(1)
        self.driver.find_element_by_name('nfoDesc').send_keys(1)
        self.driver.find_element_by_name('nfoNumero').send_keys(1)
        self.driver.find_element_by_name('nfoValor').send_keys(1)
        self.driver.find_element_by_name('nfoValorProd').send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="fsNFo"]/table/tbody/tr[2]/td[4]/img').click()
        time.sleep(1)
        self.driver.find_element_by_class_name('activeDay').click()

        self.driver.get_screenshot_as_file('print//awb_' + self.pedido + '.png')

        self.driver.find_element_by_id('registrar_encomenda').send_keys(Keys.RETURN)

        time.sleep(4)


class Coleta:

    def __init__(self, driver, pedido):
        self.driver = driver
        self.pedido = pedido

    def criar(self):
        self.driver.find_element_by_xpath('//*[@id="dhtmlgoodies_listItem0"]').click()
        time.sleep(1)

        self.driver.find_element_by_xpath("""//*[@id="dhtmlgoodies_listItem7"]/a""").click()
        time.sleep(1)

        self.driver.get_screenshot_as_file('print//coleta_' + self.pedido + '.png')

        self.driver.find_element_by_xpath("""//*[@id="tabela"]/tbody/tr[2]/td[1]/a""").click()
        time.sleep(1)

        self.driver.get_screenshot_as_file('print//antes_aprovar_coleta_' + self.pedido + '.png')

        self.driver.find_element_by_xpath(
            """//*[@id="borda"]/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/form/table/tbody/tr[1]/td/div/font/b/a""").click()
        time.sleep(2)

        self.driver.get_screenshot_as_file('print//apos_aprovacao_coleta_' + self.pedido + '.png')
        self.driver.find_element_by_xpath('//*[@id="dhtmlgoodies_listItem0"]').click()
        time.sleep(1)

        self.driver.get_screenshot_as_file('print//casamento_' + self.pedido + '.png')

        self.driver.find_element_by_xpath("""//*[@id="dhtmlgoodies_listItem7"]/a""").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("""//*[@id="tabela"]/tbody/tr[2]/td[7]/a""").click()
        time.sleep(1)
        select = Select(self.driver.find_element_by_name('criterio'))
        select.select_by_index(1)
        time.sleep(1)
        self.driver.find_element_by_name('scanfield').send_keys(self.pedido)

        self.driver.get_screenshot_as_file('print//pedido_' + self.pedido + '.png')
        self.driver.find_element_by_xpath(
            '//*[@id="borda"]/tbody/tr/td/div/form/table/tbody/tr/td[2]/table/tbody/tr[5]/td/input').send_keys(
            Keys.RETURN)
        time.sleep(1)
        self.driver.find_element_by_name('pesoscan').send_keys('1')
        time.sleep(1)

        self.driver.get_screenshot_as_file('print//peso_' + self.pedido + '.png')
        self.driver.find_element_by_xpath(
            '//*[@id="borda"]/tbody/tr/td/div/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td/input').send_keys(
            Keys.RETURN)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/a').click()

        self.driver.get_screenshot_as_file('print//final_' + self.pedido + '.png')

        time.sleep(4)




