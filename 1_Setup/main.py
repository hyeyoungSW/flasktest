from flask import Flask

app = Flask(__name__)

'''
Called Decorater
What do they decorate?
Decorate the underlying functions
functions can be anything! usually index or home or default
'''
@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello world!</h1>"

