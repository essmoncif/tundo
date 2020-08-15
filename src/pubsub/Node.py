from src.blockchain_core.Blockchain import Blockchain


class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Node(metaclass=MetaClass):

    def __init__(self):

        self._publishers = list()
        self._subscribers = list()
        self._blockchain = Blockchain(2, 3)

    def add_publisher(self, publisher):

        for pub in self._publishers:
            if pub.addess == publisher.address:
                raise Exception("This publisher is already exist")
        self._publishers.append(publisher)

    def add_subscriber(self, subscriber):

        for sub in self._subscribers:
            if sub.address == subscriber.address:
                raise Exception("This subscriber is already exist")
        self._subscribers.append(subscriber)

    def broadcast(self, publisher, message):
        for sub in self._subscribers:
            for follow in sub.follows:
                if follow.address == publisher.address:
                    sub.receive("{}! from {}".format(message, publisher.address))
                    break


if __name__ == '__main__':
    node = Node()
    print(node)
    node1 =Node()
    print(node1)
