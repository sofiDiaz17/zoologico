# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:07:58 2020

@author: Usuario
"""
animales = list()

class animal:
    def __init__(self,nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setTipo(self,tipo):
        self.tipo = tipo
        
    def getNombre(self):
        print ("The name is: "+ self.nombre)
    
    def getTipo(self):
        print ("The type is: "+ self.tipo)
        


cant=int(input("How many animals do you want to create?: "))
cont=0;
while cont < cant:
    cont=cont+1;
    animalN=input("Give me a name for animal %d: "%cont)
    animalT=input("Give me a type for animal %a: "%cont)
    anm = animal(animalN, animalT)
    animales.append(anm)
    
print("The created animales are:")
for i in animales:
    i.getNombre()
    
idA=int(input("Give me an id to change (first in list is 0): "))
print("The selected animal is: ", animales[idA].nombre) 
newType=input("Give new type: ")
animales[idA].setTipo(newType)
print("The new type is: ", animales[idA].tipo) 








