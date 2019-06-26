def resolve_order():
    input_var = input('Input your brackets order in quots: ')
    brackets_stack = []
    for var in input_var:
        if var == '[':
            brackets_stack += var
        elif var == ']' and len(brackets_stack) == 0:
            print ("It's Wrong!")
        elif var == ']':
            brackets_stack.pop()
    if input_var != '' and len(brackets_stack) == 0:
        print('Yor order was correct.')
    else:
        print('Incorrect order')


resolve_order()
