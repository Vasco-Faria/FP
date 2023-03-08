from util import *


def printStocks(stocks):
    for c in stocks:
        pa=c[2]
        pf=c[3]
        if pa>pf:
            num=-(1-pa/pf)
        else:
            num=(1-(pf/pa))

    return num

print("{:<10} {:<10} {:^10.2f})

