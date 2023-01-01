import errno
import yaml
import sys
import subprocess
import shlex

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


yaml_data=yaml.safe_load(fileb)
print(yaml_data['BOM']['category'])
args = shlex.split(yaml_data['BOM']['acquire'])
print(args)
try:
    p = subprocess.Popen(args)
except OSError as err:
    print("could not run command: ",yaml_data['BOM']['acquire'], file=sys.stderr)
    sys.exit(1)

print (p)
