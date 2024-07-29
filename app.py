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
    return produce_photo_page('2022_10_22', '0000051500', [1, 2, 5, 7, 8, 9, 10, 11, 12, 15, 17, 18, 19, 20])

@app.route('/2024_04_22/')
def photos_2024_04():
    return produce_photo_page('2024_04_22', '0000050400', [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])

@app.route('/2024_07_21/')
def photos_2024_07():
    return produce_photo_page('2024_07_21', '0000093500', [2, 4, 5, 6, 7, 8, 11, 12, 13, 17, 18, 20, 21, 22, 23, 24, 25, 26])
    
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

def produce_photo_page(photos_folder_name, photo_file_prefix, indexes_of_displayed_photos):
    root_img_name='images/' + photos_folder_name + '/' + photo_file_prefix
    with open('static/images/' + photos_folder_name + '/descriptions.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return render_template('photo_template.html', root_img_name=root_img_name, indexes_of_displayed_photos=indexes_of_displayed_photos, descriptions=lines)
    


if __name__ == '__main__':
    app.run(debug=True)