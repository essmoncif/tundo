import Node
import Subscriber

class Publisher:

    def __init__(self, address: str):
        
        self._address = address

    @property
    def address(self):
        return self._address
    
    def send(self, node, message):
        node.broadcast(self, message)



if __name__ == "__main__":
    