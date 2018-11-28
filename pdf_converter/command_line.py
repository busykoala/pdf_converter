import argparse


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
    print(args.output_dir)
    print(args.file_paths)
