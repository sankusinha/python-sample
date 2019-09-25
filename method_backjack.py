def backjack(a,b,c):
    if 0<a<=11 and 0<b<=11 and 0<c<=11:
        total = a+b+c
        if total<21:
            return total
        elif a==11 or b==11 or c ==11:
            total = total - 10
            if total>21:
                return "BUST"
        else:
            return "BUST"
