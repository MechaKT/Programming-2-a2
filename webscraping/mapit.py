# mapit.py - tool to search physical addresses
# usage -- python mapit.py 6600 Williams Road Richmond
#    output: should take us to the address in GMaps

import webbrowser
import sys
import pyperclip


# if there are NO ARGUMENTS
# grab address from clipboard
if len(sys.argv) < 2:
    address = pyperclip.paste()
else:
    address = " ".join(sys.argv[1:])

print(f"Finding {address}...")
# join(list) -> string
# Takes a list and gives it a string


prefix = "https://google.com/maps/place/"
webbrowser.open(prefix + address)
