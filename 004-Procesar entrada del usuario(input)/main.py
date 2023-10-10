
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

# Ejercicio 1; ¿Como estuvo tu dia?
miDia = input("¿Como estuvo tu dia? (Del 1 al 10):")
print("Mi dia estuvo de", miDia)

# Ejercicio 2: Datos de libro y autor
# Se solicita incluir la siguiente informacion acerca de un libro:
# Titulo
# Autor
# Debes imprimir la informacion en el siguiente formato:
# Proporciona el titulo:
# Proporciona al autor:
# <Titulo> fue escrito por <Autor>
print("¿Que libro estas leyendo?")
titulo = input("Escribe el titulo: ")
autor = input("Escribe el autor: ")
print("Estoy leyendo", titulo, "y fue escrito por", autor)
