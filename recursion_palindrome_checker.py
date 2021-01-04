# from test import testEqual

def remove_white(s):
    return s

def is_pal(s):
    if len(s) <=1:
        return True
    else:
        if s[0] == s[-1]:
            return is_pal(s[1:-1])
        else:
            return False

print(is_pal("hannah"))

# testEqual(is_pal(remove_white("x")), True)
# testEqual(is_pal(remove_white("radar")), True)
# testEqual(is_pal(remove_white("hello")), False)
# testEqual(is_pal(removeWremove_whitehite("")), True)
# testEqual(is_pal(remove_white("hannah")), True)
# testEqual(is_pal(remove_white("madam i'm adam")), True)