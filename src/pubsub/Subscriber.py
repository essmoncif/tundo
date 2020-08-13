class Subscriber:

    def __init__(self, address: str):

        self._address = address
        self._publishers = list()

    @property
    def address(self):
        return self._address

    @property
    def follows(self):
        return self._publishers
    
    def follow(self, publisher):
        for pub in self._publishers:
            if pub.address == publisher.address:
                raise Exception("Already followed!")
        self._publishers.append(publisher)
    
    def receive(self, message: str):
        print("{}".format(message))