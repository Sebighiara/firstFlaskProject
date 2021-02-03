from flask import Flask, render_template, url_for
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8ee409b7667f32241bec4b83cec5e938'

posts = [
	{
		"title": "blog title 1",
		"content": "first blog content",
		"author": "x",
		"datePosted": "Monday, 1st, 2021"
	},
	{
		"title": "blog title 2",
		"content": "second blog content",
		"author": "y",
		"datePosted": "Monday, 1st, 2021"

	}
]

@app.route('/')
@app.route('/home')
def homePage():
	return render_template('home.html', posts = posts)

@app.route('/about')
def aboutPage():
	return render_template('about.html', title = 'about')

@app.route('/register')
def registerPage():
	form = RegistrationForm()
	return render_template('register.html', form = form)

if __name__ == "__main__":
	app.run(debug = True)