from flask import Flask
app = Flask(__name__)

@app.route('/en')
def hello_world():
    return 'Hello, World!'

@app.route("/es")
def hola_mundo():
    return "<h1>hola mundo</h1>"

@app.route("/error")
def hola_omundo():
    a = "<h1>Error</h1>"
    raise Exception("Error")
    return a