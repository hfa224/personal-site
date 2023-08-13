from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)