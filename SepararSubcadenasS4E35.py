# Separar en sub cadenas el string 
#El parametro que ingresamos al split se puede usar con cualquier caracter que tenga el string
#o por si no hay entre medio caracteres se puede realizar con el espacio dejando solo 
#las entre comillas y un espacio entre estas
cadena = "Juan , 30 , Mexico"
separador = cadena.split(",")
print(separador)

cadena = "Hola Mundo"
separador = cadena.split(" ")
print(separador)
