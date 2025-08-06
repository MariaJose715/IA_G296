## 📁 Dataset: Información de Estudiantes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)

## 🧩 Actividades
#1. Crear una Serie con los nombres y alturas de los estudiantes
altura = pd.Series([162,175,168,180,170],index=["Ana","Carlos","Daniela","Eduardo","Fernanda"])
print(altura)


#Pregunta: ¿Cuál es la altura de Daniela?
#Usando loc
print(altura.loc['Daniela'])
#Usando iloc
print(altura.iloc[2])
#print(f"la altura de daniela es:{altura.loc["Daniela"]}")


#2. Accede al promedio de calificación de Carlos de 3 formas diferentes:
#Promedio de Carlos usando loc
promedio_carlos=df.loc['Carlos']['promedio']
print(f"el promedio de Carlos usando loc es {promedio_carlos}")
#Promedio de Carlos usando iloc
promedio_carlos=df.iloc[1]["promedio"]
print(f"el promedio de Carlos usando iloc es {promedio_carlos}")
#Promedio de Carlos usando query
promedio_carlos = df.query("index == 'Carlos'")["promedio"]
print(promedio_carlos)


#3. Filtra a los estudiantes con promedio mayor o igual a 4.0
estudiantes_mayor4 = df.query("promedio >= 4.0")
print(estudiantes_mayor4)
#Usando loc
estudiantes_mayor4 = df.loc[df['promedio']>=4]
print(estudiantes_mayor4)


#Pregunta: ¿Cuántos estudiantes tienen un buen promedio?
numero_estudiantes = len(estudiantes_mayor4)
print(f"Hay {numero_estudiantes} estudiantes con un buen promedio")


#4. Calcula operaciones estadísticas:
# estadisticas descriptivas
estadisticas=df.describe()
print(estadisticas)


#5. Agrega una nueva columna que indique si el estudiante es mayor de edad
df["Mayor de edad"] = df["edad"] >= 18
print("\nAñadiendo columna de mayor de edad: \n",df)


#6. Agrega una columna con el año de nacimiento (suponiendo que estamos en 2025)
df["fecha de nacimiento"] =2025 -df["edad"]
print(df[['edad','fecha de nacimiento']])


#7. Visualiza los promedios de los estudiantes en un gráfico
df["promedio"].plot(kind="bar", title="Promedio de estudiantes")
plt.xlabel("Estudiante")
plt.ylabel("Nota promedio")
plt.show()


#8. Filtra a los estudiantes con altura entre 165 y 175 cm
df=df.query("altura >= 165 and altura <= 175 ")
print()


#9. Copia el DataFrame y elimina la columna "peso"
df_copy=df.copy()
del df_copy['peso']


#10. Crea un nuevo DataFrame con solo 3 columnas: nombre, edad y año de nacimiento
df2 = pd.DataFrame(
    df,
    columns=["edad","fecha de nacimiento"],
)
print(df2)