players = {}
with open('men_100meter.txt', 'r', encoding='utf-8') as f:
    for line in f:
        #print (line)
        fields = line.split()
        k = fields[3] + ' ' + fields[4] 
        if k in players:
           players[k].append(fields[1])
        else:
           players[k] = [fields[1]]

#print (players)
for p in players.keys():
    print (p, '-->', players[p])
