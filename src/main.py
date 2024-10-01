import argparse
import syntactic

parser = argparse.ArgumentParser(
    prog='HouseLang',
    description='Programming language for learning.',
    epilog='Make with ♡')
parser.add_argument("filename", nargs="?")

args = parser.parse_args()

def start_while():
    lang = syntactic.HouseLang()
    print("HouseLang 0.0.1")
    while True:
        try:
            command = input(">>> ")
            lang.eval(command)
        except EOFError: exit(0)
        except syntactic.SyntacticException as e: print(e)

if args.filename == None:
    start_while()
else:
    lang = syntactic.HouseLang()
    with open(args.filename, "r") as f:
        data = f.readlines()
    for line in data:
        lang.eval(line)