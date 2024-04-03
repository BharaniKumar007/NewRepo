"""
This version is for the student

This BST_Node class has the following:
    attributes:
        data,
        left, right  (left and right are intended for another BST_Ndoe object
    functions:
        insert(self, data)
        minValueNode(self, node)
        deleteNode(self,rt, key)
        in_order_traversal(self)
        pre_order_traversal(self)
        post_order_traversal(self)
            display(self) +++++  Don't modify
            _display_aux(self) +++ Don't modify
        sum_of_all_elements_in_tree(self)
is_BST(root)
lst_to_BST(lst_elem: list)
kth_smallest(root, k)

"""

# Binary Search Tree implementation in Python

class BST_Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        if data == self.data:  # skip (return) if new data exist already in the tree
            return
        # Recursively call the insert method to add the data to the leaf
        if data < self.data:
            # Add to left subtree
            if self.left: # keep calling insert(data) until @ leaf.
                self.left.insert(data)
            else: # at leaf add the BST_Node(data)
                self.left = BST_Node(data)
        # Recursively call the insert method to add the data to the leaf
        else:
            # Add to right subtree
            if self.right:# keep calling insert(data) until @ leaf.
                self.right.insert(data)
            else:
                self.right = BST_Node(data)

# Given a non-empty binary search tree, return the node with minimum key value
#  find the mini in the predecessor and successor tree branches ).
#  Note that the entire tree does not need to be searched

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left
        return current

    def maxiValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.right is not None):
            current = current.right
        return current

#
    def deleteNode(self,rt, key):  # modify to support predecessor replacement.
        # Base Case
        if rt is None:
            return rt

        # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if key < rt.data:
            rt.left = rt.deleteNode(rt.left, key)

        # If the data to be delete
        # is greater than the root's data then it lies in right (successor) subtree

        elif (key > rt.data):
            rt.right = rt.deleteNode(rt.right, key)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:
            # Node with only one child or no child
            if rt.left is None:
                temp = rt.right
                rt = None
                return temp

            elif rt.right is None:
                temp = rt.left
                rt = None
                return temp

            # Node with two children: Get the smallest of successor (smallest in the right subtree)
            temp = rt.maxiValueNode(rt.left)
            # Copy the inorder successor's
            # content to this node
            rt.data = temp.data

            # Delete the inorder successor
            rt.left = rt.deleteNode(rt.left, temp.data)

        return rt

    # Inorder_traversal: Visit Left subtree, then Root node, then Right subtree
    def in_order_traversal(self):  # Left -> Root -> Right
        lst = []  # build the list from the traversal walk

        # Getting all data of the Left Subtree
        if self.left: # build the left
            lst += self.left.in_order_traversal()  # Recursively get all the data of the left subtree and add them into the list
        # Adding the root node to the list
        lst.append(self.data)

        # Getting all elements of the Right Subtree
        if self.right:
            lst += self.right.in_order_traversal()  # Recursively get all the elements of the right subtree and add them into the list
        return lst

    # Pre_order_traversal: Get all elements from the Root node then the left subtree and then the Right subtree
    def pre_order_traversal(self):  # Root -> Left -> Right
        data = []
        data.append(self.data)
        if self.left:
            data += self.left.pre_order_traversal()  # Recursively get all the data of the left subtree and add them into the list
        if self.right:
            data += self.right.pre_order_traversal()  # Recursively get all the data of the right subtree and add them into the list
        return data  # get the Root node element

    # Pre_order_traversal: Get all elements from the Right subtree then the left subtree and finally the Root node
    def post_order_traversal(self): # Left  -> Right -> Root
        data = []

        if self.left:
            data += self.left.post_order_traversal()  # Recursively get all the data of the left subtree and add them into the list

        if self.right:
            data += self.right.post_order_traversal()  # Recursively get all the data of the right subtree and add them into the list

        data.append(self.data)  # Get the Root node element

        return data

    def search_element(self, elem):  # complexity of O(log n)
        if self == None:

            return
        if self.data == elem:

            return True
        elif elem < self.data:
            # if yes, element would be on the left

            if self.left:
                return self.left.search_element(elem)
            else:
                return False
        else:
            # if yes, element would be on the right

            if self.right:
                return self.right.search_element(elem)
            else:
                return False

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def sum_of_all_elements_in_tree(self):
        treeLst = self.in_order_traversal()
        sum = 0
        for i in range(len(treeLst)):
            if (isinstance(i, int)):
                sum = sum + int(treeLst[i])
        
        return sum
        #return sum(self.in_order_traversal())

    def max_element_in_tree(self):
        return max(self.in_order_traversal())

    def min_element_in_tree(self):
        return min(self.in_order_traversal())

    # Tree Builder helper method

def is_BST(root):
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.data <= prev.data:
            return False
        prev = root
        root = root.right
    return True

def lst_to_BST(lst_elem: list):
    if len(lst_elem) > 1:
        # start with ls[0] as root
        root_node = BST_Node(lst_elem[0])
        for i in lst_elem[1:]: # compare to root[0] first
            root_node.insert(i) # build BST

        return root_node
    else:
        return print("Insufficient number of elements")
# the following defn uses the stack to move the "root"
def nth_smallest(root, n):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left   # for Maxi set root.right
        root = stack.pop()     #
        n -= 1
        if n == 0:
            break
        root = root.right  # for Maxi set root.left
    return root.data

def maxiValueNode(self, node):
        temp_current_node = node
        while (temp_current_node.right is not None):
            temp_current_node = temp_current_node.right
        return temp_current_node

def sum_of_all_elements_in_tree(self):
        initial_sum=0
        output_List=self.in_order_traversal()
        for every_item in List22:
            if isinstance(every_item, str):
                continue
            initial_sum=initial_sum+every_item
        return initial_sum

def deleteNode(self,right_node, value):  
        if right_node is None:
            return right_node

        if value < right_node.data:
            right_node.right = right_node.deleteNode(right_node.right, value)

        elif (value > right_node.data):
            right_node.left = right_node.deleteNode(right_node.left, value)

        else:
            if right_node.left is None:
                temp_node = right_node.right
                right_node = None
                return temp_node

            elif right_node.right is None:
                temp_node = right_node.left
                right_node = None
                return temp_node
            temp_node = right_node.minValueNode(right_node.left)
            right_node.data = temp_node.data
            right_node.left = right_node.deleteNode(right_node.left, temp_node.data)

        return right_node


if __name__ == '__main__':
    lsN = [17, 0, 4, 1, 20, 9, -1, 23, 18, -5, 34, 35]
    lsT = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
           'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen']

    ls = lsT
#a. print the given list
    print(lsN)
    print(lsT)

#b. convert an assigned list to BST
    bst_data_structure = lst_to_BST(lsN)

#c  check to see if it is a BST
    print('Is this a BST: ', is_BST(bst_data_structure))


#d  Display the BST
    bst_data_structure.display()

    nth = 5          # find the value of the 5th smallest number

# e.   print the value of the 5th smallest
    print(nth_smallest(bst_data_structure, nth))

#   print the miniValueNode and maximValneNode
# f. what is the minimum value ?
    print(bst_data_structure.min_element_in_tree())

# g. what is the maximum value?   (need to add a method is the BSTNode Class)
    print(bst_data_structure.max_element_in_tree())
    print('*'*60)

#h what is the In Order Traversal?
    print(bst_data_structure.in_order_traversal())

# i what is the Post Order Traversa?
    print(bst_data_structure.post_order_traversal())



# h what is the Pre Order Traversal?
    print(bst_data_structure.pre_order_traversal())

    print('-'*60)

#j delete the root mode and display.... what is the root node?
    bst_data_structure = bst_data_structure.deleteNode(bst_data_structure, bst_data_structure.data)
    bst_data_structure.display()


#k find the sum of all elements (for integer only)
    print(bst_data_structure.sum_of_all_elements_in_tree())

print("DONE")