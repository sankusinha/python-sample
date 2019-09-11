def myfunc(**kargs):
    print(kargs)
    if 'fruit' in kargs:
        print("My favourite fruit is {}".format(kargs['fruit']))
    else:
        print("Fruit is not there")
