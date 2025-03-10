from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Jason Drummond',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 2, 2025'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'March 3, 2025'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About Page')

if __name__ == '__main__':
    app.run(debug=True)
