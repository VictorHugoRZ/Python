
# Uso de operadores logicos

a = True
b = True

# El operador AND evalua ambos valores y si la condicion de ambos es verdadera, arroja un True
resultado = a and b
print(resultado)  # True

# El operador OR evalua una de las condiciones y si alguna de estas es verdadera, arroja True
resultado = a or b
print(resultado)  # True

# El operador NOT niega el valor que le demos, invirtiendo de True a False y viceversa
resultado = not a
print(resultado)  # False

# Ejercicio operador AND: Numero dentro de un rango establecido
'''
numero = int(input('Introduce un numero: '))
valorMinimo = 0
valorMaximo = 5

if valorMinimo <= numero <= valorMaximo:  # Sintaxis simplificada
    print(f'El numero {numero} esta dentro del rango permitido')
else:
    print(f'El numero {numero} esta fuera del rango permitido')
'''

# Ejercicio operador OR: Asistir al juego
'''
print('Tiene que ir al juego de su hijo pero esto depende de si usted esta de vacaciones o no \n¿Esta de vacaciones?')
vacaciones = False
diaDescando = True

if vacaciones or diaDescando:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')

# Mismo ejercicio con el operador NOT

if not vacaciones or diaDescando:
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')
'''

# Ejercicio Rango de edad entre los 20's y 30's
'''
print('¿Cual es tu edad?')
edad = int(input('Introduce tu edad: '))

veintes = 20 <= edad < 30  # Sintaxis simplificada para evaluar dos condiciones verdaderas (AND)
treintas = 30 <= edad < 40

if veintes or treintas:
    print('Tu edad esta dentro del rango de edad permitido')
else:
    print('Tu edad esta fuera del rango permitido')
'''

'''
Ejercicio comparacion numerica:
Solicita al usuario que de dos valores, determina cual de esos dos valores es el mayor 
numero1 (int)
numero2 (int)
Se debe imprimir el numero de mayor valor (la salida debe ser identica a la siguiente):
Proporciona el numero 1:
Proporciona el numero 2:
El numero mayor es: <numeroMayor>
'''
'''
print('Ingresa dos valores:')
numero1 = int(input('Proporciona el primer valor: '))
numero2 = int(input('Proporciona el segundo valor: '))

if numero1 > numero2:
    print(f'El numero {numero1} es mayor que el numero {numero2}')
else:
    print(f'El numero {numero2} es mayor que el numero {numero1}')
'''

# Ejercicio tienda de libros:
print('Proporcione los siguientes datos del libro:')

nombre = input('Ingrese el Nombre del libro: ')
identificador = int(input('Ingrese el Id del libro: '))
precio = float(input('Ingrese el Precio del libro: '))
envioTipo = input('Indica si el envio en gratuito (True/False): ')

envio = ''
if envioTipo == 'False':
    envio = 'No'
else:
    envio = "Si"

# Primera manera de imprimir informacion en la consola donde tengamos que dar formato de multiples lineas:
# print(f'Nombre: {nombre}\nId: {identificador}\nPrecio: {precio}\nEnvio gratuito: {envio}')

# Segunda manera:
print(f'''
    La informacion del libro es la siguiente:
    Nombre: {nombre}
    Id: {identificador}
    Precio: {precio}
    Envio Gratuito: {envio}
''')
