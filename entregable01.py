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

nom_jugador=float(input("INGRESE EL NUMERO DEL JUGADOR: \n"))


if nom_jugador>=0 and nom_jugador <0.99:
    print("El jugador pertenece a la liga HIERRO")
elif nom_jugador>=1.00 and nom_jugador <=1.99:
    print("El jugador pertenece a la liga BRONCE")
elif nom_jugador>=2.00 and nom_jugador <=2.99:
    print("El jugador pertenece a la liga PLATA")
elif nom_jugador>=3.00 and nom_jugador <=3.99:
    print("El jugador pertenece a la liga ORO")
elif nom_jugador>=4.00 and nom_jugador <=4.99:
    print("El jugador pertenece a la liga PLATINO")
elif nom_jugador>=5.99 and nom_jugador <=5.99:
    print("El jugador pertenece a la liga DIAMANTE")
elif nom_jugador>=6.00 and nom_jugador <=6.99:
    print("El jugador pertenece a la liga MAESTRO")
elif nom_jugador>=7.00 and nom_jugador <=7.99:
    print("El jugador pertenece a la liga GRAN MAESTRO")
elif nom_jugador>=8.00 and nom_jugador <=8.99:
    print("El jugador pertenece a la liga RETADOR ")
else:
    print("*******DIGITO UN NUMERO INVALIDO******* \n Ejecute de nuevo el código")