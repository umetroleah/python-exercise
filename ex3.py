def listOfInts(arr):
    for i in arr:
        if type(i) != int:
            return False
    return True