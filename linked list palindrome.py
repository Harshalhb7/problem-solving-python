# Node structure
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Function to check palindrome
def isPalindrome(head):
    values = []
    current = head

    # Store values
    while current:
        values.append(current.val)
        current = current.next

    # Compare values
    current = head
    while current:
        if current.val != values.pop():
            return False
        current = current.next

    return True


# -------- Taking Input --------
n = int(input("Enter number of nodes: "))

if n == 0:
    print("Empty list is a palindrome")
else:
    print("Enter values:")
    head = Node(int(input()))
    current = head

    for _ in range(n - 1):
        current.next = Node(int(input()))
        current = current.next

    # -------- Output --------
    if isPalindrome(head):
        print("Palindrome Linked List")
    else:
        print("Not a Palindrome Linked List")
