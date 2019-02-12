from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def menu():
    return "Menu"

@app.route("/introduction")
def introduction():
    return "Wait! Before you leave, make sure you read this page."
 
@app.route("/signup")
def signup():
    return "Warning! This is incomplete right now, please wait."

if __name__ == "__main__":
    app.run