# pillowcover
Mass Manipulate Images Using Python: Change Brightness, Contrast, Sharpness, Resize, Compress, Crop and Convert (e.g png to jpg).
A simple script (wrapper) using pillow.
Licensed Under: GNU General Public License v3 or later (GPLv3+)

## Requirements
python >= 3.5, pillow

## Usage
To increase brightness, contrast, sharpness by 20% and resize all images (landscape, portrait)
to max dimension of 1920 pixels (using largest dimension. hight or width) and compress them to 60%
in a given folder while keeping the same aspect ratio.

``` bash
pillowcover -d /home/user/Pictures/ -b 1.20 -c 1.20 -s 1.20 -r 1920 -q 60
```

To crop (640*480 from the left corner) and convert (from png to jpg) all images in a folder.
``` bash
plc -d /home/user/Pictures/ -k "0,0,640,480" -x jpg
```

## Usage Options
``` bash
usage: pillowcover [-h] [-v] [-d DIR] [-o OUTPUT_DIR] [-b BRIGHTNESS] [-c CONTRAST]
           [-s SHARPNESS] [-r RESIZE] [-R RESIZE_RATIO] [-k CROP]
           [-q COMPRESSION] [-x EXTENSION]
           [image_file]

PillowCover: Mass Manipulate Images Using Python: Change Brightness, Contrast,
Sharpness, Resize, Compress, Crop and Convert. A simple script (wrapper) using
pillow. Licensed Under: GNU General Public License v3 or later (GPLv3+)

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
  -k CROP, --crop CROP  Crop img by providing starting point then width and
                        length from it e.g pillowcase.py img -k "0,0,640,480"
  -q COMPRESSION, --compression-quality COMPRESSION
                        Compression quality 1-100, 100 means no compression at
                        all
  -x EXTENSION, --extension EXTENSION
                        Specifiy the output extension. Can be 'jpg', 'jpeg',
                        'png' Default is same as the input file's. e.g
                        pillowcase.py -d imgdir -x "jpg"


```
