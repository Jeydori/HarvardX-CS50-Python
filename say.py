import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex(f"Hi, {sys.argv[1]}")
