from flask import Flask, render_template, url_for ,request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message  = db.Column(db.Integer, nullable=False)

    def __repr__(self):
     return f"<Guest {self.id}{self.name} {self.email} {self.message}>" 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    guest = Guest.query.all()
    return render_template('about.html')

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        un = request.form["name"]
        em = request.form["email"]
        msg = request.form["message"]
        guest = Guest(name=un, email =em, message = msg)
        db.session.add(guest)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("form.html")


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(debug=True)