"""Utility methods for generating photos pages"""

from os import listdir
from os.path import isfile, join

from PIL import Image


def get_postcards():
    """get list of postcards"""
    postcard_dir = "static/film_postcards"
    onlyfiles = [
        f
        for f in listdir(postcard_dir)
        if (isfile(join(postcard_dir, f)) and "front" in f)
    ]
    print(onlyfiles)
    postcard_info_list = list(map(create_postcard_info, onlyfiles))
    for info in postcard_info_list:
        for keys,values in info.items():
            print(keys)
            print(values)

    return postcard_info_list


def create_postcard_info(filename):
    """create the postcard info dict"""
    return {
        "front_url": filename,
        "back_url": filename.replace("front", "back"),
        "orientation": get_orientation(filename)
    }


def get_orientation(img_name):
    """find out the postcard orientation"""
    im1_name = "static/film_postcards/" + img_name

    im1 = Image.open(im1_name)
    # im2 = Image.open(im2_name)
    size = im1.size

    if size[0] > size[1]:
        return "h"
    else:
        return "v"

    # print(f'im1.size={im1.size}')
    # print(f'im2.size={im2.size}')

    # for orientation in ExifTags.TAGS.keys():
    #     if ExifTags.TAGS[orientation] == 'Orientation':
    #         break

    # print(f'orientation={orientation}')

    # exif1 = dict(im1._getexif().items())
    # #exif2 = dict(im2._getexif().items())

    # # dump exif data
    # exif = im1.getexif()
    # for k, v in exif.items():
    #    print('{}: {}'.format(ExifTags.TAGS[k], v))

    # print(f'exif1 orientation={exif1[orientation]}')
    # print(f'exif2 orientation={exif2[orientation]}')
