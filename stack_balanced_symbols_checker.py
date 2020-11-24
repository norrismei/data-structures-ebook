from data_structures import Stack

def is_matching_symbols(open_symbol, close_symbol):
    """Check if symbols are of the same kind"""
    
    # if open_symbol == "(":
    #     return close_symbol == ")"
    # elif open_symbol == "{":
    #     return close_symbol == "}"
    # elif open_symbol == "[":
    #     return close_symbol == "]"

    all_lefts = "([{"
    all_rights = ")]}"
    # Compare index of each symbol in its respective string
    return all_lefts.index(open_symbol) == all_rights.index(close_symbol)


def check_balanced_symbols(symbols_string):
    """Checks if opening and closing symbols in a string are balanced"""

    open_symbols = Stack()

    for symbol in symbols_string:
        if symbol in "({[":
            open_symbols.push(symbol)
        elif symbol in ")}]":
            if open_symbols.is_empty():
                return False
            open_symbol = open_symbols.pop()
            if not is_matching_symbols(open_symbol, symbol):
                return False
    
    return open_symbols.is_empty()

print(check_balanced_symbols("{ { ( [ ] [ ] ) } ( ) }")) # expected True
print(check_balanced_symbols("[ ] [ ] [ ] ( ) { }")) # expected True
print(check_balanced_symbols("( [ ) ]")) # expected False
print(check_balanced_symbols("][")) # expected False

            