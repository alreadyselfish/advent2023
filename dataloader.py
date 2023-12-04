import os
os.environ["AOC_SESSION"] = ""

from aocd import get_data
d = get_data(day=1, year=2023)

file1 = open("./input_data/d1.txt", "a")
file1.write(d)
file1.close()
