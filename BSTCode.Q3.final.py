    # Function to initialise the node object
def init(self, data):
    self.data = data  # Assign data
    self.next = None  # Initialize next, prev as None

def str(self):
    return f'{self.data} ->  {self.next}'


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def init(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while temp:
            print(f'{temp.data}'" ->", end=" ")
            temp = temp.next
        print('none')

    def str(self):
        return f' {self.printList()}'


def insert(root, item):
    temp = Node(0)
    temp.data = item
    temp.next = root
    root = temp
    return root  # root as Node type


def arrayToLinkedList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])
    return root


def sum(root):  # ------------  add code here for Q22 --
    higher_nodes = []
    last = root.data
    # If there are no nodes
    if (root == None):
        return 0
    sm = 0
    temporary_node = root
    while temporary_node.next != None:
        if temporary_node.data > temporary_node.next.data:
            higher_nodes.append(temporary_node.data)
            sm = sm + temporary_node.data
        temporary_node = temporary_node.next
        node_data = temporary_node.data

    if temporary_node.data > root.data:
        sm += temporary_node.data

    # Return the sum
    return sm, higher_nodes, node_data


# Driver code


if __name__ == 'main':

    lsN = [17, 0, 4, 1, 20, 9, -1, 23, 18, -5, 34, 35]

    print(f'original list: {lsN}')

    # add codes here to convert the list lsN to a linkedList and display it.
    # get this working first (converting the list (lsN) and display the linkedlist) before coding the sum(...)
    value = len(lsN)
    root = arrayToLinkedList(lsN, value)
    print(f'linked_list: {root}')

    p, q, r = sum(root)
    print('Nodes that are greater than the next node')
    for i in b:
        print(i, end=" ")
    print()
    print('last node', c)
    print('Sum of nodes greater than the next =', a)

#   print("\nsum of nodes greater than the next = ", sum(lk))