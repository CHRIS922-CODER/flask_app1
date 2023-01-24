from flask import Flask, render_template,request,flash


#initialize our application takes in our main module which is represented by __name__
#It creates a class for our app
app = Flask(__name__)
app.secret_key = "thisismysecretkey$$$"


@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route('/greet', methods=['POST','GET'])
def greet():
    flash("Hi "+ str(request.form['name_input']+ ", great to see you !"))
    return render_template("index.html")