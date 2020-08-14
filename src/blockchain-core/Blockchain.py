from Block import Block
from Transaction import Transaction

class Blockchain:

    def __init__(self, difficulty: int, tx_capacity: int):

        self._chain = list()
        self._difficulty = difficulty
        self._pending_transactions = list()
        self._tx_capacity = tx_capacity
        #self._chain.append(self.genesis_block())
    
    def start(self):
        self.genesis_block().mine(self._difficulty)
        self._chain.append(self.genesis_block())

    def genesis_block(self):
        tx = list()
        tx.append(Transaction("toAddress", "fromAddress", "Hello, world !"))
        return Block(tx, "1ec656a82efab2f39428a13b2d4409089b20e27f452fcaa7a9cc2bf5349128c8")

    def last_block(self) :
        return self._chain[len(self._chain) - 1]
    
    def add_transaction(self, transaction):
        self._pending_transactions.append(transaction)
    
    def mining_pending_transaction(self):
        if len(self._pending_transactions) != 0:
            block = Block(self._pending_transactions[0:self._tx_capacity], self.last_block().hash_id)
            block.mine(self._difficulty)
            self._chain.append(block)
            self._pending_transactions = self._pending_transactions[self._tx_capacity:]
            if len(self._pending_transactions) != 0:
                self.mining_pending_transaction()
            
    def print_blockchain(self):
        for block in self._chain:
            print(block.dictify())


if __name__ == "__main__":
    
    blockchain = Blockchain(2, 2)
    blockchain.start()
    
    tx1 = Transaction("toAddress", "fromAddress", "Hello, world !")
    tx2 = Transaction("toAddress", "fromAddress", "Hello, world !")
    tx3 = Transaction("toAddress", "fromAddress", "Hello, world !")

    blockchain.add_transaction(tx1)
    blockchain.add_transaction(tx2)
    blockchain.add_transaction(tx3)

    blockchain.mining_pending_transaction()
    blockchain.print_blockchain()

   
