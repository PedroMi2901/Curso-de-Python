#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:43:41 2020

@author: pedro
"""

print ("BIENVENIDO A EMPAREJANDO.COM\n")

print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Escribe tu nombre: ")
ano = int(input("¿Año de nacimiento? "))
taburete = input("¿Te gusta Taburete? [Si/No] ")

edad = 2020-ano

print("Hola "+nombre+". Si no me equivoco tienes", edad, "años.")

if (taburete=="Si" or taburete=="Sí" or taburete=="S" or taburete=="s"):
    print("OK boomer. Lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

contador=1

while (contador<edad):
    print("Que no cumple",contador)
    contador+=1

print("¡ Que sí cumple",contador,"!")
