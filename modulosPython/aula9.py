"""
Aula 9

"""

from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

with open('aula8.html', 'r') as file:
    template = Template(file.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    # corpo_msg = template.substitute(nome='João Vitor', data=data_atual)
    corpo_msg = template.safe_substitute(nome='João Vitor', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'João Vitor'
msg['to'] = '@email.com'  # cliente
msg['subject'] = 'ATENÇÃO: ESTE É UM E-MAIL DE TESTE'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

user = '@gmail.com'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user, senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso!')
