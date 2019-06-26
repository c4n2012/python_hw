#Write a function decToBin() that taces decimal integer and outputs its binary representation.
def dec2bin(dec_var):
    dec_var = int(dec_var)
    res = ''
    remider = 0
    while dec_var != 0:
        if dec_var % 2 != 0:
            res += '1'
        else:
            res += '0'
        dec_var = dec_var // 2
    print(res[::-1])

var = input('Your dec value: ')
dec2bin(var)