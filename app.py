from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
	app.run(debug = True)