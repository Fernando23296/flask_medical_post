from flask import Flask   
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>hola</h1>"

@app.route("/about")
def about():
    return("esto es about")


if '__main__'==__name__:
    app.run(debug = True)
