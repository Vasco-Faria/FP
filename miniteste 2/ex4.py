from ast import Num
def cargoQuantity(t,m):
    q=0
    for i in t:
        if i[M]==m:
            q+=i[Q]
    return q




t=[["coal",30],["rice",50],["iron",5],["rice",42],["coal",45]]
M,Q=0,1

def unload(t,m,q):
    num=cargoQuantity(t,m)
    if q>num:
        for i in t:
            if i[M]==m:
                t.remove(i)
        return q-i[Q]
    else:
        for i in t:
            if i[M]==m:
                i[Q]-=q
                if i[Q]<= 0:
                    t.remove(i)
                    q-=i[Q]
                else:
                    break
        return cargoQuantity(t,m)



m="rice"
q=70
print(unload(t,m,q))