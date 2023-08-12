tb= 5

n=0
fecha=""
costtal=0

n=int(input("Ingrese la cantidad de boletas a comprar: "))
fecha=input("La boleta es para fin de semana? (si o no): ")


#Condicional para la fecha.
if fecha=="si":
    costtal=tb*1.20
else:
    costtal=tb


#Proceso segun eleccion de palco.
palco=input("Escribe a, b o c segun el palco que quieras comprar: ")
if palco=="a":
    costtal+=tb*.1  #costtal= costtal + tb*.1 
elif palco=="b":
    costtal+=tb*.05


#Proceso de descuento por cantidad de boletas.
if n>=5 and n<=10:
    costtal=costtal*.9
elif n>=11 and n<=20:
    costtal=costtal*.85
elif n>=21:
    costtal=costtal*.8


print("El costo a pagar es: ", round(costtal*n,2))
