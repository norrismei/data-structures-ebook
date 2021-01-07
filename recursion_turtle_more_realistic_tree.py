import turtle
from random import randint

# Modify the recursive tree program using one or all of the following ideas:

# Modify the thickness of the branches so that as the branch_len gets smaller, the line gets thinner.

# Modify the color of the branches so that as the branch_len gets very short it is colored like a leaf.

# Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.

# Modify the branch_len recursively so that instead of always subtracting the same amount you subtract a random amount in some range.

def rand_branch_len(branch_len):
    return branch_len - randint(0, branch_len//2)

def rand_branch_width(branch_width):
    return branch_width - branch_width//4

def tree(branch_len, branch_width, t):
    if branch_len > 5:
        if branch_len < 7:
            t.color("green")
        else:
            t.color("brown")
        t.pensize(branch_width)
        t.forward(branch_len)
        right_angle = randint(15, 40)
        t.right(right_angle)
        tree(rand_branch_len(branch_len), rand_branch_width(branch_width), t)
        left_angle = randint(20, 50)
        t.left(left_angle + right_angle)
        tree(rand_branch_len(branch_len), rand_branch_width(branch_width), t)
        t.right(left_angle)
        t.up()
        t.backward(branch_len)
        t.down()

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, 25, t)
    my_win.exitonclick()

main()
