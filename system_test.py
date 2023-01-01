import errno
import os

import yaml
import sys
import subprocess
import shlex

n_args = len(sys.argv)

if (n_args==1):
    print("no file to load", file=sys.stderr)
    sys.exit(1)


file_name = sys.argv[1]

class YamlLoader:
    def __init__(self, yaml_file_name):
        self.file_name = yaml_file_name
        self.fileb = open(file_name, 'r')
        self.data = yaml.safe_load(self.fileb)


class Verifier(YamlLoader):
    def verify(self):
        all_pass = True
        for verifier in self.data:
            print(verifier)
            print("verifying ",self.data[verifier]['category'])
            this_pipe = subprocess.Popen(self.data[verifier]['acquire'], shell=True, bufsize=-1, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out, err = this_pipe.communicate()
            string_to_compare = out.decode('ascii').strip()
            print("\t got:", string_to_compare)
            matched = False
            for possible_match in self.data[verifier]['accepted_values']:
                if string_to_compare == possible_match:
                    matched = True
            if matched is False:
                print ("could not verify")
                all_pass = False
        return all_pass


system_ok = Verifier(file_name).verify()
print("system is ok? ",system_ok)




