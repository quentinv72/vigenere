import argparse
from src import decipher
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, help="Name of cipher file")
parser.add_argument("-k", "--key", type=str, help="Vigenere cipher key")
parser.add_argument("-l", "--length", type=int, help="Key length")
parser.add_argument("-u", "--unknown", action="store_true", help="Unknown key length")

args = parser.parse_args()

if not args.filename:
    raise FileNotFoundError("Please add a filename")

with open(args.filename, mode="r") as f:
    cipher = f.read()

decipherer = decipher.VigenereDecipher(cipher, key=args.key)

if args.key:
    print(decipherer.decipher())
    sys.exit(0)

if args.length:
    print(decipherer.guess_key(args.length))
    sys.exit(0)

if args.unknown:
    print(decipherer.estimate_key_length())