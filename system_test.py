import yaml
import sys

print("hello_world")
n_args = len(sys.argv)

if (n_args==1):
    print("no file to load", file=sys.stderr)
    sys.exit(1)


