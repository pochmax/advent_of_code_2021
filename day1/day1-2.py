liste = open('input.txt','r').read().split('\n')
liste2= list(map(int, liste))
taille = len(liste)
i=1
a=0
test2=0

while i< taille-2:
    test1= liste2[i]+liste2[i+1]+liste2[i+2]
    if test1>test2:
        print("increase")
        a=a+1
    elif test2==test1:
         print("no change")
    test2 = test1
    print("tour n° ",i)
    i=i+1

print("I final",i)
print(a)

    


