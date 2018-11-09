import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'pdf_converter'
VERSION = '0.0.1'
AUTHOR = '4teamwork'
EMAIL = 'matthias.osswald@4teamwork.ch'
DESCRIPTION = 'File to PDF converter'
URL = 'https://github.com/busykoala/python_packaging'
REQUIRED = [
    'WeasyPrint==0.42.3',
    'markdown2==2.3.6',
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL V3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': [
            'start-app=pdf_converter.gui_application:main',
        ],
    },
)
