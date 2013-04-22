#!/usr/bin/env python
#-*- coding: utf-8 -*-

def init():
    try:
        anioActual = int(raw_input("Año Actual:"))
        for i in range(3):
            elTipo(anioActual)
    except ValueError:
        print "Debes introducir un año válido (dígitos)\nVuelve a intentar\n\n"
        init()

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