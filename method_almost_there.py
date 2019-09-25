def almost_there(n):
    abs1 = abs(n-100)
    abs2 = abs(n-200)
    if abs1<=10 or abs2<=10:
        return True
    else:
        return False
