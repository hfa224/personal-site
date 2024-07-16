from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/2022_10_22')
def berlin_2022():
    return render_template('2022_10_22.html')
    
@app.route('/cultivation')
def cultivation():
    return render_template('cultivation.html')


if __name__ == '__main__':
    app.run(debug=True)