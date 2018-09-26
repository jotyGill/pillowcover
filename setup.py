import sys

import setuptools

from pillowcover import __version__

if sys.version_info < (3, 5):
    sys.stderr.write(
        "ERROR: pillowcover requires Python 3.5 or above."
        + "Install using 'pip3' instead of just 'pip' \n"
    )
    sys.exit(1)

with open("README.md", encoding="utf-8") as readme_file:
    full_description = readme_file.read()
    readme_file.close()

setuptools.setup(
    name="pillowcover",
    version=__version__,
    description="Easily Manipulate Images Using Python: Change Brightness, Contrast, Sharpness, Resize",
    license="GNU General Public License v3 or later (GPLv3+)",
    author="JGill",
    zip_safe=False,
    author_email="joty@mygnu.org",
    url="https://github.com/jotyGill/pillowcover",
    keywords=["images", "image-minipulation"],
    install_requires=["pillow"],
    platforms=["GNU/Linux", "Ubuntu", "Debian", "Kali", "CentOS", "Arch", "Fedora"],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pillowcover = pillowcover.pillowcover:main",
            "plc = pillowcover.pillowcover:main",
        ]
    },
    long_description=full_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
