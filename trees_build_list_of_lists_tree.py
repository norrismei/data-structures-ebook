# List of lists functions provided by ebook
def make_binary_tree(root):
    return [root, [], []]

def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root

def insert_right(root, new_child):
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

# Write a function that returns a tree using the list of lists functions that looks like:
# [a, [b, [], [d, [], []]], [c, [e, [], []], [f, [], []]]

def build_tree():
    main_tree = make_binary_tree("a")
    insert_left(main_tree, "b")
    insert_right(get_left_child(main_tree), "d")
    insert_right(main_tree, "c")
    c_subtree = get_right_child(main_tree)
    insert_left(c_subtree, "e")
    insert_right(c_subtree, "f")

    return main_tree

print(build_tree())