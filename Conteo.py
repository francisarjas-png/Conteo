texto = "Gato Perro gato Pajaro pez GATO perro Pez Gato PAJARO Pez Gato PEZ"
palabras = texto.lower().split()
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
palabras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)
print("Texto original:", texto)
print("\nConteo de palabras")
for palabra, cantidad in palabras_ordenadas:
    print(f"{palabra}: {cantidad}")