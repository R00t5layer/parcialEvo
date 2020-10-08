# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:26:46 2020

@author: R00t_5layer
"""
def tercerCambio():
    print("Tercera funcionalidad!")

ab = []
agenda={"Juan":14253 , "Mariano": 24875 , "Marcos":65232}
agenda2={"Brandon":1821 , "Carlos": 2222 , "Yuriko":11111}

ab.append(agenda)
ab.append(agenda2)

with open("agendaarchivo.txt", "w") as agendaarchivo:
    print(ab,file=agendaarchivo)
