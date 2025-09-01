# Se dice que la inmutibilidad no permite modificar el valor de un string por lo tanto a la variable que contiene
# el string se le asigna un nuevo valor, pero el string original no se modifica
cadena = "Hola Mundo"

#cadena[1] = "a" # Esto no se puede hacer porque los strings son inmutables,cadena[1] = "a" 
# TypeError: 'str' object does not support item assignment

cadena = "Adios Mundo"
print(cadena)