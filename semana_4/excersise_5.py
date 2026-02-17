total_de_notas = 0
contador_de_nota = 1
nota_actual = 0
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0
total_de_notas = int(input("Ingrese la cantidad de notas: "))
while contador_de_nota <= total_de_notas:
    print(f"Ingrese la nota número {contador_de_nota}: ")
    nota_actual = int(input("> "))
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas += 1
        promedio_de_notas_desaprobadas += nota_actual
    else:
        cantidad_de_notas_aprobadas += 1
        promedio_de_notas_aprobadas += nota_actual
    promedio_de_notas_total += (nota_actual / total_de_notas)
    contador_de_nota += 1
if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas
else:
    promedio_de_notas_aprobadas = 0

if cantidad_de_notas_desaprobadas > 0:
    promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
else:
    promedio_de_notas_desaprobadas = 0
print("Resultados")
print(f"Cantidad de notas aprobadas: {cantidad_de_notas_aprobadas}")
print(f"Promedio de notas aprobadas: {promedio_de_notas_aprobadas}")
print(f"Cantidad de notas desaprobadas: {cantidad_de_notas_desaprobadas}")
print(f"Promedio de notas desaprobadas: {promedio_de_notas_desaprobadas}")
print(f"Promedio total de notas: {promedio_de_notas_total}")

		