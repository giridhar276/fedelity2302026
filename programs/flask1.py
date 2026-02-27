


from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
@app.route("/index.html")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/east")
def east():
    return "<p>this is east direction!</p>"



@app.route("/west")
def west():
    return "<p>this is west direction!</p>"



@app.route("/north")
def north():
    return "<p>this is north direction!</p>" 


@app.route("/south")
def south():
    return "<p>this is south direction!</p>"    




app.run(debug=True,port=5432)