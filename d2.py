f1 = open("./input_data/d2.txt", "r")
data = f1.read().splitlines()
f1.close

ret = 0
for line in data:
    line = line.split(':')
    game_no = int(line[0].split()[1])
    flag = False
    for rnd in line[1].split(';'):
        nos = {'red':0, 'green':0, 'blue':0}
        for play in rnd.split(','):
            n, col = list(play.split())
            nos[col] += int(n)
            if nos['red'] > 12 or nos['green'] > 13 or nos['blue'] > 14:
                flag = True
                break 
        if flag: break
    if not flag:
        ret += game_no 


print(ret)
