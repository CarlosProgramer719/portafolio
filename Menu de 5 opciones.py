while True:
    print("Menú de Operaciones")
    print("1. Suma")
    print("2. Multiplicación")
    print("3. División")
    print("4. Cuenta regresiva")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    if opcion == "1":
        # SUMA
        resultado = 5 + 3
        print("Ejemplo de suma:", resultado)
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif opcion == "2":
        # MULTIPLICACIÓN
        resultado = 5 * 3
        print("Ejemplo de multiplicación:", resultado)
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif opcion == "3":
        # DIVISIÓN
        resultado = 10 / 2
        print("Ejemplo de división:", resultado)
        num1 = float(input("Ingresa el dividendo: "))
        num2 = float(input("Ingresa el divisor: "))
        if num2 == 0:
            print("Error: No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
    elif opcion == "4":
        # CUENTA REGRESIVA 
        print("Cuenta Regresiva ---")
        try:
            numero_inicio = int(input("Ingresa un número positivo: "))
            if numero_inicio < 0:
                print("¡El número debe ser positivo!")
            else:
                print("Iniciando cuenta...")
                while numero_inicio >= 0:
                    print(numero_inicio)
                    numero_inicio -= 1
        except ValueError:
            print("Error: Ingresa un número entero válido.")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Intenta de nuevo.")