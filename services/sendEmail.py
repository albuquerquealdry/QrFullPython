import smtplib
import email.message

a= "aaa"
def sendemail(password, name,emailenvio):
    
    chave=password
    msgbody= "Olá, {} , segue sua senha em anexo".format(name)
    corpo_email = f"""
    <p>{msgbody}</p>
    <p> {chave}</p>
    <p>Abraços, Aldry </p>    
    """

    msg = email.message.Message()
    msg['Subject'] = "Sua chave de acesso"
    msg['From'] = "albuquerquealdry@gmail.com"
    msg['To'] = (emailenvio)
    password = "aldry877179"
    msg.add_header('Content-type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
   