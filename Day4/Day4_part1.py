import sys

def read_in():
    return {x.strip() for x in sys.stdin}

puzzleinput = read_in()

puzzlesolve = 0

for line in puzzleinput:
    tmp = line.split()
    if len(tmp) == len(set(tmp)):
        puzzlesolve = puzzlesolve + 1

print(puzzlesolve)

