# pillowcover
Easily Manipulate Images Using Python: Change Brightness, Contrast, Sharpness, Resize.
A simple script (wrapper) using pillow.

## Requirements
python >= 3.5, pillow

## Usage
To increase brightness, contrast, sharpness by 20% and resize all images (landscape, portrait)
to max dimension of 1920 pixels (using largest dimension. hight or width) and compress them to 60%
in a given folder while keeping the same aspect ratio.

``` bash
pillowcover -d /home/user/Pictures/ -b 1.20 -c 1.20 -s 1.20 -r 1920 -q 60
```

## Usage Options
``` bash
usage: pillowcover [-h] [-v] [-d DIR] [-o OUTPUT_DIR] [-b BRIGHTNESS]
                   [-c CONTRAST] [-s SHARPNESS] [-r RESIZE] [-R RESIZE_RATIO]
                   [-q COMPRESSION]
                   [image_file]

Easily Manipulate Images Using Python: Change Brightness,Contrast, Sharpness,
Resize

positional arguments:
  image_file            Full path to the image file to edit

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program\'s version number and exit
  -d DIR, --dir DIR     Path to the directory containing the image files
  -o OUTPUT_DIR, --out-dir OUTPUT_DIR
                        Path to output directory to store edited images. by
                        default they get stored in (parent
                        director)/pillowcover-output
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        Change brightness level, 1.00 is the current value
  -c CONTRAST, --contrast CONTRAST
                        Change contrast level, 1.00 is the current value
  -s SHARPNESS, --sharpness SHARPNESS
                        Change sharpness level, 1.00 is the current value
  -r RESIZE, --resize RESIZE
                        Resize img, keep ratio. provide the maximum
                        length/width value as one number. e.g pillowcase.py
                        img -r 1920
  -R RESIZE_RATIO, --resize-ratio RESIZE_RATIO
                        Resize img by providing new width and length e.g
                        pillowcase.py img -R "640 480"
  -q COMPRESSION, --compression-quality COMPRESSION
                        Compression quality 1-100, 100 means no compression at
                        all


```
