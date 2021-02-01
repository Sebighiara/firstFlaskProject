from flask import Flask, render_template, url_for

app = Flask(__name__)

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
	return render_template('index.html', posts = posts)

@app.route('/about')
def aboutPage():
	return render_template('about.html', title = 'about')

if __name__ == "__main__":
	app.run(debug = True)