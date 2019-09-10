mylist = [1,2,3,4,5,6,7,8,9,10]
for item in mylist:
    if item%2 == 0:
        print("The even number is {i}".format(i=item))
    else:
        print("The odd number is {}".format(item))
