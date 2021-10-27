print("-------BIENVENIDO A LIGUE OF ANDRE-------")
print("                  /\                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")    
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                [====]                     ")
print("                  ||                     ")
print("                  ||                     ")
print("                 [==]                     ")
print("-----------------------------------------")
print(" ")

name=float(input("INGRESE EL NUMERO DEL JUGADOR: \n"))


if name>=0 and name <1:
    print("El jugador pertenece a la liga HIERRO")
elif name>1 and name <2:
    print("El jugador pertenece a la liga BRONCE")
elif name>2 and name <3:
    print("El jugador pertenece a la liga PLATA")
elif name>3 and name <4:
    print("El jugador pertenece a la liga ORO")
elif name>4 and name <5:
    print("El jugador pertenece a la liga PLATINO")
elif name>5 and name <6:
    print("El jugador pertenece a la liga DIAMANTE")
elif name>6 and name <7:
    print("El jugador pertenece a la liga MAESTRO")
elif name>7 and name <8:
    print("El jugador pertenece a la liga GRAN MAESTRO")
elif name>8 and name <9:
    print("El jugador pertenece a la liga RETADOR \n Ejecute de nuevo el código")
else:
    print("*******DIGITO UN NUMERO INVALIDO*******")