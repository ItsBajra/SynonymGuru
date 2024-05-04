from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutus/')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus/')
def contactus():
    return render_template('contactus.html')

@app.route('/social/')
def socials():
    return render_template('socials.html')

if __name__ == '__main__':
    app.run(debug = True)