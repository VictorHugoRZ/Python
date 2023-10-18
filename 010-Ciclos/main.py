
# Ciclo WHILE

contador = 0

while contador <= 3:
    print(contador)
    contador += 1
else:
    print('Fin del ciclo While')


# Ejercicio ciclo While:
# Imprimir en consola los valores del 0 al 5

numero = 0

while numero <= 5:
    print(numero)
    numero += 1
else:
    print('Hemos llegado al valor final de manera ascendente')


# Ejercicio ciclo While:
# Imprimir en consola los valores descendentes del 5 al 0

numero = 5

while numero >= 0:
    print(numero)
    numero -= 1
else:
    print('Hemos llegado al valor final de manera descendente')

# Ciclo FOR

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin ciclo For')

'''
La palabra reservada BREAK rompe la ejecucion del codigo cuando se cumple una condicion especifica
cadena = 'Hola'

for letra in cadena:              H  <--- Salida por consola
    if letra == 'l':              o       Busca si existe una letra l con el condicional If y al encontrarla
        break <------- BREAK              rompe la ejecucion del bucle, esta puede ser una condicion o valor 
    print(letra)                          especificos, no solo una letra dentro de un string
else:
    print('Fin ciclo For')
    
-----------------------------------------------------------------------------------------------------------
    
La palabra reservada CONTINUE 'salta' u 'omite' cierto bloque de codigo que cumple una condicion especifica
cadena = 'Hola'

for letra in cadena:                   H  <--- Salida por consola
    if letra == 'l':                   o       Busca si existe la letra l con el condicional If y al
        continue <------- CONTINUE     a       encontrarla omite la ejecucion del bloque de codigo que 
    print(letra)                               incluye esa letra, esta puede ser una condicion o un 
else:                                          valor especifico, no solo una letra dentro de un string
    print('Fin ciclo For')
'''

# Ciclo FOR IN RANGE

# Buscando numeros pares dentro de un rango determinado
for i in range(100, 200):
    if i % 2 == 0:
        print(f'Valor: {i}')
else:
    print('Fin del ciclo')

# Buscando numeros pares dentro de un rango usando la palabra reservada Continue
for i in range(100, 150):
    if i % 2 != 0:
        continue
    print(f'Valor {i}')
else:
    print('Fin del ciclo')
