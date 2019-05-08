from pdf_converter.converting_pdf import PdfConverter


def test_unsupported_filetypes():
    input_file_dir = './assets/koala_tree.jpg'
    file_instance = PdfConverter(input_file_dir)
    file_instance.set_file_format()

    assert file_instance.file_format is False
