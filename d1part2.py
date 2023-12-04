f1 = open("./input_data/d1.txt", "r")
data = f1.read().splitlines()
f1.close

nums = set([i for i in "0123456789"])
keys = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
ret = 0
for line in data:
    first = None 
    last = None 
    for i in range(len(line)):
        digit = None
        for l in [3, 4, 5]:
            if line[i:min(i+l, len(line))] in keys:
                digit = str(keys[line[i:min(i+l, len(line))]])
        if line[i] in nums:
            digit = line[i]
        if digit:
            if not first:
                first = digit 
            last = digit 
    ret += int(first + last)

print(ret)