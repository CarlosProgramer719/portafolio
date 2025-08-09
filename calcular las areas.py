#Triangulo 
tri=[]
b=int(input("dame la base "))
al=int(input("dame la altura "))
tri.append(b)
tri.append(al)
tarea=(tri[0]*tri[1])/2
tri.append(tarea)
print(tri)

#Rectángulo 
cuadrado = []
b = int(input("Dame la base del cuadrado: "))
al = int(input("Dame la altura del cuadrado: "))
cuadrado.append(b)
cuadrado.append(al)
tarea = cuadrado[0] * cuadrado[1]  # Fórmula del cuadrado (sin /2)
cuadrado.append(tarea)
print("Cuadrado/Rectángulo:", cuadrado)

# ===== CUADRADO =====
cuadrado = []
lado = float(input("Dame el lado del cuadrado: "))
cuadrado.append(lado)
area = lado * lado  # Fórmula: Lado²
cuadrado.append(area)
print("Cuadrado:", cuadrado)

#Rombo
rombo = []
d_mayor = float(input("Dame la diagonal mayor del rombo: "))
d_menor = float(input("Dame la diagonal menor del rombo: "))
rombo.append(d_mayor)
rombo.append(d_menor)
area = (d_mayor * d_menor) / 2  # Fórmula: (Dmayor * Dmenor)/2
rombo.append(area)
print("Rombo:", rombo)

#Circulo
circulo = []
radio = float(input("Dame el radio del círculo: "))
circulo.append(radio)
area = 3.1416 * (radio ** 2)  # Fórmula: π * radio²
circulo.append(area)
print("Círculo:", circulo)

#Trapecio
trapecio = []
base_mayor = float(input("Dame la base mayor del trapecio: "))
base_menor = float(input("Dame la base menor del trapecio: "))
altura = float(input("Dame la altura del trapecio: "))
trapecio.append(base_mayor)
trapecio.append(base_menor)
trapecio.append(altura)
area = ((base_mayor + base_menor) * altura) / 2  # Fórmula: (B + b)*h/2
trapecio.append(area)
print("Trapecio:", trapecio)

#Romboide
romboide = []
base = float(input("Dame la base del romboide: "))
altura = float(input("Dame la altura del romboide: "))
romboide.append(base)
romboide.append(altura)
area = base * altura  # Fórmula: base * altura (igual que rectángulo)
romboide.append(area)
print("Romboide:", romboide)