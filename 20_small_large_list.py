# l1 = [12,2,33,41,5]
l1 = []
while(True):
    a = int(input('enter number'))
    if a<0:
        break
    else:
        l1.append(a);
print(l1)
large = small = l1[0]

#METHOD 1
for i in l1:
    if i < small:
        small = i
    elif i> large:
        large = i
print(large, small)



# METHOD 2 
# giving also second largest and second smallest
# l1 = [12,2,33,41,5]
# large = small = l1[0]
# smallest = [x for x in l1 if x<small]
# largest = [x for x in l1 if x>large]
# print(smallest, largest)

# METHOD 3
# large = max([x for x in l1])
# small = min([x for x in l1])
# print(large, small)
        

