import Pyro4
import pickle
import os
from . import Blockchain,Block

@Pyro4.expose
class BlockchainServer(object) :
    def __init__(self):
        self.blockchain = Blockchain()
        if os.path.isfile('myapp/data/blockchain_data.pkl'):
            with open('myapp/data/blockchain_data.pkl', 'rb') as latest_chain:
                self.blockchain.chain = pickle.load(latest_chain)
    def add_block(self, transaction):
        prev_hash = self.blockchain.get_latest_block().hash
        nonce = 0
        block = Block(len(self.blockchain.chain),transaction,prev_hash,nonce)
        self.blockchain.add_block(block)
        with open('myapp/data/blockchain_data.pkl', 'wb') as latest_chain:
            pickle.dump(self.blockchain.chain, latest_chain)
        #To brodcast this block to everyone
        #To upload File to IPFS
        return 1
    def get_chain(self) :
        return [vars(block) for block in self.blockchain.chain]
    
# # test passed
# server = BlockchainServer()
# A = server.add_block("new")
# B = server.get_chain()

# print(len(server.blockchain.chain))
# print(len(B))
# print("done")
    
    
# start server
# Pyro4.config.COMMTIMEOUT = 0.5  
# blockchain = BlockchainServer()

# daemon = Pyro4.Daemon()
# uri = daemon.register(BlockchainServer)
# with Pyro4.locateNS() as ns:
#     name = "ayankhan_blockchain_store.server"
#     ns.register(name, uri)

# print("server running with URI",uri)
# daemon.requestLoop()


