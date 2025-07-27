"""Utility methods for generating photos pages"""

import re


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
