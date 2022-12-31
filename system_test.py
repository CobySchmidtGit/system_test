import errno
import yaml
import sys

print("hello_world")
n_args = len(sys.argv)

if (n_args==1):
    print("no file to load", file=sys.stderr)
    sys.exit(1)


file_name = sys.argv[1]

try:
    fileb = open(file_name, 'r')
except IOError as e:
    print("could not open file", file_name,  ":", e.strerror, file=sys.stderr)
    sys.exit(1)


yaml_data=yaml.load(fileb)
for BOM in yaml_data:
        for dir in BOM:
                print (dir)
