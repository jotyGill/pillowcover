

# pillowcover
Easily Manipulate Images Using Python: Change Brightness, Contrast, Sharpness, Resize.
A simple script (wrapper) using pillow.

## Requirements
python3, pillow

## Usage
``` bash
pillow -d /home/user/Downloads/ -b 1.2 -c 1.2 -s 1.2 -r "1600 1200" -q 40
```

## Usage Options
``` bash
usage: pillowcover.py [-h] [-v] [-d DIR] [-b BRIGHTNESS] [-c CONTRAST]
                      [-s SHARPNESS] [-r RESIZE] [-q COMPRESSION]
                      [image_file]

Easily Manipulate Images Using Python: Change Brightness,Contrast, Sharpness,
Resize

positional arguments:
  image_file            Full path to the image file to edit

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program\'s version number and exit
  -d DIR, --dir DIR     Full path to the directory containing the image files
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        Change brightness level, 1.0 is the current value
  -c CONTRAST, --contrast CONTRAST
                        Change contrast level, 1.0 is the current value
  -s SHARPNESS, --sharpness SHARPNESS
                        Change sharpness level, 1.0 is the current value
  -r RESIZE, --resize RESIZE
                        Resize img by providing new length and width e.g
                        pillowcase.py img -r "640 480"
  -q COMPRESSION, --compression-quality COMPRESSION
                        Compression quality, 100 means no compression at all

```
