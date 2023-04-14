from myapp.views import app

# import Pyro4_server
# import Pyro4_client
# import IPFS


# def main():
#     cmd = 1
#     if cmd == 1 :
#         # uploading file to network
#         file = "fileName.txt"
#         ID = Pyro4_client.Client().server.add_block(file)
#     else :
#         # downloading file from network
#         client = Pyro4_client.Client()
#         blockchain = client.connect()
#         ID = "ID of file"
#         File = blockchain.download_file(ID)
#     return



if __name__ == "__main__" :
    app.run(debug=True)