
# Sentencias de control If/Else

'''
condicion = False

if condicion == True:
    print('Condicion valida')
elif condicion == False:
    print('Condicion invalida')
else:
    print('Condicion no reconocida')
'''

'''
Ejercicio de conversion de numero a texto:

numero = int(input('Ingrese un valor entre 1 y 3: '))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Numero Uno'
elif numero == 2:
    numeroTexto = 'Numero Dos'
elif numero == 3:
    numeroTexto = 'Numero Tres'
else:
    numeroTexto = 'Numero fuera de rango'

print(f'El numero proporcionado es {numero}: {numeroTexto}.')
'''

# Uso del Operador Ternario

# condicion = True
#
# # Condicionado comun usando sentencias If/Else
# if condicion == True:
#     print('La condicion es verdadera')
# else:
#     print('La condicion es falsa')
#
# # Condicionado con operador ternario
# print('La condicion es verdadera') if condicion else print('La condicion es falsa')

# Con el operador ternario NO podemos hacer uso de la sentencia ELIF, para esto debemos usar los
# bloques de codigo If/Elif/Else como comunmente los conocemos

'''
Ejercicio Mes del año:
El usuario proporcionara el numero de mes en el que esta para saber en que estacion del año se encuentra, 
esto proporcionando un numero del 1 al 12.
'''

# print('Mes del año')
# mes = int(input('¿En que mes del año te encuentras? (1-12) '))
# estacion = None  # None es el equivalente a Null en otros lenguajes de programacion
#
# if mes == 1 or mes == 2 or mes == 12:
#     estacion = 'Invierno'
# elif mes == 3 or mes == 4 or mes == 5:
#     estacion = 'Primavera'
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = 'Verano'
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = 'Otoño'
# else:
#     estacion = 'Mes Invalido'
#
# print(f'Para el mes {mes}, la estacion correspondiente es: {estacion}')

'''
Ejercicio Etapas de la Vida:
El usuario proporcionara numeros en un rango de entre 0 y 30, los cuales evaluaremos para mostrar una respuesta
en especifico segun el año que nos indiquen
De 0 a 10 años obtendremos ´La infancia es increible...´
De 10 a 20 años obtendremos ´Muchos cambios y mucho estudio...´
De 20 a 30 años obtendremos ´Amor y comienza el trabajo...´
'''

# print('Etapas de la vida')
# edad = int(input('Ingresa tu edad: '))
# etapa = None
#
# if 0 <= edad < 10:
#     etapa = 'La infancia es increible...'
# elif 10 <= edad < 20:
#     etapa = 'Muchos cambios y mucho estudio...'
# elif 20 <= edad <= 30:
#     etapa = 'Amor y comienza el trabajo...'
# else:
#     etapa = 'Etapa de la vida no reconocida'
#
# print(f'{etapa} tienes {edad} años.')

'''
Ejercicio Sistema de calificaciones:
El usuario proporcionara un valor entre 0 y 10
Si esta entre 9 y 10 imprimir la nota A
Si es igual a 8 imprimir la nota B
Si es igual a 7 imprimir la nota C
Si es igual a 6 imprimir la nota D
Si esta entre 0 y 6 imprimir la nota F
'''

print('Sistema de calificaciones')
calificacion = int(input('Ingresa tu calificacion (0-10): '))
nota = None

if 0 <= calificacion < 6:
    nota = 'F'
elif calificacion == 6:
    nota = 'D'
elif calificacion == 7:
    nota = 'C'
elif calificacion == 8:
    nota = 'B'
elif 9 <= calificacion <= 10:
    nota = 'A'
else:
    nota = 'No Valida'

print(f'Tu calificacion es {nota}')
