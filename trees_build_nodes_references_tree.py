class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child
    
    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child
    
    def get_root_val(self):
        return self.key
    
    def set_root_val(self, new_obj):
        self.key = new_obj
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child

# Write a function that returns a tree using nodes and references implementation that looks like:
# ['a', ['b', [], ['d', [], []]], ['c', ['e', [], []], ['f', [], []]]] (in list of lists implementation)