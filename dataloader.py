import os
os.environ["AOC_SESSION"] = "53616c7465645f5f03c9e9c57298fb1e97b67386d72232c21a27982da4eb12369b531b69697fb662ac4d8736c4e92acf21df202883df47642281b6d4c5f70636"

from aocd import get_data
d = get_data(day=5, year=2023)

file1 = open("./input_data/d5.txt", "a")
file1.write(d)
file1.close()
