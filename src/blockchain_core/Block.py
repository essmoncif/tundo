from datetime import datetime
import hashlib



class Block:

    def __init__(self, transactions: list, previousHash: str):
        self._timestamp = datetime.timestamp(datetime.now())
        self._previousHash = previousHash
        self._transactions = transactions
        self._nonce = 0
        self._hash_id = self._hash()

    @property
    def hash_id(self):
        return self._hash_id
    
    def dictify(self) -> dict:

        return {
            "timestamp": self._timestamp,
            "previousHash": self._previousHash,
            "nonce": self._nonce,
            "Tx": self._transactions
        }

    def _hash(self) -> str:
        stringify = str(self.dictify())
        id = hashlib.sha256(str.encode(stringify))
        return id.hexdigest()

    def mine(self, difficulty: int):
        while self._hash_id[:difficulty] != "0"*difficulty:
            self._nonce += 1
            self._hash_id = self._hash()
            #print("HASH :", self.hash_id, "NONCE :", self._nonce, "DICT", self.dictify())
           


if __name__ == "__main__":
    tx = ["tx1", "tx2"]
    
    block = Block(tx, "hash")
    print(block.hash_id)
    

