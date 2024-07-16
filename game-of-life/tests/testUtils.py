def test(expected, actual, testName):
    if (expected == actual):
        print(f"Test {testName} passed!")
    else:
        print(f"Test {testName} failed.")
        print("Expected: \n", expected)
        print("Actual: \n", actual)