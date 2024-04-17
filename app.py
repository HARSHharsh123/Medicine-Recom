from flask import Flask , request , render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')
if __name__ == "__main__":
    app.run(debug=True)