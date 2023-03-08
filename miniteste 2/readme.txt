# 1

stocks = [('AAAA', 'March', 10, 9.5, 1), ('ITNC', 'London', 10, 9.5, 1), ('AAAA', 'London', 1200, 14556, 3)]


for c in stocks:

    ab = c[2]

    fc = c[3]

    if fc > ab:

        num = - (1 - (ab/fc))

    else:

        num = 1 - (fc/ab)

   

    # print("{:<10} {:<10} {:^10.2f} {:>10.2f} {:>10} {:<3.0}%".format(c[0], c[1], c[2], c[3], c[4], num*100))


# 2

stocks2 = sorted(stocks, key=lambda x:(x[0], -x[-1]))

for c in stocks2:

    pass

    #print("{:<10} {:<10} {:^10.2f} {:>10.2f} {:>10}".format(c[0], c[1], c[2], c[3], c[4]))




# 3

t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45], ['iron', 3]]


def cargoQuantidade(t,m):

    num = 0

    for tupl in t:

        if tupl[0] == m:

            num += tupl[1]

    return num

#print(cargoQuantidade(t,'coal'))



# 4

def merchandise(t):

    dic = {}

    for tupl in t:

        if tupl[0] in dic.keys():

            dic[tupl[0]] += tupl[1]

        else:

            dic[tupl[0]] = tupl[1]

    return dic

#print(merchandise(t))



# 5

def unload(t, m, q):

    num = cargoQuantidade(t,m)

    if num < q:

        for i in range(len(t)-1,-1,-1):

            if t[i][0] == m:

                t.pop(i)

        return q-num

    else:

        for i in range(len(t)-1,-1,-1):

            if t[i][0] == m:

                temp = t[i][1]

                t[i][1] -= q

                if t[i][1] <= 0:

                    q -= temp

                    t.pop(i)

                else:

                    break

        return cargoQuantidade(t,m)


#print(t)

#print(unload(t,'rice',40))

#print(t)

#print(unload(t,'coal',50))

#print(t)

#print(unload(t,'iron',20))

#print(t)


votes = [15300, 12000, 6600, 5100]

def hondt(votes, numseats):

    n = 0

    N = [0] * len(votes)     # [0,0,0,0]

    while n < numseats:

        votes2 = [votes[i]/(N[i]+1) for i in range(len(votes))]

        num = max(votes2)

        index = [x for x in range(len(votes2)) if votes2[x] == num]

        N[index[-1]] += 1

        n += 1

        print(votes2)

        print(N)

    return N


#print(hondt(votes, 6))