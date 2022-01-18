from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia Pessoal, eu sou Leonardo e estou criando um bot"
        self.grupos = ["Eu mesmo","Valentine"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome()
    
    def EnviarMensagens(self):

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()