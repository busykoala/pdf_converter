# Busykoala PDF Converter

Busykoala PDF Converter is a CLI application for converting
files to PDF.

## Supported Filetypes

Currently supported filetypes are:

    - Markdown (.md)
    - Word Documents (.docx)
    - RestructuredText (.rst)

## Quickstart

Clone and install package:

```zsh
git clone git@github.com:busykoala/pdf_converter.git
cd pdf_converter
path/to/python3.7.1 -m venv venv
source venv/bin/activate
python setup.py install
```

This package needs cairo installed.

## Usage

```zsh
convert output-dir input-filepath [input-filepath ...]
```

## Test

```zsh
python -m pytest
```
