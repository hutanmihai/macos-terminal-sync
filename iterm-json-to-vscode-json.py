"""
This script takes an iTerm Color Profile as an argument and translates it for use with Visual Studio Code's built-in terminal.

To export an iTerm Color Profile:
    1) Open iTerm
    2) Go to Preferences -> Profiles -> Colors
    3) Other Actions -> Save Profile as JSON

To generate the applicable color settings and use them in VS Code:
    1) MOST IMPORTANT: Set your correct vscode settings.json PATH in the VSC_SETTINGS_PATH variable below !!!
    2) Run this script from the command line: `python3 iterm-json-to-vscode-json.py [path-to-iterm-profile.json]
"""

import sys
import json
import math

VSC_SETTINGS_PATH =  "/Users/your_user/Library/Application Support/Code/User/settings.json"

MAP = {
  'terminal.background': 'Background Color',
  'terminal.foreground': 'Foreground Color',
  'terminalCursor.background': 'Cursor Text Color',
  'terminalCursor.foreground': 'Cursor Color',
  'terminal.ansiBlack': 'Ansi 0 Color',
  'terminal.ansiBlue': 'Ansi 4 Color',
  'terminal.ansiBrightBlack': 'Ansi 8 Color',
  'terminal.ansiBrightBlue': 'Ansi 12 Color',
  'terminal.ansiBrightCyan': 'Ansi 14 Color',
  'terminal.ansiBrightGreen': 'Ansi 10 Color',
  'terminal.ansiBrightMagenta': 'Ansi 13 Color',
  'terminal.ansiBrightRed': 'Ansi 9 Color',
  'terminal.ansiBrightWhite': 'Ansi 15 Color',
  'terminal.ansiBrightYellow': 'Ansi 11 Color',
  'terminal.ansiCyan': 'Ansi 6 Color',
  'terminal.ansiGreen': 'Ansi 2 Color',
  'terminal.ansiMagenta': 'Ansi 5 Color',
  'terminal.ansiRed': 'Ansi 1 Color',
  'terminal.ansiWhite': 'Ansi 7 Color',
  'terminal.ansiYellow': 'Ansi 3 Color',
  'terminal.selectionBackground':'Selection Color'
}

vsc_colors = {}

# Convert values of red green and blue from json file to Hex
def convert_to_hex(dict):
    green = math.floor(dict['Green Component'] * 255)
    red = math.floor(dict['Red Component'] * 255)
    blue = math.floor(dict['Blue Component'] * 255)
    return '#%02x%02x%02x' % (red, green, blue)

# Read the json file and save it to ITERM_COLORS dictionary
with open(sys.argv[1], 'r') as json_file:
    ITERM_COLORS = json.load(json_file)

# Save the converted values to vsc_colors dictionary
for key in MAP:
    if MAP[key] in ITERM_COLORS.keys():
        vsc_colors[key] = convert_to_hex(ITERM_COLORS[MAP[key]])

# Read the settings.json file and save it to vsc_settings dictionary
with open(VSC_SETTINGS_PATH, 'r') as json_file:
    vsc_settings = json.load(json_file)

# Replace the colors in the settings.json file with the converted values
for key in vsc_colors:
        vsc_settings['workbench.colorCustomizations'][key] = vsc_colors[key]

# Write the new settings.json file to the path specified in VSC_SETTINGS_PATH
with open(VSC_SETTINGS_PATH, 'w') as json_file:
    json.dump(vsc_settings, json_file, indent=4)
