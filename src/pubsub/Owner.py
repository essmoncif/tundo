from src.pubsub.Publisher import Publisher
from src.pubsub.Subscriber import Subscriber


class Owner(Publisher, Subscriber):
    
    def __init__(self, public_address, private_address):
        self._public = public_address
        self._private = private_address
        Publisher.__init__(self, self._public)
        Subscriber.__init__(self, self._public)


    def send_transaction(self, transaction):
        pass


if __name__ == "__main__":
    owner = Owner("address_p", "address")