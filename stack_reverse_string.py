from data_structures import Stack

def rev_string(my_string):
    """Uses stack to reverse characters in string"""
    chars = Stack()

    for char in my_string:
        chars.push(char)
    
    reversed_string = ''

    while not chars.is_empty():
        reversed_string += chars.pop()
    
    return reversed_string

print(rev_string('apple'))