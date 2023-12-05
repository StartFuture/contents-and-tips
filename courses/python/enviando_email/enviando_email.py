import smtplib # Importação Da lib built-in para envio de e-mail
import email.message # Importação Da lib built-in para envio de e-mail

titulo = 'Titulo do E-mail'
conteudo = '''<h1>Conteúdo E-mail</h1>''' # Conteúdo do e-mail, pode ser HTML
email_origem = 'email_origem@gmail.com' # O seu e-mail do gmail
email_destino = 'email_destino@gmail.com' # Pode ser outros além do gmail
pin_gmail = 'seu_pin_do_gmail' # O pin do seu gmail

msg = email.message.Message() # Instanciando Objeto
msg['Subject'] = titulo # Adicionando o titulo
msg['From'] = email_origem # Adicionando o e-mail de origem
msg['To'] = email_destino # Adicionando o e-mail de destino
msg.add_header('Content-Type', 'text/html') # Adicionando o tipo de conteúdo
msg.set_payload(conteudo) # Adicionando o conteúdo do e-mail

servidor_smpt_google = smtplib.SMTP('smtp.gmail.com: 587') # Instanciando Objeto
servidor_smpt_google.starttls() # Iniciando conexão
servidor_smpt_google.login(msg['From'], pin_gmail) # Realizando login
servidor_smpt_google.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) # Enviando e-mail