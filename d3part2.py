f1 = open("./input_data/d3.txt", "r")
data = f1.read().splitlines()
f1.close

grid = []
for line in data:
    grid.append(list(line))

nRows = len(grid)
nCols = len(grid[0])
nums = set([str(i) for i in range(10)])

def is_star(r, c):
    if r<0 or c<0 or r>=nRows or c>=nCols:
        return False
    return grid[r][c] == '*' 

visited = set()
ret = []
sym_nums = {(r, c):[] for r in range(nRows) for c in range(nCols)}

def check_gears_around(r, c):
    to_check = [(r-1, c-1), (r, c-1), (r+1, c-1)]
    num_here = []
    while c < nCols and grid[r][c] in nums:
        to_check.append((r-1, c))
        to_check.append((r+1, c))
        num_here.append(grid[r][c])
        c += 1
        visited.add((r, c))
    to_check.append((r+1, c))
    to_check.append((r-1, c))
    to_check.append((r, c))
    num_here = int("".join(num_here))
    for r, c in to_check:
        if is_star(r, c):
            sym_nums[(r, c)].append(num_here) 
    

for r in range(nRows):
    for c in range(nCols):
        if grid[r][c] in nums and (r, c) not in visited:
            check_gears_around(r, c)

for r in range(nRows):
    for c in range(nCols):
        if grid[r][c] == '*' and len(sym_nums[(r, c)]) == 2:
            # print((r+1, c+1), sym_nums[(r, c)])
            p = sym_nums[(r, c)]
            ret.append(p[0]*p[1])

print(sum(ret))
            
            

