#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" Un programa sencillo, para calcular cuadrados de números """
def main():
    print "Se calcularán cuadrados de números"
    n1 = input("Ingrese un número entero: ")
    n2 = input("Ingrese otro número entero: ")
    
    for x in range(n1, n2):
        print x*x
    print "Es todo por ahora"

"""Condicionamos para que se ejecute la función solo cuando
el script se ejecute directamente y no desde una importación"""
if __name__ == "__main__":
    main()