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
    X=None
    y=0
    while root!=None:
            X=root.next
            if (root.next!=None and root.data>X.data):
                print(f'{root.data}', end=" ")
                sm=sm+root.data 
            if(root.next==None):
                print(" ")
                print("last node ",root.data)
                sm=sm+root.data
            root=root.next
    # Return the sum
    return sm

# Driver code


if __name__ == '__main__':

    lsN = [17, 0, 4, 1, 20, 9, -1, 23, 18, -5, 34, 35]

    print(f'original list: {lsN}')
    # add codes here to convert the list lsN to a linkedList and display it.
    # get this working first (converting the list (lsN) and display the linkedlist) before coding the sum(...)
    #l=LinkedList()
    r=arrayToLinkedList(lsN,len(lsN))
    l=LinkedList()
    l.head=r
    l.printList()
    #b=arrayToLinkedList(lsN,len(lsN))

    print('Nodes that are greater than the next node')
    s=sum(r)
    
    print("Sum of nodes greater than the next",s)

 #   print("\nsum of nodes greater than the next = ", sum(lk))