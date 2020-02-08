from flask import Flask
app=Flask(__name__)

@app.route('/')
def konane():
    return ("Hello from Konane!")