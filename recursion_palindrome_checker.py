from test import testEqual

def remove_white(s):
    return s

def is_pal(s):
    return False

testEqual(is_pal(remove_white("x")), True)
testEqual(is_pal(remove_white("radar")), True)
testEqual(is_pal(remove_white("hello")), False)
testEqual(is_pal(removeWremove_whitehite("")), True)
testEqual(is_pal(remove_white("hannah")), True)
testEqual(is_pal(remove_white("madam i'm adam")), True)