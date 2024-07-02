from flask import Flask, render_template
from read_data import read_book_data, read_book_isbns
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')
    
@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html')
    
@app.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')

@app.route('/book_club')
def book_club():
    read_book_data()
    book_array = read_book_isbns()
    return render_template('book_club.html', book_array=book_array)

@app.route('/book_club_wrapped')
def book_club_wrapped():
    read_book_data()
    book_array = read_book_isbns()
    return render_template('book_club_wrapped.html', book_array=book_array)

@app.route('/book_club_about')
def book_club_about():
    read_book_data()
    book_array = read_book_isbns()
    return render_template('book_club_about.html', book_array=book_array)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))