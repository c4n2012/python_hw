#-------------------------

def reverse(a):
    print(a[::-1])

#-------------------------



#---------------------

import time

def histogram(int_array):
    res = ""
    for var in int_array:
        for i in range(var):
            res += "*"
        time.sleep(1)
        print(res)
        res = ""

#--------------------------



#-------------------------------