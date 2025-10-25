# Programa que solicita dos números enteros y muestra diferentes resultados

# Pedir al usuario dos números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Calcular las operaciones solicitadas
suma = numero1 + numero2
diferencia = numero1 - numero2
producto = numero1 * numero2
promedio = (numero1 + numero2) / 2
distancia = abs(numero1 - numero2)
maximo = max(numero1, numero2)
minimo = min(numero1, numero2)

# Mostrar los resultados
print("\nResultados:")
print(f"La suma es: {suma}")
print(f"La diferencia es: {diferencia}")
print(f"El producto es: {producto}")
print(f"El promedio es: {promedio}")
print(f"La distancia (valor absoluto de la diferencia) es: {distancia}")
print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")

