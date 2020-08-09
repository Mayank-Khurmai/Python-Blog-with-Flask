from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/") 
def home(): 
    return render_template("home.html")

@app.route("/about") 
def about(): 
    name = "Mayank Khurmai"
    return render_template("about.html", fname=name) 

@app.route("/contact") 
def contact(): 
    return render_template("contact.html")
    
app.run(debug=True)