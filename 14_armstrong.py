def armstrong(val):
    dup = val
    length = len(str(val))
    sum = 0
    
    if(length == 1):
        print(val,' is a armstrong number')
        return

    while(val != 0):
        res = val % 10
        sum += res**length
        val = int(val/10)
 

    if(sum == dup):
        print(dup, ' is a armstrong number')
    else:
        print(dup, ' is not a armstrong number')


a = int(input('enter a number\n'))
armstrong(a)

