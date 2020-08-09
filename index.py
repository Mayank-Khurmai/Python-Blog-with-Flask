from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/blog"
db = SQLAlchemy(app)

class Contact(db.Model):
    '''sr_no	name	email	phone	message	'''
    sr_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(200), nullable=True)

@app.route("/") 
def home(): 
    return render_template("home.html")

@app.route("/about") 
def about(): 
    name = "Mayank Khurmai"
    return render_template("about.html", fname=name) 

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        ''' Add entry to the database'''
        ''' sr_no	name	email	phone	message	'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, email = email, phone = phone, message = message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')
    
app.run(debug=True)