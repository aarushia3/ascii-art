import numpy as np

def test(expected, actual, testName):
    if isinstance(expected, np.ndarray) and isinstance(actual, np.ndarray):
        # Compare numpy arrays
        if np.array_equal(expected, actual):
            print(f"Test {testName} passed!")
        else:
            print(f"Test {testName} failed.")
            print("Expected:\n", expected)
            print("Actual:\n", actual)
    else:
        # Compare other types
        if expected == actual:
            print(f"Test {testName} passed!")
        else:
            print(f"Test {testName} failed.")
            print("Expected:\n", expected)
            print("Actual:\n", actual)