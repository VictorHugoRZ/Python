
# Uso de operadores de comparacion

a = 3
b = 4

# Igual que (igualdad)
resultado = a == b
print(f'El resultado de la comparacion es: {resultado}')  # False

# Distinto que
resultado = a != b
print(f'El resultado de la comparacion es: {resultado}')  # True

# Mayor que
resultado = a > b  # Tambien existe mayor o igual que >=
print(f'El resultado de la comparacion es: {resultado}')  # False

# Menor que
resultado = a < b  # Tambien existe menor o igual que <=
print(f'El resultado de la comparacion es: {resultado}')  # True

'''
Ejercicio Numero par o impar:
Desarrolla un algoritmo que reciba por parametro un numero x y verifique si este es par o impar
'''

print('¿Par o impar?')
numero = int(input('Introduzca un numero:'))
if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')

'''
Ejercicio Mayor de edad:
Desarrolla un algoritmo que reciba por parametro la edad del usuario y verifique si este es mayor de edad
'''

print('¿Eres mayor de edad?')
edad = int(input('Introduce tu edad: '))
if edad >= 18:
    print(f'Tienes {edad} años, eres mayor de edad')
else:
    print(f'Tienes {edad} años, eres menor de edad, vuelve cuando tengas 18 o mas años')

