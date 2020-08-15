from src.pubsub.Node import Node
from src.pubsub.Subscriber import Subscriber


class Publisher:

    def __init__(self, address: str):
        
        self._address = address

    @property
    def address(self):
        return self._address
    
    def send(self, node: Node, message):
        node.broadcast(self, message)



if __name__ == "__main__":
    node = Node.Node()
    sub1 = Subscriber("sub1")
    sub2 = Subscriber("sub2")
    sub3 = Subscriber("sub3")

    pub1 = Publisher("pub1")

    sub1.follow(pub1)
    sub2.follow(pub1)
    sub3.follow(pub1)

    node.add_subscriber(sub1)
    node.add_subscriber(sub2)
    node.add_subscriber(sub3)

    pub1.send(node, "Hello, world!")