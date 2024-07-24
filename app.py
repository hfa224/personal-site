from flask import Flask, render_template
app = Flask(__name__)

app.config['FREEZER_RELATIVE_URLS']= True

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/photos/')
def photos():
    return render_template('photos.html')

@app.route('/2022_10_22/')
def photos_2022_10():
    root_img_name="images/2022_10_22/0000051500"
    no_of_photos=20
    return render_template('photo_template.html', root_img_name=root_img_name, no_of_photos=no_of_photos, descriptions=[])

@app.route('/2024_04_22/')
def photos_2024_04():
    root_img_name="images/2024_04_22/0000050400"
    no_of_photos=38
    with open('static/images/2024_04_22/descriptions.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return render_template('photo_template.html', root_img_name=root_img_name, no_of_photos=no_of_photos, descriptions=lines)

@app.route('/2024_07_21/')
def photos_2024_07():
    root_img_name="images/2024_07_21/0000093500"
    no_of_photos=26
    return render_template('photo_template.html', root_img_name=root_img_name, no_of_photos=no_of_photos, descriptions=[])
    
@app.route('/cultivation/')
def cultivation():
    return render_template('cultivation.html')

@app.route('/digital_garden/')
def digital_garden():
    return render_template('digital_garden.html')

@app.route('/newsletter/')
def newsletter():
    return render_template('newsletter.html')

@app.route('/hag_chat/')
def hag_chat():
    return render_template('hag_chat.html')

@app.route('/sub_hag_chat/')
def sub_hag_chat():
    return render_template('sub_hag_chat.html')



if __name__ == '__main__':
    app.run(debug=True)