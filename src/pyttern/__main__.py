import argparse

from .pyttern_parser import main

parser = argparse.ArgumentParser(
    prog='Pyttern',
    description='Parse Pyttern code')

exclusive_group = parser.add_mutually_exclusive_group()

exclusive_group.add_argument('-b', '--brut',
                             action='store_true')
parser.add_argument("pytternFile")
exclusive_group.add_argument("-c", "--codeFile", required=False)

args = parser.parse_args()
main(args)
