"""Serves up the personal site"""

import re
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
    return produce_photo_page(
        "2025_07_03", "0000087500", range(1, 36)
    )

@app.route("/2025_02_08/")
def photos_2025_02_08():
    """Renders photo page for 2025_02_08"""
    return produce_photo_page(
        "2025_02_08", "0000087500", [ 24, 33, 34, 35, 36, 37, 38, 39]
        
    )

@app.route("/2025_06_25/")
def photos_2025_06_25():
    """Renders photo page for 2025_06_25"""
    return produce_photo_page(
        "2025_06_25", "0000052000", range(1, 39)
    )

@app.route("/2025_06_25_2/")
def photos_2025_06_25_2():
    """Renders photo page for 2025_06_25_2"""
    return produce_photo_page(
        "2025_06_25_2", "0000052300", range(1, 40)
    )

@app.route("/2025_07_22/")
def photos_2025_07_22():
    """Renders photo page for 2025_07_22"""
    return produce_photo_page(
        "2025_07_22", "0000067600", list(range(1, 29)) + [39, 40]
    )

@app.route("/2025_09_06/")
def photos_2025_09_06():
    """Renders photo page for 2025_09_06"""
    return produce_photo_page(
        "2025_09_06", "0000082800", range(1, 41)
    )

@app.route("/2026_01_01/")
def photos_2026_01_01():
    """Renders photo page for 2026_01_01"""
    return produce_photo_page(
        "2026_01_01", "0000", range(8, 37)
)

@app.route("/2026_03_09/")
def photos_2026_03_09():
    """Renders photo page for 2026_03_09"""
    return produce_photo_page(
        "2026_03_09", "0000", [1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
    )

@app.route("/2022_10_22/")
def photos_2022_10_22():
    """Renders photo page for 2022_10_22"""
    return produce_photo_page(
        "2022_10_22", "0000051500", [1, 2, 5, 7, 8, 9, 10, 11, 12, 15, 17, 18, 19, 20]
    )


@app.route("/2024_04_22/")
def photos_2024_04_22():
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
def photos_2024_07_21():
    """Renders photo page for 2024_07_21"""
    return produce_photo_page(
        "2024_07_21",
        "0000093500",
        [2, 4, 5, 6, 7, 8, 11, 12, 13, 17, 18, 20, 21, 22, 23, 24, 25, 26],
    )


@app.route("/2024_08_06/")
def photos_2024_08_06():
    """Renders photo page for 2024_08_06"""
    return produce_photo_page(
        "2024_08_06",
        "0000024500",
        [
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            11,
            12,
            13,
            14,
            15,
            16,
            18,
            19,
            20,
            22,
            24,
            25,
            26,
            27,
            28,
            29,
        ],
    )

@app.route("/2024_09_27/")
def photos_2024_09_27():
    """Renders photo page for 2024_09_27"""
    return produce_photo_page(
        "2024_09_27",
        "0000057600",
        [1, 2, 4, 5, 6, 7, 9, 10, 11, 14, 15, 16, 20, 21, 22, 23, 24, 26, 27, 28],
    )


@app.route("/2024_12_01/")
def photos_2024_12_01():
    """Renders photo page for 2024_12_01"""
    return produce_photo_page(
        "2024_12_01",
        "0000034800",
        [1, 2, 4, 5, 6, 7, 11, 13,
         14, 15, 16, 17, 18, 19,
         20, 21, 22, 23, 24, 25,
         26, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],
    )


@app.route("/spooktober/")
def spooktober():
    """Renders spooktober page"""
    return render_template("spooktober/calendar.html")

@app.route("/jjjhagdo/")
def jjhagdo():
    """Renders jjj hag do page page"""
    return render_template("jjjhagdo/index.html")


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
        photos_folder_name=photos_folder_name,
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
