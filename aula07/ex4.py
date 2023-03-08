#hello
def Addteams():
    teams=[]
    while True:
        team=input("Equipa a adicionar ao campeonato: ")
        if team == "":
            break
        else:
            teams.append(team)
    return teams


def allmatches(teams):
    matches=[]
    for i in teams:
        for x in teams:
            if x!=i:
                matches.append((i,x))
    
    return matches


def printTable(dic):
    print("{:10} | {} | {} | {} | {} | {} | {}".format("Equipa", "Vitórias", "Empates", "Derrotas", "Golos Marcados", "Golos Sofridos", "Pontos"))
    for team in dic:
        print("{:10} | {:^8} | {:^7} | {:^8} | {:^14} | {:^14} | {:^6}".format(team, dic[team][0], dic[team][1], dic[team][2], dic[team][3], dic[team][4], dic[team][5]))


def setChampion(dic):
    champion = list(dic)[0]
    for team in dic:
        if dic[team][5] > dic[champion][5]:
            champion = team
        elif dic[team][5] == dic[champion][5] and dic[team][3] - dic[team][4] > dic[champion][3] - dic[champion][4]:
            champion = team
    return champion


teams=Addteams()
matches = allmatches(teams)
results = {}
table = {}

for team in teams:
    table[team] = [0,0,0,0,0,0]

for match in matches:
    print()
    print("Resultado do jogo", match, "?")
    x=int(input("{} : ").format(match[0]))
    y=int(input("{} : ").format(match[1]))
    results[match]=(x,y)

    table[match[0]][3] +=x
    table[match[0]][4] += y
    table[match[1]][3] += y
    table[match[1]][4] += x
    
    if x > y:
        table[match[0]][0] += 1
        table[match[0]][5] += 3
        table[match[1]][2] += 1
    elif x < y:
        table[match[1]][0] += 1
        table[match[1]][5] += 3
        table[match[0]][2] += 1
    else:
        table[match[0]][1] += 1
        table[match[0]][5] += 1
        table[match[1]][1] += 1
        table[match[1]][5] += 1


print()
printTable(table)
print()
print("A equipa vencedora é:", setChampion(table))