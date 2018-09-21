#!/usr/bin/env python3

import argparse
import glob
import os
import sys

from PIL import Image, ImageEnhance, ImageFilter

from .__init__ import __version__

__license__ = "GNU General Public License v3 or later (GPLv3+)"


def main():
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
        "-o",
        "--out-dir",
        dest="output_dir",
        help="Full path to output directory to store edited images.\
        by default they get stored in (parent director)/pillowcover-output",
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
        help="Resize img, keep ratio. provide the maximum length/width\
        value as one number. e.g pillowcase.py img -r 1920",
        type=int,
    )
    parser.add_argument(
        "-R",
        "--resize-ratio",
        dest="resize_ratio",
        help='Resize img by providing new width and length\
        e.g pillowcase.py img -R "640 480"',
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
        args.output_dir,
        args.brightness,
        args.contrast,
        args.sharpness,
        args.resize,
        args.resize_ratio,
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


def resize_img(image, max_dimension):
    size = max_dimension, max_dimension  # tuple of (max_width, max_height)
    image.thumbnail(size, Image.ANTIALIAS)


def resize_img_ratio(image, dimensions):
    width = int(dimensions.split()[0])
    height = int(dimensions.split()[1])
    resized_img = image.resize((width, height))
    return resized_img


def sharperner(input_image, output_image):
    with Image.open(input_image) as image:
        try:
            image.filter(ImageFilter.SHARPEN)
        except ValueError:
            print("Exception while trying to sharpen img")
            pass  # skip filtering for images which do not support it
        image.save(output_image)


def run(
    image_file, dir, output_dir, brightness, contrast, sharpness, resize, resize_ratio, compression
):
    if dir:
        if not os.path.isdir(dir):
            print("directory does not exist, make sure it's the full path")
            sys.exit(1)
        extensions = ("*.png", "*.jpg", "*.jpeg", "*.PNG", "*.JPG", "*.JPEG")
        # all_imgs = []
        # for extension in extensions:
        #     all_imgs.extend(glob.glob(dir + extension))   # same as following
        all_imgs = []
        [all_imgs.extend(glob.glob(dir + ext)) for ext in extensions]

        if not all_imgs:
            print("directory exists but no image was found in it")
            sys.exit(1)
    elif image_file:
        if not os.path.isfile(image_file):
            print("provided image not exist, make sure it's the full path")
            sys.exit(1)
        all_imgs = [image_file]

    for img in all_imgs:
        img_file_name = os.path.basename(img)

        # if output_dir not provided, save images in (parent)/pillowcover-output folder
        if not output_dir:
            output_dir = os.path.join(
                os.path.dirname(os.path.abspath(img)), "pillowcover-output")

        # create it if doesn't exist
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        new_name = os.path.join(output_dir, img_file_name)
        with Image.open(img) as image:
            if brightness:
                image = adjust_brightness(image, brightness)
            if contrast:
                image = adjust_contrast(image, contrast)
            if sharpness:
                image = adjust_sharpness(image, sharpness)
            if resize:
                resize_img(image, resize)
            if resize_ratio:
                image = resize_img_ratio(image, resize_ratio)

            if compression:
                image.save(new_name, quality=compression)
                print("saving image {}".format(new_name))
            else:
                image.save(new_name)
                print("saving image {}".format(new_name))
                # image.show()


if __name__ == "__main__":
    main()
