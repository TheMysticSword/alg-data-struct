class Node:
    def __init__(self, val, parent):
        self.left = None
        self.right = None
        self.val = val
        self.parent = parent
    
    def min(self):
        if self.left is not None:
            return self.left.min()
        return self
    
    def max(self):
        if self.right is not None:
            return self.right.max()
        return self
    
    def replace_in_parent(self, new):
        if self.parent is not None:
            if self.parent.left == self:
                self.parent.left = new
            elif self.parent.right == self:
                self.parent.right = new
            
            if new is not None:
                new.parent = self
    
    def delete_node(self):
        if (self.left is None) and (self.right is None):
            self.replace_in_parent(None)
        elif (self.left is None):
            self.replace_in_parent(self.right)
        elif (self.right is None):
            self.replace_in_parent(self.left)
        else:
            right_min = self.right.min()
            self.val = right_min.val
            right_min.delete_node()
    
    def pred(self):
        if self.left is not None:
            return self.left.min()
        else:
            n = self
            while n.parent is not None:
                if n.parent.left != n: # идём вверх, пока не придём вверх справа
                    return n.parent
                n = n.parent
            return n
    
    def succ(self):
        if self.right is not None:
            return self.right.min()
        else:
            n = self
            while n.parent is not None:
                if n.parent.right != n: # идём вверх, пока не придём вверх слева
                    return n.parent
                n = n.parent
            return n

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        if self.root is None:
            self.root = Node(x, None)
        else:
            n = self.root
            pre_none = None
            while n is not None:
                pre_none = n
                if x < n.val:
                    n = n.left
                else:
                    n = n.right
            
            new = Node(x, pre_none)
            if x < pre_none.val:
                pre_none.left = new
            else:
                pre_none.right = new
            return new

    def delete(self, x):
        if self.root is None:
            return

        n = self.root
        while n is not None:
            if x == n.val:
                break
            if x < n.val:
                n = n.left
            elif x > n.val:
                n = n.right
        
        if n is not None:
            if n == self.root:
                self.root = None
            else:
                n.delete_node()

    def lookup(self, x):
        n = self.root
        while n is not None:
            if x == n.val:
                return True
            elif x < n.val:
                n = n.left
            elif x > n.val:
                n = n.right
        return False
    
    def min(self):
        if self.root is None:
            return None
        return self.root.min()
    
    def max(self):
        if self.root is None:
            return None
        return self.root.max()

    def print_tree(self):
        stack = list()
        stack.append({'node': self.root, 'level': 0})
        while len(stack) > 0:
            cur = stack.pop()
            level = cur['level']
            node = cur['node']
            indentation = ''.join([' ' for _ in range(2*level)])
            if node is not None:
                print(indentation, node.val)
                stack.append({'node': node.right, 'level': level+1})
                stack.append({'node': node.left, 'level': level+1})
            else:
                print(indentation, 'None')
    
    def skew(self): # -
        pass

    def split(self): # -
        pass

tree = Tree()
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(4)
six = tree.insert(6)
tree.insert(5)
tree.insert(8)
tree.insert(2)
tree.insert(5)
tree.print_tree()

print()
print("Min is " + str(tree.min().val)) # 1
print("Max is " + str(tree.max().val)) # 8
print("6 successor is " + str(six.succ().val)) # 7
print("6 predecessor is " + str(six.pred().val)) # 5
print("4 exists: " + str(tree.lookup(4))) # True
print("9 exists: " + str(tree.lookup(9))) # False

print()
print("Deleting 4")
tree.delete(4)
tree.print_tree()
print("4 exists: " + str(tree.lookup(4))) # False
