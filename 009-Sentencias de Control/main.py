
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

# Con el operador ternario NO podemos hacer uno de la senteencia ELIF, para esto debemos usar los
# bloques de codigo If/Elif/Else como comunmente los conocemos


