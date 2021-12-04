liste = open('./day3/input.txt','r').read().split('\n')
taille = len(liste)
i=-1
compte01= 0
compte11=0
compte02= 0
compte12=0
compte03= 0
compte13=0
compte04= 0
compte14=0
compte05=0
compte15=0
compte06=0
compte16=0
compte07=0
compte17=0
compte08=0
compte18=0
compte09=0
compte19=0
compte010=0
compte110=0
compte011=0
compte111=0
compte012=0
compte112=0

gamma = []
epsilon=[]

while i < taille :
    split = list(liste[i])
    if split[0]=="0":
        compte01 = compte01+1
    elif split[0]=="1":
        compte11 = compte11+1

    if split[1]=="0":
        compte02 = compte02+1
    elif split[1]=="1":
        compte12= compte12+1
    
    if split[2]=="0":
        compte03 = compte03+1
    elif split[2]=="1":
        compte13 = compte13+1
    
    if split[3]=="0":
        compte04 = compte04+1
    elif split[3]=="1":
        compte14 = compte14+1
    
    if split[4]=="0":
        compte05 = compte05+1
    elif split[4]=="1":
        compte15 = compte15+1

    if split[5]=="0":
        compte06 = compte06+1
    elif split[5]=="1":
        compte16 = compte16+1

    if split[6]=="0":
        compte07 = compte07+1
    elif split[6]=="1":
        compte17 = compte17+1

    if split[7]=="0":
        compte08 = compte08+1
    elif split[7]=="1":
        compte18 = compte18+1
    
    if split[8]=="0":
        compte09 = compte09+1
    elif split[8]=="1":
        compte19 = compte19+1

    if split[9]=="0":
        compte010 = compte010+1
    elif split[9]=="1":
        compte110 = compte110+1

    if split[10]=="0":
        compte011 = compte011+1
    elif split[10]=="1":
        compte111 = compte111+1

    if split[11]=="0":
        compte012 = compte012+1
    elif split[11]=="1":
        compte112 = compte112+1
    i= i+1


if compte01>compte11:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte02>compte12:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte03>compte13:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte04>compte14:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte05>compte15:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte06>compte16:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte07>compte17:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte08>compte18:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte09>compte19:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte010>compte110:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte011>compte111:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

if compte012>compte112:
    gamma.append("0")
    epsilon.append("1")
else:
    gamma.append("1")
    epsilon.append("0")

print(list(map(int,gamma)))
print(list(map(int,epsilon)))
gammanumber= int("".join(gamma),2)
epsilonnumber= int("".join(epsilon),2)
print(gammanumber*epsilonnumber)