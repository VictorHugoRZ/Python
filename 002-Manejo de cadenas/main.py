# Concatenacion de cadenas con variables

miGrupoFavorito = "Avenged Sevenfold"
textoAdicional = "por sus obligados pesados"

print("Mi banda favorita es " + miGrupoFavorito + " " + textoAdicional)
# Mi banda favorita es Avenged Sevenfold por sus obligados pesados

# Tambien podemos concatenar variables con comas, como en Golang (Go)

print("Mi banda favorita es", miGrupoFavorito)  # la coma ya nos agrega el espacio
# Mi banda favorita es Avenged Sevenfold

# Concatenacion de numeros como cadenas o enteros

numero1 = "1"
numero2 = "2"
print(numero1 + numero2)  # 12, los toma como strings

numero3 = 3
numero4 = 4
print(numero3 + numero4)  # 7, toma nuestros valores como enteros y realiza la suma

# Podemos convertir los strings de numeros a enteros con la funcion Int()

print(int(numero1) + int(numero2))  # 3
