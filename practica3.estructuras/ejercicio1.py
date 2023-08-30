#EJERCICIO 1. DESARROLLE UNA TUPLA CON LOS DOCE MESES DEL AÑO
def obtener_nombre_mes(numero_mes):
    meses = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )

    if 1 <= numero_mes <= 12:
        return meses[numero_mes - 1]
    else:
        return "Mes inválido"

# Pedirle al usuario que ingrese un numero de mes
numero_mes = int(input("Ingresa el numero de mes: "))

nombre_mes = obtener_nombre_mes(numero_mes)
print("El mes es:", nombre_mes)