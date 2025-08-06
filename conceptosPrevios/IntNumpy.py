import numpy as np
import matplotlib.pyplot as plt
#Matriz de 2 x 4 de (0)
a=np.zeros((2,4))
print(a)

#Matriz de 2 x 4 de (1)
b=np.ones((2,4))
print(b)

#Imprimir las dimensiones de la matriz
print ("Dimensiones: ", a.shape)

#Imprimir las dimensiones de la matriz
print ("Dimensiones: ", a.ndim)

#Imprimir el tamaño de la matriz
print ("tamaño: ", a.size)

#Array o matriz cuyos valores son todos el valor indicado como segundo parametro
c=np.full((2,3,4),8)
print (c)

#Inicializa los valores del array con lo que haya en memoria en el momento
#el llenado del empty es aleatorio
d=np.empty((2,3,9))
print(d)

d=np.array([[1,2,3],[4,5,6]])
print (d)
print("tamaño",d.shape)
print("tamaño",d.size)

#creacion del array utilizando una funcion basada en rangos
#()
print(np.linspace(0,6,10))

#inicializacion del array con valores aleatorios
e=np.random.rand(2,3,4)
print(e)

#inicializacion del array con valores aleatorios conforme a una distribucion normal
f=np.random.rand(2,4)
print(f)

#Histograma con valores aleatorios
"""
g=np.random.rand(500)
plt.hist(g,bins=100)
plt.show()
#print(g)

#Histograma con valores personalizados
h=np.array([1,2,2,2,3,3,4,5,6,7,8])
plt.hist(h,bins=20) #(numero d barras)
plt.show()
"""
# #inicializacion del array/matriz usando una funcion 
def func(x,y):
    #print(x)
    #print(x+2*y)
    return x+2*y
i=np.fromfunction(func,(3,5))
print(i)

#Acceso a los elementos de un array 
#Array unidimensional
array_uni=np.array([1,3,5,7,9,11])
print("Shape: ", array_uni.shape)
print("array_uni: ",array_uni)
#accediendo al quinto elemento
print(array_uni[4])
#accediendo a los elementos 0,3 y 5 del array
print(array_uni[0::3])

#array multidiemensional
array_mult=np.array([[1,2,3,4],[5,6,7,8]])
print("Shape: ", array_mult.shape)
print("array_uni: ",array_mult)

#accediendo al cuarto elemnto del array multi
array_mult[0,3]

#accediendo a los datos de la segunda fila
print(array_mult[1,:])

#accediendo al tercer elemento de las dos primeras filas del array
print(array_mult[0:2,2]) 

#Modificacion de un array/matriz
#Crear un array unidimensional inicializando un rango de elementos del 0 al 27
array1=np.arange(27)
print("shape: ",array1.shape)
print("array 1:\n",array1) 

#cambiar las dimensiones del array y sus longitudes
array2=array1.shape=(6,4)
print("shape: ",array2.shape)
print("array 2:\n",array2)


