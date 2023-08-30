#EJERCICIO 2. DESARROLLAR UN PROGRAMA DONDE EL USUARIO INGRESE UNA CADENA
#Solicitar al usuario ingresar una cadena
cadena = input("Ingresa una cadena: ")

#Dividir la cadena en palabras 
lista_palabras = cadena.split()

#Obtener la cantidad de palabras
cantidad_palabras = len(lista_palabras)

#Mostrar la cantidad de palabras
print(f"La cadena tiene {cantidad_palabras} palabra(s).")

