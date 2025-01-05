class BidNode:
    def __init__(self, bid_amount):
        self.bid_amount = bid_amount
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_bid(self, bid_amount):
        new_node = BidNode(bid_amount)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_bids(self):
        current = self.head
        while current:
            print(f"Bid: {current.bid_amount}")
            current = current.next

# Example usage
bids = DoublyLinkedList()
bids.add_bid(100)
bids.add_bid(150)
bids.add_bid(200)
bids.display_bids()
