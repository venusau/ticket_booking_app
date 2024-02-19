from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:vicky2003@localhost/ticket_booking'
db = SQLAlchemy(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster_url = db.Column(db.String(255), nullable=True)

class Showtimes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    showtime = db.Column(db.DateTime, nullable=False)
    tickets_available = db.Column(db.Integer, nullable=False)
    movie = db.relationship('Movies', backref='showtimes', lazy=True)

class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    showtime_id = db.Column(db.Integer, nullable=False)
    num_tickets = db.Column(db.Integer, nullable=False)
    booking_time = db.Column(db.DateTime, default=datetime.now)

@app.route('/')
def index():
    movies = Movies.query.all()
    return render_template('index.html', movies=movies)

@app.route('/book/<int:movie_id>/<int:showtime_id>', methods=['POST'])
def book_tickets(movie_id, showtime_id):
    num_tickets = request.form.get('num_tickets')
    if num_tickets.isdigit():
        num_tickets = int(num_tickets)
        showtime = Showtimes.query.get(showtime_id)
        if showtime and showtime.tickets_available >= num_tickets:
            showtime.tickets_available -= num_tickets
            db.session.commit()
            booking = Bookings(user_id=1, showtime_id=showtime_id, num_tickets=num_tickets)
            db.session.add(booking)
            db.session.commit()
            return redirect('/booking-confirmation')  # Redirect to booking confirmation page
    return "Invalid number of tickets or tickets not available."

@app.route('/tickets_options/<int:movie_id>')
def tickets_options(movie_id):
    movie = Movies.query.get(movie_id)
    if movie:
        showtimes = movie.showtimes
        return render_template('tickets_options.html', movie=movie, showtimes=showtimes)
    else:
        return "Movie not found."

@app.route('/booking-confirmation')
def booking_confirmation():
    return render_template('booking_confirmation.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
