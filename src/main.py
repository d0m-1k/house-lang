import argparse
import syntactic
import sys

parser = argparse.ArgumentParser(
    prog='HouseLang',
    description='Programming language for learning.',
    epilog='Make with ♡')
parser.add_argument("filename", nargs="?")

args = parser.parse_args()

version = "0.0.3"

def start_while():
    lang = syntactic.HouseLang()
    print(f"HouseLang {version}")
    while True:
        try:
            command = input(">>> ")
            lang.eval(command)
        except EOFError: sys.exit(0)
        except syntactic.SyntacticException as e: print(e)
    sys.exit(1)

if args.filename == None:
    start_while()
else:
    lang = syntactic.HouseLang()
    with open(args.filename, "r") as f:
        data = f.readlines()
    for line in data:
        lang.eval(line)