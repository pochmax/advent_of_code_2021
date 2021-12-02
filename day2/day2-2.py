from typing import List
liste = open('./day2/input.txt','r').read().split('\n')
taille = len(liste)
i=0
horizontal = 0
depth = 0
listey = []

while i < taille:
    ligne= liste[i].split();
    mouvement = ligne[0]
    avancé = ligne[1]
    if mouvement == "forward":
        horizontal = horizontal + int(avancé)
        y = depth*int(avancé)
        listey.append(y)    
    if mouvement == "up":
        depth = depth - int(avancé)
    if mouvement == "down":
        depth = depth + int(avancé)
    i=i+1
print(horizontal*sum(listey))
