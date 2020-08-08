from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/") 
def hello(): 
    return render_template("index.html")

@app.route("/about") 
def harry(): 
    name = "Mayank Khurmai"
    return render_template("about.html", fname=name) 
    
app.run()