# from test import testEqual

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

print(reverse(''))

# testEqual(reverse("hello"), "olleh")
# testEqual(reverse("l"), "l")
# testEqual(reverse("follow"), "wollof")
# testEqual(reverse(""), "")