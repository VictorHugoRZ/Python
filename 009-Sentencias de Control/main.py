
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

condicion = True

# Condicionado comun usando sentencias If/Else
if condicion == True:
    print('La condicion es verdadera')
else:
    print('La condicion es falsa')

# Condicionado con operador ternario
print('La condicion es verdadera') if condicion else print('La condicion es falsa')

# Con el operador ternario NO podemos hacer uso de la sentencia ELIF, para esto debemos usar los
# bloques de codigo If/Elif/Else como comunmente los conocemos

'''
Ejercicio Mes del año:
El usuario proporcionara el numero de mes en el que esta para saber en que estacion del año se encuentra, 
esto proporcionando un numero del 1 al 12.
'''

print('Mes del año')
mes = int(input('¿En que mes del año te encuentras? (1-12) '))
estacion = None  # None es el equivalente a Null en otros lenguajes de programacion

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes Invalido'

print(f'Para el mes {mes}, la estacion correspondiente es: {estacion}')


