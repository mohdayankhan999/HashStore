import Pyro4
import pickle

class BlockchainClient() :
    def __init__(self) -> None:
        with Pyro4.locateNS() as ns :
            self.server = Pyro4.Proxy(ns.lookup("ayankhan_blockchain_store.server"))
        self.chain = self.server.get_chain()
    def update_chain(self) :
        self.chain = self.server.get_chain()
        with open('myapp/data/blockchain_data.pkl', 'wb') as latest_chain:
            pickle.dump(self.blockchain.chain, latest_chain)
    
# test
# a = BlockchainClient()
# a.server.add_block("add a new transaction")
# print(a.chain)
# print("done")


            
    
