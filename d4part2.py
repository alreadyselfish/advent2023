f1 = open("./input_data/d4.txt", "r")
data = f1.read().splitlines()
f1.close

wins = []
numbs = []

for line in data:
    line = line.split(':')[1].split('|')
    wins.append(line[0])
    numbs.append(line[1])

copies = {idx:1 for idx in range(len(wins))}

for idx in range(len(wins)):
    won = set(map(int, wins[idx].split()))
    nums = list(map(int, numbs[idx].split()))
    cnt = 0
    for n in nums:
        if n in won:
            cnt += 1
    if cnt == 0:
        continue
    for nex in range(idx+1, min(len(wins), idx+cnt+1)):
        copies[nex] += copies[idx] 

print(sum(copies.values()))    