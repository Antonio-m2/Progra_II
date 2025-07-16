matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

num_filas = len(matriz)
num_columnas = len(matriz[0])  
for i in range(num_filas):
  for j in range(num_columnas):
    elemento = matriz[i][j]
    print(f"Elemento en la fila {i}, columna {j}: {elemento}")


for fila_actual in matriz:
  for elemento in fila_actual:
    print(elemento, end=" ")
  print()

matriz = [[col + fila * 5 + 1 for col in range(5)] for fila in range(5)]
for fila in matriz:
  print(" ".join(str(elem) for elem in fila))
print()
teclado_numerico = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9'],
  ['*', '0', '#']
]
for fila in teclado_numerico:
  print(" ".join(fila))
    