from flask import Flask, render_template, url_for # this file contains the definition of the application and its views


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('templates\home.html')

@app.route('/about/')
def about():
    return render_template('templates\about.html')
if __name__ == "__main__":
    app.run(debug=True)