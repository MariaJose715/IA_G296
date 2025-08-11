import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""1.Calificación final 
La calificación final de un curso se calcula así: 30% del primer parcial, 30% del 
segundo parcial y 40% del proyecto final. 
Crea una función que calcule la nota final a partir de las tres calificaciones. 
"""
def calcularnotafinal(parcial1, parcial2, proyecto):
    nota = parcial1 * 0.3 + parcial2 * 0.3 + proyecto * 0.4
    return nota
p1 = float(input("Ingrese la nota del primer parcial: "))
p2 = float(input("Ingrese la nota del segundo parcial: "))
pf = float(input("Ingrese la nota del proyecto final: "))

final = calcularnotafinal(p1, p2, pf)
print("La nota final del curso es:", round(final, 2))

"""2.Carrera de atletismo 
Un atleta corre a una velocidad constante de 8 km/h. 
Escribe una función que indique la distancia recorrida según el tiempo en 
horas.
"""
def distancia_recorrida(tiempo_horas):
    velocidad = 8  # km/h
    return velocidad * tiempo_horas

tiempo = float(input("Ingrese el tiempo en horas: "))

distancia = distancia_recorrida(tiempo)
print("La distancia recorrida es:", distancia, "km")

"""3.Plan de celular 
Un plan de celular cuesta $15.000 mensuales e incluye 100 minutos. Cada 
minuto adicional cuesta $200. 
Escribe una función que calcule el costo total del plan según los minutos 
usados.
"""
def calcular_costo_plan(minutos_usados):
    costo_base = 15000
    minutos_incluidos = 100
    costo_extra = 200

    if minutos_usados <= minutos_incluidos:
        return costo_base
    else:
        extras = minutos_usados - minutos_incluidos
        return costo_base + extras * costo_extra

minutos = int(input("Ingrese la cantidad de minutos usados: "))

costo_total = calcular_costo_plan(minutos)
print("El costo total del plan es: $", costo_total)

"""4.Consumo de gasolina 
Un carro consume 1 galón de gasolina por cada 40 kilómetros recorridos. 
Crea una función que indique cuántos galones necesita el carro para recorrer 
cierta distancia.
"""
def calcular_galones(distancia_km):
    galon_por_km = 1 / 40  # 1 galón por cada 40 km
    return distancia_km * galon_por_km

distancia = float(input("Ingrese la distancia a recorrer en kilómetros: "))

galones = calcular_galones(distancia)
print("Se necesitan", round(galones, 2), "galones de gasolina")

"""5.Entrada al parque 
La entrada a un parque de diversiones cuesta $30.000 por persona. Si un grupo 
de personas va al parque, el total a pagar depende del número de personas. 
Escribe una función que relacione el número de personas con el costo total.
"""
def costo_entrada(numero_personas):
    precio_por_persona = 30000
    return numero_personas * precio_por_persona

personas = int(input("Ingrese el número de personas: "))

costo_total = costo_entrada(personas)
print("El costo total de entrada es: $", costo_total)


"""6.Costo de envío 
Una empresa de mensajería cobra una tarifa fija de $5.000 por envío, más 
$2.000 por cada kilogramo que pese el paquete. 
Crea una función que represente el costo total del envío según el peso del 
paquete. 
"""
def costo_entrada(numero_personas):
    precio_por_persona = 30000
    return numero_personas * precio_por_persona
def costo_envio(peso_kg):
    tarifa_base = 5000
    recargo_por_kg = 2000
    return tarifa_base + (peso_kg * recargo_por_kg)

peso = float(input("Ingrese el peso del paquete en kg: "))

costo = costo_envio(peso)
print("El costo total del envío es: $", costo)

personas = int(input("Ingrese el número de personas: "))

costo_total = costo_entrada(personas)
print("El costo total de entrada es: $", costo_total)
"""7.Costo salario por horas 
Una empresa paga a sus empleados una tarifa fija de $10.000 por hora, más un 
recargo del 100% por cada hora adicional. 
Crea una función que represente el pago total del empleado según el total de 
horas trabajadas. 
"""
def calcular_pago(horas_normales, horas_extra):
    tarifa = 10000
    return (horas_normales * tarifa) + (horas_extra * tarifa * 2)

normales = int(input("Ingrese las horas normales trabajadas: "))
extra = int(input("Ingrese las horas extra trabajadas: "))

pago = calcular_pago(normales, extra)
print("El pago total es: $", pago)

"""8.Plantear de acuerdo a su experiencia o trabajo un ejercicio de su autoría, que 
contengan funciones y resuélvalo 
"""
def puede_votar(edad):
    if edad >= 18:
        return "Puede votar"
    else:
        return "No puede votar"

edad = int(input("Ingrese su edad: "))

print(puede_votar(edad))
