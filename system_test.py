import errno
import os

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
    p = subprocess.Popen(yaml_data['BOM']['acquire'], shell=True, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #string_out = os.system(yaml_data['BOM']['acquire'])
except OSError as err:
    print("could not run command: ",yaml_data['BOM']['acquire'], file=sys.stderr)
    sys.exit(1)

out, err = p.communicate()
print (out.decode('ascii'))

accepted_value = yaml_data['BOM']['accepted_values']
string_to_compare=out.decode('ascii')
print (string_to_compare)
print (accepted_value)
if string_to_compare == accepted_value:
    print ("same")
else:
    print ("not same")


