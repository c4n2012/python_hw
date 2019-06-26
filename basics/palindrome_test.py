def palindrome(var):
    from collections import deque
    dq = deque(var)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            print ('False')
            return False
    print('True')
    return True

var= input('Enter a word: ')
palindrome(var)
