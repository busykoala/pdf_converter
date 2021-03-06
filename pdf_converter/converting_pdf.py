import mammoth
import markdown2
from weasyprint import HTML
from docutils import core


class PdfConverter(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = file_path.rsplit('/', 1)[1]
        self.file_format = False
        self.error_collection = {}

    def set_file_format(self):
        file_ending = self.file_name.rsplit('.', 1)[1]
        if file_ending == 'md':
            self.file_format = 'Markdown'
        if file_ending == 'docx':
            self.file_format = 'Docx'
        if file_ending == 'rst':
            self.file_format = 'RestructuredText'

    def convert_2_pdf(self):

        self.set_file_format()

        if not self.file_format:
            self.add_error('convert_2_pdf', 'File type isn\'t supported.')
        else:
            if self.file_format == 'Markdown':
                self.convert_markdown(self.file_path)
            if self.file_format == 'Docx':
                self.convert_docx(self.file_path)
            if self.file_format == 'RestructuredText':
                self.convert_rst(self.file_path)

    def read_file_to_bytes(self):
        with open(self.file_path, 'rb') as file_:
            return file_.read()

    def convert_markdown(self, output_path):
        md2html_string = markdown2.markdown(
            self.read_file_to_bytes(),
            extras=["footnotes"]
        )
        html = HTML(string=md2html_string)
        html.write_pdf(
            output_path,
        )

    def convert_docx(self, output_path):
        docx_file = open(self.file_path, 'rb')
        result = mammoth.convert_to_html(docx_file)
        docx_file.close()
        html = HTML(string=result.value)
        html.write_pdf(
            output_path,
        )

    def convert_rst(self, output_path):
        rst_file = self.read_file_to_bytes()
        html_code = core.publish_string(
            source=rst_file,
            writer_name='html').decode()
        result = html_code[html_code.find(
            '<body>') + 6:html_code.find('</body>')].strip()
        html = HTML(string=result)
        html.write_pdf(
            output_path,
        )

    def add_error(self, error_location, error_message):
        self.error_collection.update({error_location: error_message})

    def return_errors(self):
        return self.error_collection
