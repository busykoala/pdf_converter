# Busykoala PDF Converter

## Study Project

This project is a study project for me to get to know python better.

It has been tested with python 3.7.1

## Goal

The package shall convert as much fileformats to pdf as it's possible in the
scope of this project.

## Quickstart

Clone and install package:

```zsh
git clone git@github.com:busykoala/pdf_converter.git

cd pdf_converter

path/to/python3 -m venv venv

source venv/bin/activate

python setup.py install
```

This package needs cairo installed.

## Supported Filetypes

Currently supported filetypes are:

    - Markdown (.md)
    - Word Documents (.docx)
    - RestructuredText (.rst)

## Usage

The GUI can be started with:

```zsh
start-app
```

The CLI can be started with"

```zsh
convert output-dir input-filepath [input-filepath ...]
```
