from flask import Flask
import sys,os
sys.path.append(os.path.abspath("myapp/mymodules"))

def create_app() :
    app = Flask(__name__)
    app.config.from_object('config.Config')
    return app
    

