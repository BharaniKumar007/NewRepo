from main import LinkedList

print("HW4-a------------------create and display the three separate nodes ")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1'])
linked_list1.printList()
linked_list2 = LinkedList()
linked_list2.insert_node_values(['2'])
linked_list2.printList()
linked_list3 = LinkedList()
linked_list3.insert_node_values(['3'])
linked_list3.printList()

print("HW4-a----------------the linkedlist of the above nodes")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '2' , '3'])
linked_list1.printList()



print("HW4-b--------add node(9) to after the head of the current linkedList ")
linked_list2 = LinkedList()
linked_list2.insert_node_values(['1'])
linked_list2.insert_at_end(9)
linked_list2.printList()

print("HW4-c---------insert node(9) between node(1) and node(2)")
linked_list1.printList()
linked_list1.insert_node_values(1,9)
linked_list1.printList()

print("HW4-d------before replace node(7) and (8) with node(5)")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['7' , '8' , '3'])
linked_list1.printList()

print("HW4-d------after--the replacement ")
linked_list1.remove_at_node(1)
linked_list1.remove_at_node(0)
linked_list1.insert_at_begining(5)
linked_list1.printList()

print("HW4-e------before adding node(3) to the end of the list ")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '2'])
linked_list1.printList()

print("HW4-e------after adding ")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '2'])
linked_list1.insert_at_end(3)
linked_list1.printList()

print("HW4-f-------before adding node(3) to the start of the list")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '2'])
linked_list1.printList()

print("HW4-f-------after adding node(3)")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '2'])
linked_list1.insert_at_begining(3)
linked_list1.printList()


print("HW4-g------------before combining two linkedLists")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '2'])
print('list one = ',end='',)
linked_list1.printList()
linked_list2 = LinkedList()
linked_list2.insert_node_values(['3' , '4'])
print('list two = ',end='')
linked_list2.printList()
linked_list2.insert_at_end([linked_list2])
linked_list2.printList()



print("HW4-g--------after combining the lists is ")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '3','4','2'])
linked_list1.printList()

print("HW4-h-------before split one linkedlists into two")
linked_list1 = LinkedList()
linked_list1.insert_node_values(['1' , '2','3'])
linked_list1.printList()


print("HW4-h------after split one linkedLists into two")
linked_list1 = LinkedList()
linked_list1.insert_node_values([ '2'])
print('list one = ',end='',)
linked_list1.printList()
linked_list2 = LinkedList()
linked_list2.insert_node_values(['1' , '3'])
print('list two = ',end='')
linked_list2.printList()



