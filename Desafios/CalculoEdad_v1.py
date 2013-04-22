#!/usr/bin/env python
#-*- coding: utf-8 -*-

anioActual = raw_input("Año Actual:")
if anioActual.isdigit():
    anioActual = int(anioActual)
    for i in range(3):
        nom = raw_input("Nombre:")
        anioNac = raw_input("Año de Nacimiento:")
        if anioNac.isdigit():
            edad =  anioActual - int(anioNac)
            print "%s en este año cumpliras %d\n" % (nom, edad)
        else:
            print "Debes introducir un año válido (dígitos)"
else:
    print "Debes introducir un año válido (dígitos)"