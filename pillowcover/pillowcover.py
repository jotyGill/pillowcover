#!/usr/bin/env python3

import argparse
import glob
import os
import sys

from PIL import Image, ImageEnhance, ImageFilter

# __version__ = "0.0.1"
from .__init__ import __version__

__license__ = "GNU General Public License v3 or later (GPLv3+)"


def main():
    # dir = "/home/it/Music/test"
    parser = argparse.ArgumentParser(
        description="Easily Manipulate Images Using Python: Change Brightness,"
        "Contrast, Sharpness, Resize"
    )
    parser.add_argument("-v", "--version", action="version", version="pollowcover " + __version__)
    parser.add_argument("image_file", nargs="?", help="Full path to the image file to edit")
    parser.add_argument(
        "-d",
        "--dir",
        dest="dir",
        help="Full path to the directory containing the image files",
        type=str,
    )
    parser.add_argument(
        "-b",
        "--brightness",
        dest="brightness",
        help="Change brightness level, 1.0 is the current value",
        type=float,
    )
    parser.add_argument(
        "-c",
        "--contrast",
        dest="contrast",
        help="Change contrast level, 1.0 is the current value",
        type=float,
    )
    parser.add_argument(
        "-s",
        "--sharpness",
        dest="sharpness",
        help="Change sharpness level, 1.0 is the current value",
        type=float,
    )
    parser.add_argument(
        "-r",
        "--resize",
        dest="resize",
        help='Resize img by providing new length and width\
        e.g pillowcase.py img -r "640 480"',
        type=str,
    )
    parser.add_argument(
        "-q",
        "--compression-quality",
        dest="compression",
        help="Compression quality, 100 means no compression at all",
        type=int,
    )

    args = parser.parse_args()

    run(
        args.image_file,
        args.dir,
        args.brightness,
        args.contrast,
        args.sharpness,
        args.resize,
        args.compression,
    )


def adjust_brightness(image, brightness):
    enhancer_object = ImageEnhance.Brightness(image)
    return enhancer_object.enhance(brightness)


def adjust_contrast(image, contrast):
    enhancer_object = ImageEnhance.Contrast(image)
    return enhancer_object.enhance(contrast)


def adjust_sharpness(image, sharpness):
    enhancer_object = ImageEnhance.Sharpness(image)
    return enhancer_object.enhance(sharpness)


def resize_img(image, dimensions):
    length = int(dimensions.split()[0])
    width = int(dimensions.split()[1])
    resized_img = image.resize((length, width))
    return resized_img


def sharperner(input_image, output_image):
    with Image.open(input_image) as image:
        try:
            image.filter(ImageFilter.SHARPEN)
        except ValueError:
            print("Exception while trying to sharpen img")
            pass  # skip filtering for images which do not support it
        image.save(output_image)


def run(image_file, dir, brightness, contrast, sharpness, resize, compression):
    if dir:
        # if '/' not provided at the end add it
        if dir[-1] != "/":
            dir = dir + "/"

        if not os.path.isdir(dir):
            print("directory does not exist, make sure it's the full path")
            sys.exit(1)
        extensions = ("*.png", "*.jpg", "*.jpeg", "*.PNG", "*.JPG", "*.JPEG")
        # all_imgs = []
        # for extension in extensions:
        #     all_imgs.extend(glob.glob(dir + extension))
        all_imgs = []
        [all_imgs.extend(glob.glob(dir + ext)) for ext in extensions]

        if not all_imgs:
            print("directory exists but no image was found in it")
            sys.exit(1)
        print(all_imgs)
    elif image_file:
        all_imgs = [image_file]

    for img in all_imgs:
        new_name = img[: img.rfind(".")] + "-new" + img[img.rfind(".") :]
        with Image.open(img) as image:
            # brightness = 1.2
            # contrast = 1.5
            # sharpness = 1.5
            # resize = ['640', '480']
            if brightness:
                image = adjust_brightness(image, brightness)
            if contrast:
                image = adjust_contrast(image, contrast)
            if sharpness:
                image = adjust_sharpness(image, sharpness)
            if resize:
                image = resize_img(image, resize)

            if compression:
                image.save(new_name, quality=compression)
            else:
                # image.save(new_name)
                image.show()


if __name__ == "__main__":
    main()
