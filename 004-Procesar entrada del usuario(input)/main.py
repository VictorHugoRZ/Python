
# Utilizaremos la funcion Input para procesar la entrada de datos del usuario

# Esta funcion nos permite ingresar valores mediante la consola para asignarlos a nuestras variables,
# estos datos se declararan en nuestras variables con el tipo String, a pesar de ingresar numeros o booleanos
# en consola

print("Ingresa cualquier valor:")
resultado = input()
print(type(resultado))
print(resultado)

# Conversion de la entrada de datos

# Manera 1
# print("Calculadora \nIngresa el primer valor:")
# resultado1 = input()
# print("Ingresa el segundo valor:")
# resultado2 = input()
# print("El resultado de la suma es:")
# print(int(resultado1) + int(resultado2))

# Manera 2
print("Calculadora de suma")
resultado1 = int(input("Ingrese el primer valor: "))
resultado2 = int(input("Ingrese el segundo valor: "))
print("El resultado es:", resultado1 + resultado2)

# Ejercicio; ¿Como estuvo tu dia?
miDia = input("¿Como estuvo tu dia? (Del 1 al 10):")
print("Mi dia estuvo de", miDia)
