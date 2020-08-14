from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail

with open('templates/config.json', 'r') as c:
    parameter = json.load(c)["parameter"]

app = Flask(__name__) 
# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = 'test@email.com,
#     MAIL_PASSWORD=  'password'
# )
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

class Posts(db.Model):
    '''sr_no	title	tagline	  slug   content   date	'''
    sr_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    tagline = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    content= db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(20), nullable=True)
    
class Contacta(db.Model):
    '''sr_no	name	email	phone	message	'''
    sr_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(200), nullable=True)

class Postsa(db.Model):
    '''sr_no	title	tagline	  slug   content   date	'''
    sr_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    tagline = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    content= db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(20), nullable=True)

class Contactb(db.Model):
    '''sr_no	name	email	phone	message	'''
    sr_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(200), nullable=True)

class Postsb(db.Model):
    '''sr_no	title	tagline	  slug   content   date	'''
    sr_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    tagline = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    content= db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(20), nullable=True)


@app.route("/") 
def home(): 
    posts = Posts.query.filter_by().all()[0:5]
    return render_template('home.html', param=parameter, posts=posts)



@app.route("/about") 
def about(): 
    name = "Mayank Khurmai"
    return render_template("about.html", fname=name) 


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=parameter, post=post)

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



#
#
#
#
#
#
# Ending of Pyhton Script 