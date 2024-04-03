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
        list = self.head

        while list.next:
           list = list.next

        list.next = Node(data, None)

    def insert_anywhere(self, value, data):
        if value < 0 or value > self.get_length():
            raise Exception("Invalid Index")

        if value == 0:
            self.insert_at_begining(data)
            return

        total = 0
        list = self.head
        while list:
            if total == value - 1:
                node = Node(data, list.next)
                list.next = node
                break

            list = list.next
            total += 1


    def remove_anywhere(self, value):
        if value<0 or value>=self.get_length():
            raise Exception("Invalid Index")

        if value==0:
            self.head = self.head.next
            return

        total = 0
        list = self.head
        while list:
            if total == value - 1:
                list.next = list.next.next
                break

            list = list.next
            total+=1

    def insert_node_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)





 

        