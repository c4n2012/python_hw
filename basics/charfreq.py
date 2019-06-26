#Write a function charFreq() that takes a string and builds a frequency listing of the characters contained in it.
# Represent the frequency listing as a Python dictionary. Try it with something like charFreq("abbabcbdbabdbdbabababcbcbab")
from collections import Counter

def charfreq():
    input_string = "abbabcbdbabdbdbabababcbcbab"
    input_as_array = list(map(str,input_string))
    print (Counter(input_as_array))

charfreq()