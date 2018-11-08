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

    def convert_2_pdf(self):

        self.set_file_format()

        if not self.file_format:
            self.add_error('convert_2_pdf', 'File type isn\'t supported.')
        else:
            if self.file_format == 'Markdown':
                self.convert_markdown()

    def convert_markdown(self):
        pass

    def add_error(self, error_location, error_message):
        self.error_collection.update({error_location: error_message})

    def return_errors(self):
        return self.error_collection
