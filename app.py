from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"

#initialize the database
db = SQLAlchemy(app)

#create database model
class Friends(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(200), nullable = False) 
	dateCreated = db.Column(db.DateTime, default = datetime.utcnow)
	
	#create a function to return a string when we add something
	def __repr__(self):
		return '<name %r>' % self.id 

posts = [
	{
		"title": "Blog Post 1",
		"datePosted": "Thursday, 4 February, 2021",
		"author": "Sebi",
		"content": "1st blog content"
	},
	{
		"title": "Blog Post 2",
		"datePosted": "Thursday, 4 February, 2021",
		"author": "Mariana",
		"content": "2nd blog content"
	}

]


@app.route("/")
@app.route("/home")
def homePage():
	title = 'home page'
	return render_template('home.html', title = title)

@app.route("/about")
def aboutPage():
	title = 'about page'
	return render_template('about.html', title = title, posts = posts)

@app.route("/subscribe")
def subscribePage():
	title = 'Subscribe to my Email Newsletter'
	return render_template('subscribe.html', title = title)

@app.route("/form", methods = ["POST"])
def formPage():
	title = 'Thank you'
	firstName = request.form.get("firstName")
	lastName = request.form.get("lastName")
	email = request.form.get("email")
	if not firstName or not lastName or not email:
		statementError = "All form fields required..."
		return render_template("subscribe.html",
			statementError = statementError, 
			firstName = firstName,
			lastName = lastName,
			email = email)
	return render_template('form.html', title = title, subscribers = subscribers)

@app.route("/friends", methods = [ "GET", "POST"])
def friendsPage():
	title = "My friend list"
	if request.method == "POST":
		friendName = request.form["name"]

		#add friend
		newFriend = Friends(name = friendName)

		#push to database
		try:
			db.session.add(newFriend)
			db.session.commit()
			return redirect(url_for('friendsPage'))
		except:
			return "There was an error adding your friend"
	else:
		friends = Friends.query.order_by(Friends.dateCreated)
		return render_template('friends.html', title = title, friends = friends)

if __name__ == "__main__":
	app.run(debug = True)