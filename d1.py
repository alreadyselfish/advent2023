f1 = open("./input_data/d1.txt", "r")
data = f1.read().splitlines()
f1.close

nums = set([i for i in "0123456789"])
ret = 0
for line in data:
    first = None 
    last = None 
    for ch in line:
        if ch in nums:
            if not first:
                first = ch 
            last = ch 
    ret += int(first + last)
    # print(line, ">>", first+last)

print(ret)