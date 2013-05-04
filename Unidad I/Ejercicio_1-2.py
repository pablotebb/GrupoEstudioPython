#!/usr/bin/env python
#-*- coding: utf-8 -*-

def main():
    print "Se calcularán cuadrados de números"
    n1 = input("Ingrese un número entero: ")
    n2 = input("Ingrese otro número entero: ")
    
    for x in range(n1, n2):
        print "Valor de x:",x
        print x*x
    print "Valor Final de x:",x
    print "Es todo por ahora"

if __name__ == "__main__":
    main()