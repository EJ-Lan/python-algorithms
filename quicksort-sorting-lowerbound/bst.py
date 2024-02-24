class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
    
def print_tree(tree, level = 0):
    if tree is not None:
        print_tree(tree.right, level + 1)
        print(' ' * 3 * level, tree.val)
        print_tree(tree.left, level + 1)

def test_bst():
    # kind of random, not very balanced
    node1 = BSTNode(1)
    node1.insert(5)
    node1.insert(3)
    node1.insert(2)
    node1.insert(8)
    print_tree(node1)
    print("\nworst case, insert elements in order")
    root = BSTNode(10)
    root.insert(9)
    root.insert(8)
    root.insert(7)
    root.insert(6)
    root.insert(5)
    root.insert(4)
    root.insert(3)
    print_tree(root)

    print("\nbest case, balanced")
    root = BSTNode(6)
    root.insert(8)
    root.insert(4)
    root.insert(5)
    root.insert(7)
    root.insert(3)
    root.insert(9)
    print_tree(root)
    print("\ndelete 5")
    root.delete(5)
    print_tree(root)
    print("\ndelete 6")
    root.delete(6)
    print_tree(root)
    
if __name__ == '__main__':
    test_bst()
