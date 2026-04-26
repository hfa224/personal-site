"""Serves up the personal site"""

import re
import os
from flask import Flask, render_template

app = Flask(__name__)

app.config["FREEZER_RELATIVE_URLS"] = True


@app.route("/")
def landing_page():
    """Renders landing page"""
    return render_template("landing-page.html")


@app.route("/about/")
def landing_page_about():
    """Renders about page"""
    return render_template("landing-page-about.html")


@app.route("/changelog/")
def landing_page_changelog():
    """Renders changelog page"""
    return render_template("changelog.html")


@app.route("/colophon/")
def landing_page_colophon():
    """Renders colophon page"""
    return render_template("colophon.html")


@app.route("/sheets/")
def sheets():
    """Renders sheets page"""
    return render_template("sheets/book_log.html")


@app.route("/photos/")
def photos():
    """Renders base photo page"""
    return render_template("photos.html")


@app.route("/counters/")
def counters():
    """Renders counters page"""
    return render_template("archive/counters.html")

@app.route("/2025_07_03/")
def photos_2025_07_03():
    """Renders photo page for 2025_07_03"""
    return produce_photo_page("2025_07_03")


@app.route("/2025_02_08/")
def photos_2025_02_08():
    """Renders photo page for 2025_02_08"""
    return produce_photo_page("2025_02_08")


@app.route("/2025_06_25/")
def photos_2025_06_25():
    """Renders photo page for 2025_06_25"""
    return produce_photo_page("2025_06_25")


@app.route("/2025_06_25_2/")
def photos_2025_06_25_2():
    """Renders photo page for 2025_06_25_2"""
    return produce_photo_page("2025_06_25_2")


@app.route("/2025_07_22/")
def photos_2025_07_22():
    """Renders photo page for 2025_07_22"""
    return produce_photo_page("2025_07_22")


@app.route("/2025_09_06/")
def photos_2025_09_06():
    """Renders photo page for 2025_09_06"""
    return produce_photo_page("2025_09_06")


@app.route("/2026_01_01/")
def photos_2026_01_01():
    """Renders photo page for 2026_01_01"""
    return produce_photo_page("2026_01_01")


@app.route("/2026_03_09/")
def photos_2026_03_09():
    """Renders photo page for 2026_03_09"""
    return produce_photo_page("2026_03_09")


@app.route("/2022_10_22/")
def photos_2022_10_22():
    """Renders photo page for 2022_10_22"""
    return produce_photo_page("2022_10_22")


@app.route("/2024_04_22/")
def photos_2024_04_22():
    """Renders photo page for 2024_04_22"""
    return produce_photo_page("2024_04_22")


@app.route("/2024_07_21/")
def photos_2024_07_21():
    """Renders photo page for 2024_07_21"""
    return produce_photo_page("2024_07_21")


@app.route("/2024_08_06/")
def photos_2024_08_06():
    """Renders photo page for 2024_08_06"""
    return produce_photo_page("2024_08_06")


@app.route("/2024_09_27/")
def photos_2024_09_27():
    """Renders photo page for 2024_09_27"""
    return produce_photo_page("2024_09_27")


@app.route("/2024_12_01/")
def photos_2024_12_01():
    """Renders photo page for 2024_12_01"""
    return produce_photo_page("2024_12_01")


def produce_photo_page(photos_folder_name):
    """Renders the photo template page for the photos in the given photos_folder_name"""
    photo_folder_name = "images/" + photos_folder_name
    image_list = []
    for file in os.listdir(os.path.join("static", photo_folder_name)):
        if "txt" not in file:
            image_list.append(photo_folder_name + "/" + file)
    # sort list
    image_list.sort()
    with open(
        "static/images/" + photos_folder_name + "/descriptions.txt", encoding="utf-8"
    ) as f:
        lines = [put_links_in_descriptions(line.rstrip("\n")) for line in f]
    return render_template(
        "photo_template.html",
        photos_folder_name=photos_folder_name,
        image_list=image_list,
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
