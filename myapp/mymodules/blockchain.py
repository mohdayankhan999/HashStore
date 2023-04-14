import datetime as date
import hashlib
import pickle

class Block :
    def __init__(self,index,transactions,previous_hash,nonce = 0) -> None:
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = date.datetime.now()
        self.nonce = nonce
        self.hash = self.calculate_hash() 
        
    def get_index(self) :
        return self.index
    
    def __str__(self) -> str:
        return str(str(self.index).encode('utf-8') + str(self.transactions).encode('utf-8') + str(self.previous_hash).encode('utf-8') )
        
    def calculate_hash(self) :
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.transactions).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.nonce).encode('utf-8'))
        return sha.hexdigest()
    
    def mine_block(self, difficulty) :
        while self.hash[:difficulty] != "0" * difficulty :
            self.nonce += 1
            self.hash = self.calculate_hash()
            
    def serialize(self):
        return pickle.dumps(self)

    @staticmethod
    def deserialize(serialized_block):
        return pickle.loads(serialized_block)
        
            



class Blockchain :
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
    
    def create_genesis_block(self) :
        return Block(0,"Genesis Block","0")
    
    def get_latest_block(self) :
        return self.chain[-1]
    
    def get_latest_index(self) :
        return self.get_latest_block().get_index()
    
    def add_block(self,new_block : Block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        
    def is_chain_valid(self):
        for i in range(1,len(self.chian)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash[:self.difficulty] != "0" * self.difficulty:
                return False
        return True
    
    def __str__(self):
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + " \n"
        return chain_str
    
    def serialize(self):
        return pickle.dumps(self)

    @staticmethod
    def deserialize(serialized_block):
        return pickle.loads(serialized_block)
    
    
#test passed
# a = Blockchain()
# a.add_block(Block(1,"d",a.get_latest_block().hash))
# a.add_block(Block(2,"c",a.get_latest_block().hash))
# print(a)