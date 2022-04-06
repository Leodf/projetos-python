from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib



with open('./python-modulos/aula9-Strings_template/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Leonardo de Faveri', data=data_atual)

msg = MIMEMultipart()
msg['from'] = ''
msg['to'] = ''
msg['subject'] = 'Atenção: este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso!')
