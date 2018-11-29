import argparse
from pdf_converter import converting_pdf


def create_output_paths(output_dir, file_paths):
    output_file_paths = []
    output_dir = output_dir.rstrip('/') + '/'
    for file_path in file_paths:
        filename_incl_ext = file_path.split('/')[-1]
        filename = filename_incl_ext.split('.')[0]
        output_file_paths.append(output_dir + filename + '.pdf')

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
            if file_instance.file_format == 'Markdown':
                file_instance.convert_markdown(output_file_dirs[index])
            if file_instance.file_format == 'Docx':
                file_instance.convert_docx(output_file_dirs[index])
            if file_instance.file_format == 'RestructuredText':
                file_instance.convert_rst(output_file_dirs[index])


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
