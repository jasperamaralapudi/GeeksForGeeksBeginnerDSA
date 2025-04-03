# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    if x == 1:
        # Delete head node
        if head:
            new_head = head.next
            head.next = None  # Optional: break reference for garbage collection
            return new_head
        return None
    
    temp = head
    # Traverse to the node just before the target node (x-2 moves)
    for _ in range(x-2):
        if not temp:
            return head  # x is out of bounds
        temp = temp.next
    
    # Check if target node exists
    if not temp or not temp.next:
        return head
    
    # Delete the target node
    node_to_delete = temp.next
    temp.next = temp.next.next
    node_to_delete.next = None  # Optional: break reference
    
    return head



#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = self.head
        else:
            self.last.next = new_node
            self.last = new_node


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        list1 = LinkedList()
        values = list(map(int, input().strip().split()))
        for value in values:
            list1.insert(value)
        k = int(input())
        new_head = deleteNode(list1.head, k)
        print_list(new_head)
        print("~")
# } Driver Code Ends
