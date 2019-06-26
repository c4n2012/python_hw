import time

def histogram(int_array):
    res = ""
    for var in int_array:
        for i in range(var):
            res += "*"
        time.sleep(0.2)
        print(res)
        res = ""

histogram([3,4,5,2,22,32,4])