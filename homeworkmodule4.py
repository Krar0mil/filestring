def palindrom(string):
    reversed_string = ''.join(reversed(string))
    if string == reversed_string:
        return print(True)
    
    else:
        return print(False)
    
palindrom('124')
