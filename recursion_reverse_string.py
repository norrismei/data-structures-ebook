from test import testEqual

def reverse(s):
    return s

testEqual(reverse("hello"), "olleh")
testEqual(reverse("l"), "l")
testEqual(reverse("follow"), "wollof")
testEqual(reverse(""), "")