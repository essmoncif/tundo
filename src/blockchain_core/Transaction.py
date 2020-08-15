from datetime import datetime
import hashlib
import json


class Transaction:

    def __init__(self, toAddress: str, fromAddress: str, message):

        if toAddress is None or fromAddress is None:
            raise Exception("Cannot create transaction with None address")
        self._toAddress = toAddress
        self._fromAddress = fromAddress
        self._message = message
        self._timestamp = datetime.timestamp(datetime.now())

    def dictify(self) -> dict:
        
        return {"toAddress": self._toAddress, "fromAddress": self._fromAddress, "message": self._message, "timestamp": self._timestamp}

    def hash(self) -> str:
        
        stringify = json.dumps(self.dictify())
        id = hashlib.sha256(str.encode(stringify))
        return id.hexdigest()

    def signTransaction(self, signing_key):

        if signing_key == self._fromAddress:
            raise Exception("Cannot sign transaction for other wallets!")
        hashTx = self.hash()

        

if __name__ == "__main__":
    tx = Transaction("toAddress", "fromAddress", "Hello, world!")

    print("data", tx.dictify())
    print("hash", tx.hash())

