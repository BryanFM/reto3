count = 1
list_notas = []
#validar numero nota
def inputnumber(message):
  while True:
    try:
       nota = int(input(message))       
    except ValueError:
       print("El dato ingresado no es numérico")
       continue
    else:
       return nota

while count <= 5:
    nota = inputnumber(f"Ingrese nota {count}: ")

    list_notas.append(nota)

    count = count + 1
print(f"Sus notas son {list_notas}")
promedio = sum(list_notas) / len(list_notas)
nota_mayor = max(list_notas)
nota_menor = min(list_notas)
print(f"Su promedio es {promedio}")
print(f"Su nota más alta es {nota_mayor}")
print(f"Su nota más baja es {nota_menor}")