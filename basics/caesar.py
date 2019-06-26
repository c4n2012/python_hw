import string

def create_cypher_dict(cypher_key):
    cypher_key = int(cypher_key)
    alphabet = string.ascii_lowercase
    alphabet_offset = alphabet[cypher_key:] + alphabet[0:cypher_key]
    return alphabet_offset

def caesar(text_str, cypher_key) :
    alphabet = string.ascii_lowercase
    alphabet_offset = create_cypher_dict(cypher_key)
    text_secured = ""
    for element in text_str:
        if element.lower() in alphabet:
            n = list(alphabet).index(element.lower())
            text_secured += alphabet_offset[n]
        else:
            text_secured += element
    print(text_secured)

key = input("Input key: ")
text_input = input("Input your text: ")
str(text_input)
caesar(text_input,key)