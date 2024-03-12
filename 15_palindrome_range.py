start = int(input('enter the starting number'))
end = int(input('enter the ending number'))

# ALTERNATE WAY
# print([x for x in range(start, end+1) if x==int(str(x)[::-1])])

l1 = []
for i in range(start, end+1):
    res = True
    s = 0
    e = len(str(i)) -1
    while(s <= e):

        if(str(i)[s] == str(i)[e]):
            s += 1
            e -= 1

    
        else:
            res = False
            break;
    
    if(res == True):
        l1.append(i)
    else:
        continue

print(l1)
        
