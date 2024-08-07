"""Serves up the personal site"""

import re
from flask import Flask, render_template

app = Flask(__name__)

app.config["FREEZER_RELATIVE_URLS"] = True


@app.route("/")
def home():
    """Renders home page"""
    return render_template("home.html")


@app.route("/about/")
def about():
    """Renders about page"""
    return render_template("about.html")


@app.route("/photos/")
def photos():
    """Renders base photo page"""
    return render_template("photos.html")


@app.route("/2022_10_22/")
def photos_2022_10():
    """Renders photo page for 2022_10_22"""
    return produce_photo_page(
        "2022_10_22", "0000051500", [1, 2, 5, 7, 8, 9, 10, 11, 12, 15, 17, 18, 19, 20]
    )


@app.route("/2024_04_22/")
def photos_2024_04():
    """Renders photo page for 2024_04_22"""
    return produce_photo_page(
        "2024_04_22",
        "0000050400",
        [
            1,
            2,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
        ],
    )


@app.route("/2024_07_21/")
def photos_2024_07():
    """Renders photo page for 2024_07_21"""
    return produce_photo_page(
        "2024_07_21",
        "0000093500",
        [2, 4, 5, 6, 7, 8, 11, 12, 13, 17, 18, 20, 21, 22, 23, 24, 25, 26],
    )


@app.route("/cultivation/")
def cultivation():
    """Renders cultivation page"""
    return render_template("cultivation.html")


@app.route("/digital_garden/")
def digital_garden():
    """Renders digital garden page"""
    return render_template("digital_garden.html")


@app.route("/newsletter/")
def newsletter():
    """Renders now page TODO: under construction/hiden"""
    return render_template("newsletter.html")


@app.route("/hag_chat/")
def hag_chat():
    """Renders hag chat page TODO: under construction/hiden"""
    return render_template("hag_chat.html")


def produce_photo_page(
    photos_folder_name, photo_file_prefix, indexes_of_displayed_photos
):
    """Renders the photo template page for the photos in the given photos_folder_name"""
    root_img_name = "images/" + photos_folder_name + "/" + photo_file_prefix
    with open(
        "static/images/" + photos_folder_name + "/descriptions.txt", encoding="utf-8"
    ) as f:
        lines = [put_links_in_descriptions(line.rstrip("\n")) for line in f]
    return render_template(
        "photo_template.html",
        root_img_name=root_img_name,
        indexes_of_displayed_photos=indexes_of_displayed_photos,
        descriptions=lines,
    )


def put_links_in_descriptions(desc):
    """Finds links in the format [link text] in description and replaces with wikipedia link"""
    link_regex = re.compile(
        r"\[([\w\s,]+)\]"
    )  # match anything in the description in format [words words]
    return link_regex.sub(linkrepl, desc)


def linkrepl(matchobj):
    """replace link in [link text] format with wikipedia hyperlink to 'link_text'"""
    stripped_string = matchobj.group(0).replace("[", "").replace("]", "")
    match_string = stripped_string.replace(" ", "_")
    return (
        '<a href="https://en.wikipedia.org/wiki/'
        + match_string
        + '">'
        + stripped_string
        + "</a>"
    )


if __name__ == "__main__":
    app.run(debug=True)
