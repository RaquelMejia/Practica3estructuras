def main():
    # Inicialización de variables
    notas = []

    # Lectura de las notas ingresadas por el usuario
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
        
        # Validación para notas entre 0 y 10
        while nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10.")
            nota = float(input(f"Ingrese la nota {i+1} nuevamente: "))
        
        notas.append(nota)

    # Mostrar las notas
    print("\nNotas ingresadas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")

    # Calcular la nota media
    nota_media = sum(notas) / len(notas)
    print(f"Nota media: {nota_media:}")

    # Calcular la nota mas alta y la nota mas baja
    nota_maxima = max(notas)
    nota_minima = min(notas)
    print(f"Nota mas alta: {nota_maxima}")
    print(f"Nota mas baja: {nota_minima}")

if __name__ == "__main__":
    main()