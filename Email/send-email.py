import smtplib

def prompt(prompt):
    return input(prompt).strip()


fromEmail = prompt("From: ")
toEmail  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
body = ("From: %s\r\nTo: %s\r\n\r\n "
       % (fromEmail, ", ".join(toEmail)))

msg = input('Message: ')
body = body + msg
print("Por favor aguarde, enviando email...")

server = smtplib.SMTP('localhost')
server.set_debuglevel(0)
server.sendmail(fromEmail, toEmail, body)
server.quit()
print('E-mail enviado com sucesso!!!')