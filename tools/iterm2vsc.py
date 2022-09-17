import sys
import json
import math
import xmltodict

PATH_VSCODE_SETTINGS = sys.argv[2].strip()
PATH_ITERMCOLORS = sys.argv[1].strip()

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

iterm_theme_values_list = xmltodict.parse(open(PATH_ITERMCOLORS, 'r').read())['plist']['dict']['dict']
iterm_theme_keys_list = xmltodict.parse(open(PATH_ITERMCOLORS, 'r').read())['plist']['dict']['key']

vsc_theme = {}
 
IDK = {}

counter = 0

for dict in iterm_theme_values_list:
    b, g, r = dict['real']
    blue  = math.floor(float(b) * 255)
    green = math.floor(float(g) * 255)
    red   = math.floor(float(r) * 255)
    IDK[iterm_theme_keys_list[counter]] = '#%02x%02x%02x' % (red, green, blue)
    counter += 1

for key in MAP:
    if MAP[key] in IDK.keys():
        vsc_theme[key] = IDK[MAP[key]]

# Read the settings.json file and save it to vsc_settings dictionary
with open(PATH_VSCODE_SETTINGS, 'r') as json_file:
    vsc_settings = json.load(json_file)

# Replace the colors in the settings.json file with the converted values
for key in vsc_theme:
        vsc_settings['workbench.colorCustomizations'][key] = vsc_theme[key]

vsc_settings['terminal.integrated.fontFamily'] = 'MesloLGS NF'

# Write the new settings.json file to the path specified in VSC_SETTINGS_PATH
with open(PATH_VSCODE_SETTINGS, 'w') as json_file:
    json.dump(vsc_settings, json_file, indent=4)
