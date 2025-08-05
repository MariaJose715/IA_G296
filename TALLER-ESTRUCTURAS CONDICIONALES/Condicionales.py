#determinar si un numero es positivo o negativo
def n1():
    n1 =float(input("escribe el numero: "))
    if n1 > 0:
        print("el numero es positivo")
    if n1 == 0:
        print("el numero es cero")
    if n1 < 0:
        print("el numero es positivo")

# Determinar si un numero es par impar
def n2():
    n2=int(input("escribe el numero: "))
    if n2 % 2 == 0:
        print("numero par")
    if n2 % 2 != 0:
        print("el numero es impar")

#Determinar si un numero es divisible exactamente por 3 y 5 al mismo tiempo, por ejemplo 15 cumple, 10 no cumple porque no es divible por 3
def n3():
    n3= int(input("ingresa un numero"))
    if n3 % 3 == 0 and n3 % 5 ==0:
        print("correct")
    else:
        print("incorrec")

#Leer un caracter, determinar si es una vocal
def n4():
    n4=(input("ingresa caracter"))
    n=["a","e","i","o","u","A","E","I","O","U"] 
    if n4 in n:
        print("es vocal")
    else:
        print("no")

#Leer una letra por teclado determinar si es vocal, consonante o digito numerico ayuda a ver la tabla de ascii
def n5():
    n5=(input("ingresa caracter: "))
    n=["a","e","i","o","u","A","E","I","O","U"] 
    if n5 in n:
        print("es vocal")
    elif ord(n5) > 47 and ord(n5) < 58:
        print("es numero")
    elif ord(n5.lower()) >96 and ord(n5) <123:
        print("es consonante")
    else: 
        print("ninguna")
#Leer 3 numeros mostrarlo y deducir si se han introducido en orden creciente
def n6():

    n6.append(int (input("ingresa el primer numero" )))
    n6.append(int (input("ingresa el segundo numero" )))
    n6.append(int(input("ingresa el tercer numero" )))
    if n6[0]< n6[1]<n6[2]:
        print("estan en orden creciente")
    else:
        print ("no esta en orden")

n6()
