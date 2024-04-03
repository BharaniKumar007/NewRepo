class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next, prev as None


    def __str__(self):
        return f'{self.data} ->  {self.next}'

# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while temp:
            print(f'{temp.data}'" ->", end=" ")
            temp = temp.next
        print('none')
    def __str__(self):
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


def sum(root): # ------------  add code here for Q22 --

    # If there are no nodes
    if (root == None):
        return 0
    sm = 0








    # Return the sum
    return sm

# Driver code


if __name__ == '__main__':

    lsN = [17, 0, 4, 1, 20, 9, -1, 23, 18, -5, 34, 35]

    print(f'original list: {lsN}')
    # add codes here to convert the list lsN to a linkedList and display it.
    # get this working first (converting the list (lsN) and display the linkedlist) before coding the sum(...)






    print('Nodes that are greater than the next node')


 #   print("\nsum of nodes greater than the next = ", sum(lk))