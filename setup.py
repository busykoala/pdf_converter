import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'pdf_converter'
VERSION = '0.0.1'
AUTHOR = '4teamwork'
EMAIL = 'matthias.osswald@4teamwork.ch'
DESCRIPTION = 'File to PDF converter'
URL = 'https://github.com/busykoala/pdf_converter'
REQUIRED = [
    'pytest',
    'cairocffi<1.0.1',
    'WeasyPrint',
    'markdown2',
    'mammoth',
    'docutils',
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
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU GPL V3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': [
            'convert=pdf_converter.command_line:main',
        ],
    },
)
