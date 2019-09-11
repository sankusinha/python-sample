def myfunc(*args,**kargs):
    print(args)
    print(kargs)
    print("I have {} {}".format(args[0],kargs['food']))
