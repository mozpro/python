#!/bin/python3

import random

konto = 30

while True:

        print("Du hast ", konto, "€ wie viel wilst du setztn? ")

        eingabe = int(input())

        if eingabe > konto:
                print("Du hast nicht so viel Geld.")
                continue

        zufallszahl = random.randint (0,20)

        print("Was denkst du, ist die Zahl?")

        geraten = input()

        if geraten == zufallszahl:
                konto = konto + eingabe * 5
                print ("Gewonnen. Dein Einsatz wird verfünffacht. Dein neuer Kontostand ist ", konto, "€")

        else:
                konto=konto - eingabe
                if konto==0 :
                        print ("Du bist blank. Geh betteln. Tschö mit ö!")
                        break
                else:
                        print ("Verloren. Die richtige Zahl wäre ", zufallszahl, "gewesen. Dein neuer Kontostand ist ", konto, "€")