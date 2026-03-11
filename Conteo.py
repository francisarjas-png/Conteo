texto = "gato perro gato pajaro pez gato perro"
palabras = texto.split()
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Texto:", texto)
print("\nConteo de palabras:")
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}:")