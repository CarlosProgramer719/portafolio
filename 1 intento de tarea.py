def mostrar_menu():
    print("Menú de Operaciones")
    print("1 Repetir cierta cantidad de dígitos")
    print("2 Multiplicar los dígitos *5")
    print("3 Cuenta regresiva de 2 en 2")
    print("4 ¿Cuántos números desea sumar?")
    print("5 Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")
        
    if opcion == "1":
        cantidad_numeros = int(input("¿Cuántos números deseas ingresar?: "))
        for _ in range(cantidad_numeros):
            numero = int(input("Ingresa un número: "))
            print(f"Has ingresado el número: {numero}")
    
    elif opcion == "2":
        numero = int(input("Ingresa un número: "))
        veces = int(input("¿Cuántas veces quieres multiplicarlo?: "))
        print("Resultados:")
        for i in range(veces):
            numero *= 5 
            print(f" {i + 1}: {numero}")
    
    elif opcion == "3":
        numero = int(input("Ingresa un número para la cuenta regresiva: "))
        print(f"Cuenta regresiva desde {numero} hasta 0 (de 2 en 2):")
        for i in range(numero, -1, -2):
            print(i)
    
    elif opcion == "4":
        cantidad = int (input("¿Cuántos números deseas sumar? "))
        suma_total = 0
        for i in range(cantidad):
            numero = float(input(f"Ingresa el número {i + 1}: "))
            suma_total += numero
        print(f"La suma total es: {suma_total}")
    
    elif opcion == "5":
        print("Hasta luego")
    
    else:
        print("Opción inválida. Intenta nuevamente.")