def clasificion_peliculas(edad):

  if edad < 0:
    return "Edad no valida"
  elif edad < 13:
    return "Te recomendamos peliculas clasificadas G o PG"
  elif edad < 18:
    return "Puedes ver peliculas clasificadas PG-13"
  else:
    return "!Puedes ver peliculas clasificadas R¡"


# Pruebas Unitarias
assert clasificion_peliculas(20) == "!Puedes ver peliculas clasificadas R¡", "Error para edad 20"
assert clasificion_peliculas(15) == "Puedes ver peliculas clasificadas PG-13", "Error para edad 15"
assert clasificion_peliculas(10) == "Te recomendamos peliculas clasificadas G o PG", "Error para edad 10"
assert clasificion_peliculas(-5) == "Edad no valida", "Error para edad enegativa"

print("Pruebas unitarias superadas")

while True:
  try:
    edad = int(input("Ingresa tu edad: "))
    resultado = clasificion_peliculas(edad)
    print(f" {resultado}")
  except ValueError:
    print("Ingresa un valor numerico valido")
    continue

  continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
  if continuar != "s":
    break

print("Programa terminado Antonio Moreno")
