from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail

with open('templates/config.json', 'r') as c:
    parameter = json.load(c)["parameter"]

app = Flask(__name__) 
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'test@email.com,
    MAIL_PASSWORD=  'password'
)
mail = Mail(app)
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
    return render_template("home.html", param=parameter)

@app.route("/about") 
def about(): 
    name = "Mayank Khurmai"
    return render_template("about.html", fname=name) 

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        ''' Adding entry to the database'''
        ''' sr_no	name	email	phone	message	'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, email = email, phone = phone, message = message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = "mayankkhurmai8@gmail.com",
                          body = message + "\n" + phone
                          )
    return render_template('contact.html')
    
    
app.run(debug=True)
