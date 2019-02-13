#! /usr/bin/env python3
"""
Reports the number of times a given word appears in a text file.

Usage:
    word-count (-f <FILE> | --file=<FILE>) (-w <WORD> | --word=<WORD>) [-i]
    word-count -h | --help

Options:
    -f FILE --file=<FILE>   Open the file named <FILE>
    -w WORD --word=<WORD>   Search for the word <WORD>
    -i                      Case insensitive search [default: False]
    -h --help               Show this message
"""
import getopt
import string
import sys


def search(filename, target_word, case_sensitive):
    """
    Search the given file for the target word and return a count of the
    instances found. By default the search is case sensitive.
    """
    try:
        with open(filename, "r") as file:
            translator = str.maketrans("", "", string.punctuation)
            count = 0
            for line in file.readlines():
                line = line.translate(translator)
                if not case_sensitive:
                    line = line.lower()
                for word in line.split():
                    if word == target_word:
                        count += 1
    except IOError as err:
        print(err)
        sys.exit()

    return count


def usage():
    """Display usage information."""
    print(__doc__)


def main():
    """
    Get, parse, and verify user input.
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:w:ih", ["file=", "word=", "help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    file = None
    word = None
    case_sensitive = True

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i"):
            case_sensitive = False
        elif o in ('-f", "--file'):
            file = a
        elif o in ("-w", "--word"):
            word = a

    if word is None or file is None:
        usage()
        sys.exit()

    count = search(file, word, case_sensitive)
    print(count)


if __name__ == "__main__":
    main()
