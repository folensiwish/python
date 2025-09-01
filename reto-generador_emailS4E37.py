#Generador de email
#Crea un programa para generar un email a partir de los siguientes datos
#Nombre : Ubaldo Acosta Soto
#Empresa : Global Mentoring
#Dominio: com.mx
#Resultado final : email: ubaldo.acosta.soto@globalmentoring.com.mx

nombre = input("Ingrese su nombre: ")
empresa = "Global Mentoring"
dominio = "com.mx"

nombre = nombre.lower()
nombre = nombre.replace(" ", ".")
empresa = empresa.lower()
empresa = "".join(empresa.split()) #Sirve para juntar una cadena que tiene espacios entre medio 
                                   #(No use strip porque solo elimina los espacios incial y final) y necesitaba eliminar el espacio entremedio

email = f'email: {nombre}@{empresa}.{dominio}'
print(email)
