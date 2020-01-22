from flask import Flask,escape
app = Flask(__name__)
# to bind a function to a URL
@app.route('/')
def get():
    # show the message
    return 'Hello, World!'

# to bind a function to a URL
@app.route('/hello')
def getresponse():
    # show the response
    return 'Hello, Stranger!'

# to bind a function to a URL
@app.route('/hello/<name>')
def getName(name):
    # show the name for any user # keyword argument
    return 'hello %s' % escape(name)
