def calcular_area_rectangulo(base, altura):
  """"Calcula el area de un rectangulo"""
  return base * altura

def mostrar_area_rectangulo(numero, base, altura):
  """Muestra el area de un rectangulo con formato"""
  area = calcular_area_rectangulo(base, altura)
  print(f"El area del rectangulo {numero} ({base}x{altura}) es: {area}")

def main():
  """Funcion principal del programa"""
  # Ejemplo de uso
  mostrar_area_rectangulo(1, 10, 5)
  """Puedes probar con mas rectangulo"""
  mostrar_area_rectangulo(2, 8, 3)

if __name__ == "__main__":
  main()
  mostrar_area_rectangulo(3, 15, 7)