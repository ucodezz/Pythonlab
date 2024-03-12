def fact(val):
    if(val == 1 or val == 0):
        return 1
    else:
        return val * fact(val-1)
    
        # ALTERNATIVE METHOD
        # return math.factorial(val)

num = int(input('enter value\n'))
print(fact(num))