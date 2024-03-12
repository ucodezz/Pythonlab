def palindrome(val):
#     # ALTERNATE WAY
#     # return val == val[::-1]
    res = True
    s = 0
    e = len(str(val)) -1
    while(s <= e):

        if(str(val)[s] == str(val)[e]):
            s += 1
            e -= 1

    
        else:
            res = False
            break;
    
    if(res == True):
        print('pal')
    else:
        print('not pal')


# n=(input("enter any digit or string\n"))
# palindrome(n);

# n=int(input("enter a number: "))
# print(n==int(str(n)[::-1]))
        

# l1=[1,1,2,1,3,3,1,4,1]
# [l1.pop(x) for x in range(0,len(l1)) if (11[x]==1 or l1[x]==4)]
# print(l1)