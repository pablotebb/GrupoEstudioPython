#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Definimos una funcion inicial, el nombre es lo de menos
def init():
    """El except sirven para capturar errores que surjan
       al momento de ejecutar las operaciones que estan dentro
       del try
    """
    try:
        #Solicitamos el año actual y lo convertimos a entero
        anioActual = int(raw_input("Año Actual:"))
        
        for i in range(3):
            #llamamos la funcion elTipo y le pasamos como parametro anioActual
            elTipo(anioActual)
            
    #El except capturara los errores de tipo ValueError esto es si en dado caso
    #al convertir (linea 12) la entrada no sean numeros (que hayan introducido
    #alguna letra u otro caracter)"""
    except ValueError:
        #Le enviamos un mensaje al usuario
        print "Debes introducir un año válido (dígitos)\nVuelve a intentar\n\n"
        #volvemos a llamar la función init
        init()

"""La función elTipo lleva el mismo patrón de procedimiento que la 
   función init (refirendo al try,except)
"""
def elTipo(anioActual):
    try:
        nom = raw_input("Nombre:")
        anioNac = int(raw_input("Año de Nacimiento:"))
        edad = anioActual - anioNac
        print "%s en este año cumpliras %d\n" % (nom, edad)
    except ValueError:
        print "Debes introducir un año válido (dígitos)\nVuelve a intentar\n\n"
        elTipo(anioActual)

init()