# Introdcuion a pandas 
Python 3.13.5
## librerias
```
import pandas as pd
```
## craeacion de objetos serie
```
# craeacion de objetos serie
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
```