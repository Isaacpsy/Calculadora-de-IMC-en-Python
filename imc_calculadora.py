def calcular_imc(peso_kg, altura_m):
    """Calcula el Índice de Masa Corporal (IMC)."""
    if altura_m <= 0:
        return "Error: La altura debe ser mayor que cero."
    imc = peso_kg / (altura_m ** 2)
    return imc

def interpretar_imc(imc):
    """Interpreta el valor del IMC según las categorías de la OMS."""
    if isinstance(imc, str) and imc.startswith("Error"):
        return imc
    elif imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad grado I"
    elif 35 <= imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

def obtener_datos_usuario():
    """Obtiene el peso y la altura del usuario desde la entrada."""
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos (kg): "))
            if peso <= 0:
                print("El peso debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para el peso.")

    while True:
        try:
            altura = float(input("Ingrese su altura en metros (m): "))
            if altura <= 0:
                print("La altura debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para la altura.")

    return peso, altura

def main():
    """Función principal para ejecutar la calculadora de IMC."""
    print("Bienvenido a la Calculadora de IMC")
    peso, altura = obtener_datos_usuario()
    imc = calcular_imc(peso, altura)

    if isinstance(imc, str) and imc.startswith("Error"):
        print(imc)
    else:
        interpretacion = interpretar_imc(imc)
        print(f"\nSu IMC es: {imc:.2f}")
        print(f"Categoría: {interpretacion}")

if __name__ == "__main__":
    main()