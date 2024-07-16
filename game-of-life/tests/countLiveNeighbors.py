import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np

from testUtils import test
from life import countLiveNeighbors

def countLiveNeighborsTests():
    test1 = "Count Live Neighbors 1"
    init_state1 = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])
    actual1 = countLiveNeighbors(init_state1, 1, 1, 3, 3)
    expected1 = 0
    test(expected1, actual1, test1)

    test2 = "Count Live Neighbors 2"
    init_state1 = np.array([
        [1,0,0],
        [0,1,1],
        [0,0,0]
    ])
    actual1 = countLiveNeighbors(init_state1, 1, 1, 3, 3)
    expected1 = 2
    test(expected1, actual1, test2)

    test3 = "Count Live Neighbors 3"
    init_state1 = np.array([
        [1,0,0],
        [0,1,1],
        [0,0,1]
    ])
    actual1 = countLiveNeighbors(init_state1, 0, 1, 3, 3)
    expected1 = 3
    test(expected1, actual1, test3)