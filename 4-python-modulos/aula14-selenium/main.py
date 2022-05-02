
from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = './python-modulos/aula14-selenium/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('user-data-dir=./python-modulos/aula14-selenium/Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar no Sign in')
    
    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('')
            input_password.send_keys('')
            sleep(2)
            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login', e)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
            perfil.click()
            sleep(1)
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            logout = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            logout.click()
        except Exception as e:
            print('Não foi possível fazer o logout:', e)
    
    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def sair(self):
        self.chrome.quit()

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clica_sign_in()
    chrome.faz_login()
    chrome.clica_perfil()
    chrome.verifica_usuario('Leodf')

    chrome.faz_logout()
    sleep(5)
    chrome.sair()

    