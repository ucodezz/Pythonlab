# QUESTION 17 

# (A)
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


n=(input("enter any digit or string\n"))
palindrome(n);

# (B)
def sum_of_natural_numbers(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    print('the sum of ', num, ' number is : ', sum)

num = int(input('enter a number\n'))
sum_of_natural_numbers(num)