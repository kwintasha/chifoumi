# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:06:48 2019

@author: kristnamah
"""

"""jeu pierre, papier, ciseaux l'oridnateur joue au hasard"""
from random import randint

feuille = 2
ciseaux = 3
pierre = 1

##def end(a,b):
##    randint(1,3)
##    return
def chifoumi (a,b) :  
    print("écrire pierre, papier, ciseaux :")
    def ecrire(nombre):
        if nombre == 2:
            print("pierre")
        elif nombre == 3:
            print ("feuille")
        elif nombre == 1:
            print("pierre")
        def choixordi(a,b):
            randint(1,3)
        def choixmoi (x):
            print(int("écrire pierre, papier, ciseaux :"))
        def majscore(choixordi, choixmoi):
            global scoreordi, scoremoi
            if choixordi > choixmoi == 2:
                scoremoi +1
            else:
                scoreordi +1

