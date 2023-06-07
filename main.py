import yagmail

email = 'programaciondairo@gmail.com'
contraseña ='tcocsjjbsamwaeqx'

yag = yagmail.SMTP(user=email, password= contraseña)

destinararios = ['dairoxd155@gmail.com']
asunto = 'Prueba de envio'
mensaje = 'Hola, esto es una prueba de envio de correo'


yag.send(destinararios, asunto, mensaje )