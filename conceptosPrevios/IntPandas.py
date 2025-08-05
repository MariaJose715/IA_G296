import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
#  craeacion de obejetos serie
s= pd.Series([2,4,6,8,10])
print(s)

# Creacion de un objeto Serie inicializandolo con un diccionario de python
altura={"santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura)
print(s)
"""
Creacion de un objeto series inicializandolo con algunos 
de los elementos de un diccionario de python 
"""
altura={"santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}
s=pd.Series(altura,index=["Marcelo","Luis"])
print(s)

# Creacion de un objeto Serie inicializandolo con un escalar
s=pd.Series(34,["test1","test2","test3"])
print(s)

#Acceso a los Elementos de un objeto Series
#Cada elemento de un objeto series tiene un identificador unico
s=pd.Series([2,4,6,8],index=["num1","num2","num3","num4"])
print(s)

#accediendo al tercer elemento del objeto
print(s["num3"])

#acceder por la posiscion
print(s.iloc[2])
print(s.loc["num3"])

#accediendo al segundo y tercer elementopor posicion
print(s.iloc[2:4])

#Operaciones aritmeticas con series
#sumar 
print(np.sum(s))
print(f"suma {np.sum(s)}")
print("suma", np.sum(s))

#creacion e un objeto series denominado temperaturas
temperaturas=pd.Series([4.4,5.1,6.1,6.2,6.1,6.1,5.2,4.7,4.1,3.9])
s=pd.Series(temperaturas,name="Temperatura")
print(s)
s.plot()
plt.show()

#creacion de un objeto DataFrame
personas={
    "peso":pd.Series([90,80,70,60],["Santiago","Marcelo","Luis","Alejandra"]),
    "altura":pd.Series({"Santiago":180,"Marcelo":172,"Luis":174,"Alejandra":160}),
    "hijos":pd.Series([2,3],["Luis","Marcelo"])
}
df =pd.DataFrame(personas)
print(df)
df3=pd.DataFrame(
    personas,
    columns=["altura","peso"],
    index=["Santiago","Luis","Marcelo"]
)
print(df3)
#Acceso a los elementos
print(df["peso"])
#Combinar metodos
print(df["peso"]>80)
df4=(df["peso"]>=60) & (df["peso"]>80)
print(df4)

print(df.iloc[1:3])

#Consultas avanzadas
df4=df.query("altura >=170 and peso >70")
print(df4)

#copiar un dataFrame
df_copy =df.copy()
#Añadir una nueva columna
df_copy["cumpleaños"]=[1990,1878,1780,1994]
print(df_copy)

#añadir una columna calculada
df_copy["años"]=2025 - df_copy["cumpleaños"]

#añadir una nueva columna creando un DataFrame nuevo
df_mod=df_copy.assign(mascotas=[1,3,0,0])
print(df_mod)

#eliminar una columna
del df_mod["peso"]
print(df_mod)
