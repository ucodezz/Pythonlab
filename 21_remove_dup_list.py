l1 = [1,3,4,1,3,2,5,7,8,9,99]


#METHOD 1
# print(list(set(l1)))


# METHOD 2
i = 0
while(i < len(l1)):
    if(i == i+1):
        l1.remove(i)
    else:
        continue

print(l1)
   