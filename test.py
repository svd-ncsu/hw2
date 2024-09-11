import hw2_debugging
def test1():
    assert hw2_debugging.mergeSort([3,6,8,2,5,30,24,9])==[2,3,5,6,8,9,24,30]

def test2():
    assert hw2_debugging.mergeSort([43,67,8,2,5,90])==[2,5,8,43,67,90]

def test3():
    assert hw2_debugging.mergeSort([1,4,1,2,7,0,0])==[0,0,1,1,2,4,7]