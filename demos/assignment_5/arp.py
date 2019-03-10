import argparse

parser = argparse.ArgumentParser(prog="argparse test", description="Process some text.")
parser.add_argument(
    "-f",
    "--file",
    type=argparse.FileType("r", encoding="UTF-8"),
    help="filename to open",
)

args = parser.parse_args()


def main(text_file):
    with text_file as infile:
        for line in infile:
            print(line, end="")


if __name__ == "__main__":
    main(args.file)
