from flask import Flask,render_template




app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/home")
def home():
    return render_template("home.html")    
@app.route("/home/contact") 
def cont():
    return "i am nithin  this is contact page"   
@app.route("/login")
def log():
    return render_template("login.html")    



if(__name__=="__main__"):
    app.run(debug="true")