f1 = open("./input_data/d2.txt", "r")
data = f1.read().splitlines()
f1.close

ret = 0
for line in data:
    line = line.split(':')
    game_no = int(line[0].split()[1])
    flag = False
    nos = {col:float("-inf") for col in ["red", "green", "blue"]}
    for rnd in line[1].split(';'):
        for play in rnd.split(','):
            n, col = list(play.split())
            nos[col] = max(nos[col], int(n))
    power = 1
    for col in nos:
        if nos[col] == float("-inf"):
            continue
        power *= nos[col]
    ret += power


print(ret)
