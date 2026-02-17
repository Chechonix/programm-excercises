nombre_del_usuario= input("ingrese su nombre")
apellido_del_usuiario= input("ingrese su apellido")
edad_del_usuario = int(input("Ingrese su edad: "))
print(f"{nombre_del_usuario}+{apellido_del_usuiario}+{edad_del_usuario}")
if( edad_del_usuario <= 3):
    print ("el usuario es un bebé")
elif (edad_del_usuario<=12):
    print ("el usuario es un niño")
elif(edad_del_usuario<=14):
    print ("el usuario es un preadolecente")
elif(edad_del_usuario<=18):
    print ("el usuario es un adolecente")
elif(edad_del_usuario<=35):
    print ("el usuario es un adulto joven")
elif(edad_del_usuario<=64):
    print ("el usuario es un adulto")
elif(edad_del_usuario>64):
    print ("el usuario es un adulto mayor")
    