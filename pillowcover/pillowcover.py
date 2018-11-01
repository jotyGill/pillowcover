#!/usr/bin/env python3

import argparse
import glob
import os
import sys

from PIL import Image, ImageEnhance, ImageFilter

from .__init__ import __license__, __version__


def main():
    parser = argparse.ArgumentParser(
        description="PillowCover: Mass Manipulate Images Using Python: Change Brightness, Contrast,"
        " Sharpness, Resize and Compress. A simple script (wrapper) using pillow."
        " Licensed Under: {}".format(__license__)
    )
    parser.add_argument("-v", "--version", action="version", version="pollowcover " + __version__)
    parser.add_argument("image_file", nargs="?", help="Full path to the image file to edit")
    parser.add_argument(
        "-d", "--dir", dest="dir", help="Path to the directory containing the image files", type=str
    )
    parser.add_argument(
        "-o",
        "--out-dir",
        dest="output_dir",
        help="Path to output directory to store edited images.\
        by default they get stored in (parent director)/pillowcover-output",
        type=str,
    )
    parser.add_argument(
        "-b",
        "--brightness",
        dest="brightness",
        help="Change brightness level, 1.00 is the current value",
        type=float,
    )
    parser.add_argument(
        "-c",
        "--contrast",
        dest="contrast",
        help="Change contrast level, 1.00 is the current value",
        type=float,
    )
    parser.add_argument(
        "-s",
        "--sharpness",
        dest="sharpness",
        help="Change sharpness level, 1.00 is the current value",
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
        "-k",
        "--crop",
        dest="crop",
        help='Crop img by providing starting point then width and length from it\
        e.g pillowcase.py img -k "0,0,640,480"',
        type=str,
    )

    parser.add_argument(
        "-q",
        "--compression-quality",
        dest="compression",
        help="Compression quality 1-100, 100 means no compression at all",
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
        args.crop,
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


def crop_img(image, dimensions):
    dimensions_list = [int(i) for i in dimensions.split(',')]
    dimensions_tuple = tuple(dimensions_list)
    cropped_img = image.crop(dimensions_tuple)
    return cropped_img


def sharperner(input_image, output_image):
    with Image.open(input_image) as image:
        try:
            image.filter(ImageFilter.SHARPEN)
        except ValueError:
            print("Exception while trying to sharpen img")
            pass  # skip filtering for images which do not support it
        image.save(output_image)


def run(
    image_file, dir, output_dir, brightness, contrast, sharpness, resize, resize_ratio, crop, compression
):
    if dir:
        if not os.path.isdir(dir):
            print("directory does not exist, make sure it's the full path")
            sys.exit(1)

        # get full path, "Downloads" will turn to "/home/user/Downloads/"
        dir_path = os.path.abspath(dir) + "/"  # glob needs "/"
        extensions = ("*.png", "*.jpg", "*.jpeg", "*.PNG", "*.JPG", "*.JPEG")
        # all_imgs = []
        # for extension in extensions:
        #     all_imgs.extend(glob.glob(dir + extension))   # same as following
        all_imgs = []
        [all_imgs.extend(glob.glob(dir_path + ext)) for ext in extensions]

        if not all_imgs:
            print("directory exists but no image was found in it")
            sys.exit(1)
    elif image_file:
        if not os.path.isfile(image_file):
            print("provided image not exist, make sure it's the full path")
            sys.exit(1)
        all_imgs = [image_file]

    for img in all_imgs:
        extension = "jpg"
        if not extension:
            extension = os.path.splitext(os.path.basename(img))[1]
        # if resizing, include resize value in img name
        if resize:
            img_file_name = "{}_{}.{}".format(
                os.path.splitext(os.path.basename(img))[0],
                str(resize),
                extension,
            )
        else:
            img_file_name = "{}.{}".format(os.path.splitext(os.path.basename(img))[0], extension)
        print(img_file_name)
        # if output_dir not provided, save images in (parent)/pillowcover-output folder
        if not output_dir:
            output_dir = os.path.join(os.path.dirname(os.path.abspath(img)), "pillowcover-output")

        # create it if doesn't exist
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        new_name = os.path.join(output_dir, img_file_name)
        with Image.open(img) as image:
            if crop:
                image = crop_img(image, crop)
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

            # converting PNG to JPG, fixes error
            if extension.lower() == "jpg" and image.mode in ("RGBA", "P"):
                image = image.convert("RGB")

            if compression:
                image.save(new_name, quality=compression)
                print("saving image {}".format(new_name))
            else:
                image.save(new_name)
                print("saving image {}".format(new_name))
                # image.show()


if __name__ == "__main__":
    main()
