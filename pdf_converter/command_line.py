import argparse


def create_output_paths(output_dir, file_paths):
    output_file_paths = []
    output_dir = output_dir.rstrip('/') + '/'
    for file_path in file_paths:
        filename_incl_ext = file_path.split('/')[-1]
        filename = filename_incl_ext.split('.')[0]
        output_file_paths.append(output_dir + filename + '.pdf')

    return output_file_paths


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
