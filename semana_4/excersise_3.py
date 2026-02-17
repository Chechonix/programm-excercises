import random
numero_secreto = random .randint(1,10)
contador_de_intentos= 0
adivinar_numero= 0
print("Adivina el numero secreto del 1 al 10")
while adivinar_numero != numero_secreto:
 adivinar_numero = int(input("Ingresa tu número: "))
 contador_de_intentos = +1
 if adivinar_numero< numero_secreto:
  print("Elige otro numero")
 elif adivinar_numero > numero_secreto:
  print("Elige otro numero")
 else:
  print("Correcto ese era el numero")
