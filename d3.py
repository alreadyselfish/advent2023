f1 = open("./input_data/d3.txt", "r")
data = f1.read().splitlines()
f1.close

grid = []
for line in data:
    grid.append(list(line))

nRows = len(grid)
nCols = len(grid[0])
nums = set([str(i) for i in range(10)])

def check(r, c):
    if r<0 or c<0 or r>=nRows or c>=nCols:
        return False
    if grid[r][c] in nums or grid[r][c] == ".":
        return False 
    return True 

visited = set()
ret = []

def verify_and_add(r, c):
    flag = False
    flag = flag or check(r-1, c-1) or check(r, c-1) or check(r+1, c-1)
    num_here = []
    while c < nCols and grid[r][c] in nums:
        flag = flag or check(r-1, c) or check(r+1, c)
        num_here.append(grid[r][c])
        c += 1
        visited.add((r, c))
    flag = flag or check(r-1, c) or check(r, c) or check(r+1, c)
    if flag:
        ret.append(int("".join(num_here)))

for r in range(nRows):
    for c in range(nCols):
        if grid[r][c] in nums and (r, c) not in visited:
            verify_and_add(r, c)

print(sum(ret))

