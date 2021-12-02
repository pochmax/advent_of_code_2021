liste = open('input.txt','r').read().split('\n')
taille = len(liste)
i=1
a=1

while i< taille:
    if liste[i]>liste[i-1]:
        a=a+1
    i=i+1

print(a)
