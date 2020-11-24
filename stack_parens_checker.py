from data_structures import Stack

def parens_checker(parens_string):
    """Checks if parentheses in given string is balanced"""

    open_parens = Stack()

    for paren in parens_string:
        if paren == "(":
            open_parens.push(paren)
        else:
            if open_parens.is_empty():
                return False
            open_parens.pop()
    
    # if open_parens:
    #     return False
    # else:
    #     return True

    # The above can be simplified to a boolean check of is the stack empty

    return open_parens.is_empty()

print(parens_checker("((()))"))  # expected True
print(parens_checker("((()()))"))  # expected True
print(parens_checker("(()"))  # expected False
print(parens_checker(")("))  # expected False