"""
This script decodes a plist file to a json file.
"""

import sys
import json
import plistlib

# Decode the plist file and print it as JSON
plist = open(sys.argv[1], 'rb')
json_file = json.dumps(plistlib.load(plist), indent=4)
print(json_file)