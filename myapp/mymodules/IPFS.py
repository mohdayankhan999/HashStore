import ipfshttpclient

def ipfs_upload(file : str):
    ipfs_client = ipfshttpclient.connect() 
    file_hash = ipfs_client.add(file)['Hash']    
    return file_hash

def ipfs_download(file_hash):
    ipfs_client = ipfshttpclient.connect() 
    file_contents = ipfs_client.cat(file_hash)
    return file_contents



