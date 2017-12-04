import math
import numpy

puzzleinput = 289326

def round_up_to_odd(f):
    f = int(numpy.ceil(f))
    return f + 1 if f % 2 == 0 else f


def round_up_to_even(f):
    f = int(numpy.ceil(f))
    return f if f % 2 == 0 else f + 1

matrixsize = round_up_to_odd(numpy.ceil(math.sqrt(puzzleinput)))

if math.sqrt(puzzleinput) == matrixsize:
    midpointcoord = matrixsize - 2
else:
    midpointcoord = round_up_to_even(numpy.ceil(math.sqrt(puzzleinput))/2)

smallermax = (matrixsize-2) * (matrixsize-2)

largermax = matrixsize * matrixsize

print("Matrix Size is {0} x {0}".format(matrixsize))
print("Matrix Midpoint coordintes are {0} x {0}".format(midpointcoord))
print("Max value of smaller assumed matrix values is {0}".format(smallermax))
print("Max value of the matrix is {0}".format(largermax))


def findcornervals(matrixhigh, matrixlow, matrixdim):
    cornervals = []
    for i, cornerval in enumerate(xrange(matrixlow + 1, matrixhigh + 2, (matrixdim-1))):
        if i == 0:
            pass
        else:
            cornervals.append(cornerval-1)
    return cornervals

cornerints = (findcornervals(largermax, smallermax, matrixsize))

print("Matrix Corner Values are {0}".format(cornerints))

print("Min moves to center is {0}".format(midpointcoord-1))

for i, cornerint in enumerate(cornerints):
    if i == 0:
        lowval = smallermax + 1
        highval = cornerints[i]
    else:
        lowval = cornerints[i-1]
        highval = cornerints[i]
    if lowval <= puzzleinput <= highval:
        print("Corner range is {0} and {1}".format(lowval,highval))
        midptval = highval - (midpointcoord - 1)
        print("The Midpoint value is {0}".format(midptval))
        if midptval == puzzleinput:
            optmoves = 0
        elif midptval > puzzleinput:
            optmoves =  midptval - puzzleinput
        else:
            optmoves = puzzleinput - midptval
        print("Calculated optional moves to be included is {0}".format(optmoves))

puzzlesolve = (midpointcoord-1) + optmoves

print("Moves to center is {0}".format(puzzlesolve))




