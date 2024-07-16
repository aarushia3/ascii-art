import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from testUtils import test
from life import cellInBounds

def cellInBoundsTests():
    test1 = "Cell in bounds 1"
    actual1 = cellInBounds(x=-1, y=0, boardRows=5, boardCols=6)
    expected1 = False
    test(expected1, actual1, test1)

    test1 = "Cell in bounds 2"
    actual1 = cellInBounds(x=7, y=0, boardRows=5, boardCols=6)
    expected1 = False
    test(expected1, actual1, test1)

    test1 = "Cell in bounds 3"
    actual1 = cellInBounds(x=7, y=0, boardRows=8, boardCols=9)
    expected1 = True
    test(expected1, actual1, test1)

    test1 = "Cell in bounds 4"
    actual1 = cellInBounds(x=7, y=0, boardRows=7, boardCols=6)
    expected1 = False
    test(expected1, actual1, test1)

    

