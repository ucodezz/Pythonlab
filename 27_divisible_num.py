l1=[234,5,7,4,65]
l2=[]

n=int(input('enter any number '))
for i in l1 :
    if i%n==0:
        l2.append(i)
print(l2)

