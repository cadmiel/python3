from bottle import run
import time, shutil, os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome('/Users/victor/Downloads/chromedriver_')
driver = webdriver.Chrome('C:/Users/T41533/Downloads/chromedriver')

try:

    if os.path.exists('print//'):
        shutil.rmtree('print//')

    os.mkdir('print//')

    driver.get('https://www.google.com/intl/pt/gmail/about/#')
    driver.find_element_by_class_name('gmail-nav__nav-link__sign-in').click()

    # driver.set_page_load_timeout(30)
    opt = True
    while opt == True:

        driver.set_page_load_timeout(30)

        if os.path.exists('print//'):
            shutil.rmtree('print//')

        os.mkdir('print//')

        el = driver.find_element_by_name('identifier')
        email = input('Digite seu email: ')
        el.send_keys(email)
        driver.get_screenshot_as_file('print//email.png')
        el.send_keys(Keys.RETURN)

        password = input('Digite sua senha: ')
        el = driver.find_element_by_name('password')
        el.clear()
        el.send_keys(password)
        driver.get_screenshot_as_file('print//password.png')
        el.send_keys(Keys.RETURN)

        time.sleep(1)

        try:
            txtError = driver.find_element_by_class_name('RxsGPe').text
        except NoSuchElementException:
            txtError = ''

        time.sleep(5)

        if len(txtError) >= 3:
            print('Erro Autenticacao: ',txtError)
            driver.get_screenshot_as_file('print//txtError.png')
            driver.execute_script("window.history.go(-1)")

        else:
            time.sleep(3)
            opt = False
            driver.get_screenshot_as_file('print//success.png')

except Exception as error:
    driver.get_screenshot_as_file('print//error_exception.png')
    print('Erro: ',error)

driver.quit()

# run(reloader=True)

#java -jar selenium-server-standalone-3.8.0.jar
