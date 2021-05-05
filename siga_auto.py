import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path='C:\selenium\geckodriver.exe')
driver.implicitly_wait(1)
driver.get("http://siga.saude.prefeitura.sp.gov.br/sms/login.do?method=logoff")


def doLogin():
    name_login = 'j_username'
    name_pass = 'j_password'
    btn_id = 'confirmar'
    user = input(Enter Login -)
    passw = input(Enter Senha -)
    # driver.get("http://siga.saude.prefeitura.sp.gov.br/sms/login.do?method=logoff")
    input_login = driver.find_element_by_name(name_login)
    input_pass = driver.find_element_by_name(name_pass)
    btn_login = driver.find_element_by_id(btn_id)
    input_login.send_keys(user)
    input_pass.send_keys(passw)
    btn_login.click()


def goToProntoAtendimento():
    prontoAtendimento_Id = 'at_pronto_at'

    iframes = driver.find_elements_by_tag_name('frame')

    driver.switch_to.frame(iframes[0])
    btn_atendimento = driver.find_element_by_id('at')
    btn_atendimento.click()

    driver.switch_to.parent_frame()
    driver.switch_to.frame(iframes[1])
    driver.implicitly_wait(1)
    driver.switch_to.default_content()

    driver.switch_to.frame(iframes[1])

    btn_prontoAtendimento = driver.find_element_by_id('at_pronto_at')
    btn_prontoAtendimento.click()

    driver.implicitly_wait(2)

    btn_prontoAtendimento.is_selected()
    driver.implicitly_wait(2)
    btn_prontoAtendimento.click()
#--------------------- Menu functions ----------------------#

def Sair():
    driver.close()

#--------------------

#def menu():
 #   print('Selecione uma opção: \n', menu)
  #  menu = {
   #     0 : Sair(),
    #    1 : doLogin(),
     #   2 : goToProntoAtendimento()
    #}

#--------------------------------------------------------
driver.implicitly_wait(2)
doLogin()
goToProntoAtendimento()
driver.close()

