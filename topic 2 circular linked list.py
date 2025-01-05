class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("No active auctions.")
            return
        temp = self.head
        while True:
            print(f"Auction: {temp.data}")
            temp = temp.next
            if temp == self.head:
                break

# Example usage
auction_list = CircularLinkedList()
auction_list.add("Auction 1")
auction_list.add("Auction 2")
auction_list.display()
