from flask import render_template,request
import ipfshttpclient
import os 
import pickle
from . import create_app
from .mymodules import *

# create app
app = create_app()

        
        
@app.route('/', methods = ['GET','POST'])
def index():
    print("index")
    if request.method == 'POST' :
        file = request.files['file']
        if file :
            # client = ipfshttpclient.Client()
            # file_hash = ipfs_client.add(file) 
            # ipfs_client.pin.rm(file_hash)
            return 'file uploaded successfull!' 
        else :
            return "file upload failed"
    else :
        return render_template('index.html')
    
@app.route("/blockchain")
def blockchain():
    blockchain = Blockchain()
    if os.path.isfile("myapp/data/blockchain_data.pkl"):
        with open("myapp/data/blockchain_data.pkl", 'rb') as latest_chain:
            blockchain.chain = pickle.load(latest_chain)
    return render_template("blockchain.html",chain = blockchain.chain)

@app.route("/about")
def about():
    return render_template("about.html")