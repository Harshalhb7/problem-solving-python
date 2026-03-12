class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

key = int(input("Enter element to search: "))

current = head

while current is not None:
    if current.data == key:
        print("Element Found")
        break
    current = current.next
else:
    print("Element Not Found")
