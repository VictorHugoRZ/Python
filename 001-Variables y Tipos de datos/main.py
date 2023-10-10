
# Tipos de datos en Python

# Primer ejercicio de variables y tipos de datos
x = 10
print(x)  # 10

# Para saber el tipo de una variable podemos usar el metodo type()
print(type(x))  # <class 'int'> Nos indica que nuestra variable es de tipo entero


# Segundo ejercicio de variables y tipos de datos
y = "Hola a todos!"
print(y)  # Hola a todos!

print(type(y))  # <class 'str'>

# Podemos indicar de manera manual el tipo de dato de nuestra variable con un hint o pista

x1: str = "Hola!"
print(x1)  # Hola!
print(type(x1))  # <class 'str'>

# Aun asi podemos inicializar nuestras variables con un tipo de dato diferente al valor que le daremos al declararla

x2: str = 20  # Expected type 'str', got 'int' instead
print(x2)  # 20
print(type(x2))  # <class 'int'>

# Las variables en Python son dinamicas, por lo que pueden apuntar a cualquier tipo de dato que deseemos

# Podemos tener variables de tipo Flotante

x3 = 10.5
print(x3)  # 10.5
print(type(x3))  # <class 'float'>

# Podemos tener variables de tipo Booleano

x4 = True  # o False, tenemos que respetar las mayusculas al inicio de la palabra
print(x4)  # True
print(type(x4))  # <class 'bool'>
