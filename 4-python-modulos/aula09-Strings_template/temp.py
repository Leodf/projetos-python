from string import Template
from datetime import datetime

with open('./python-modulos/aula9-Strings_template/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Leonardo de Faveri', data=data_atual)

print(corpo_msg)