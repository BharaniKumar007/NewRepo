class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data} -> {self.next}'

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(f'{temp.data}'" ->", end=" ")
            temp = temp.next
        print('none')

    def __str__(self):
        return f' {self.printList()}'

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node



    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head

        while itr.next:
           itr = itr.next

        itr.next = Node(data, None)

    def insert_at_node(self, index_value, x):
        if index_value < 0 or index_value > self.get_length():
            raise Exception("Invalid Index Value")

        if index_value == 0:
            self.insert_at_begining(x)
            return

        total = 0
        list = self.head
        while list:
            if total == index_value - 1:
                node = Node(x, list.next)
                list.next = node
                break

            itr = list.next
            total = total + 1


    def remove_at_node(self, index_value):
        if index_value < 0 or index_value >= self.get_length():
            raise Exception("Invalid Index Value")

        if index_value == 0:
            self.head = self.head.next
            return

        total = 0
        list = self.head
        while list:
            if total == index_value - 1:
                list.next = list.next.next
                break

            list = list.next
            total = total + 1

    def insert_node_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)





 

        