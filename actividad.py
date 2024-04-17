import os
os.system ("cls")


totalIngresos = 0
totalIngresos = 0
banderaCantidad = True
banderaPrecio = True
while banderaCantidad:
    try:
        cantidad= int(input("ingrese cantidad de pasajes "))
        if cantidad > 0 
        for x in range (cantidad):
            while banderaPrecio:
                for x in range(cantidad):
                    try:
                        precio = int(input(f"ingrese precio de pasaje {x+1}\n"))
                        totalIngresos = totalIngresos + precio
                        break
                    except:
                        print ("no existe ese precio")
                    
    except:
      print ("numero no valido")
    break
print(f"para {cantidad} pasajes, el valor a pagar es: ${totalIngresos}")
    




   