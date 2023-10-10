
# Podemos mandar a imprimir datos a la consola de unna manera mas eficiente, por ejemplo:

# Operador de suma (+)

operando1 = 10
operando2 = 20
suma = operando1 + operando2

# Primera Manera
print("El resultado de la suma es:", suma)  # El resultado de la suma es: 30

# Segunda Manera (mas eficiente)
print(f'El resultado de la suma es: {suma}')  # El resultado de la suma es: 30

# Ejercicio 1: implementa el nuevo metodo de impresion de datos con una calculadora

print('Calculadora (suma)')
numero1 = int(input('Introduce el primer valor: '))
numero2 = int(input('Introduce el segundo valor: '))
print(f'El resultado final es: {numero1 + numero2}')

# Operador de resta (-)

numero3 = 20
numero4 = 15
resta = numero3 - numero4
print(f'El resultado de la resta es: {resta}')

# Operador de multiplicacion (*)

numero5 = 8
numero6 = 8
multiplicacion = numero5 * numero6
print(f'El resultado de la multiplicacion es: {multiplicacion}')

# Operador de division (/)

numero7 = 80
numero8 = 7
division = numero7 / numero8
print(f'El resultado de la division es: {division}')  # 11.428571428571429

'''
La division que acabamos de hacer nos da un numero de tipo flotante, es decir, decimal, si no queremos que el
resultado sea de tipo flotante y solo queremos el entero sin los decimales podemos hacer lo siguiente:
'''
division1 = numero7 // numero8  # Hacemos la division con doble barra divisoria
print(f'El resultado de la division que solo retorna valores enteros es: {division1}')  # 11

# Operador de modulo o resto (%)

numero9 = 20
numero10 = 6
modulo = numero9 % numero10
print(f'El modulo de la division es: {modulo}')  # 2

# Operador de exponente (**)

numero11 = 2
numero12 = 3
exponente = numero11 ** numero12
print(f'El resultado de el numero exponenciado es: {exponente}')  # 8

'''
Ejercicio 2: Area y Perimetro de un rectangulo
Se solicita calcular el area y perimetro de un rectangulo, para ello debemos crear las siguientes variables:
alto (int)
ancho (int)
El usuario debe proporcionar los valores del largo, ancho y despues se debe imprimir el resultado en el
siguiente formato:

Proporciona el alto:
Proporciona el ancho:

Area: <area>
Perimetro: <perimetro>
'''

print('Calculadora de Area y Perimetro de rectangulos')
alto = int(input('Proporciona el alto: '))
ancho = int(input('Proporciona el ancho: '))
print(f'Area: {ancho * alto}')
print(f'Perimetro: {(ancho * 2) + (alto * 2)}')
