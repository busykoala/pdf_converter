import argparse
from pdf_converter import converting_pdf
from pathlib import Path


def create_output_paths(output_dir, file_paths):
    output_file_paths = []
    output_dir = output_dir.rstrip('/') + '/'
    for file_path in file_paths:
        filename_incl_ext = file_path.split('/')[-1]
        filename = filename_incl_ext.split('.')[0]
        output_file_paths.append(output_dir + filename)

    return output_file_paths


def convert_files_to_pdf(input_file_dirs, output_file_dirs):

    for index, input_file_dir in enumerate(input_file_dirs):
        file_instance = converting_pdf.PdfConverter(input_file_dir)
        file_instance.set_file_format()

        if not file_instance.file_format:
            pass
            # This could later on raise an
            # error saying file type isn't supported.
        else:
            # check if already exists
            file_exists = True
            temp_file = Path(output_file_dirs[index] + '.pdf')
            new_file_path = output_file_dirs[index]
            while file_exists is True:
                if not temp_file.is_file():
                    file_exists = False
                else:
                    temp_file = Path(new_file_path + '_new' + '.pdf')
                    new_file_path = new_file_path + '_new'
                    file_exists = True
            new_file_path = new_file_path + '.pdf'

            if file_instance.file_format == 'Markdown':
                file_instance.convert_markdown(new_file_path)
            if file_instance.file_format == 'Docx':
                file_instance.convert_docx(new_file_path)
            if file_instance.file_format == 'RestructuredText':
                file_instance.convert_rst(new_file_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir",
                        metavar='output-directory',
                        type=str,
                        nargs=1,
                        help="Path to save the file/s in")
    parser.add_argument("file_paths",
                        metavar='input-file',
                        type=str,
                        nargs='+',
                        help="Path of file to convert")
    args = parser.parse_args()

    output_paths = create_output_paths(args.output_dir[0], args.file_paths)
    convert_files_to_pdf(args.file_paths, output_paths)
