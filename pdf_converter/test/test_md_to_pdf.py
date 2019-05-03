from pdf_converter.converting_pdf import PdfConverter
import pdf_converter
import _io


def test_filetype_md_is_recognized():
    input_file_dir = './assets/testfile.md'
    file_instance = PdfConverter(input_file_dir)
    file_instance.set_file_format()

    assert file_instance.file_format == 'Markdown'


def test_converting_md_to_pdf(tmpdir):
    package_path = pdf_converter.__path__[0]
    input_file_dir = package_path + '/test/assets/testfile.md'
    output_path = str(tmpdir) + '/testfile.pdf'

    file_instance = PdfConverter(input_file_dir)
    file_instance.set_file_format()
    file_instance.convert_markdown(output_path)

    # We expect that there is a converted file
    # now. The converted file should be saved at
    # the given output directory "output_path".
    with open(output_path) as f_:
        pdf_file = f_

    assert isinstance(pdf_file, _io.TextIOWrapper) is True
