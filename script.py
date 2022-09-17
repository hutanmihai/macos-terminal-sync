import os
import sys
import pprint
from shutil import move as movefile

DIRNAME = os.path.dirname(__file__)

print('Hello, please pay attention to all the instructions')
print()
print('-' * 100)

print('Enter the path to the itermcolors file: ')

PATH_ITERMCOLORS = input().strip()

PATH_WITHOUT_THEME = '/'.join(PATH_ITERMCOLORS.split('/')[:-1]).strip()
THEME_NAME = ''.join(PATH_ITERMCOLORS.split('/')[-1].split('.')[0]).strip()

print('-' * 100)
print()
os.system(f'./tools/iterm2terminal.swift "{PATH_ITERMCOLORS}"')
print()
print('-' * 100)
movefile(f'{PATH_WITHOUT_THEME}/{THEME_NAME}.terminal', f'{DIRNAME}/generated_themes/{THEME_NAME}.terminal')
print('Now I will open the new generated file for you!')
print('-' * 100)
print('All you have to do is to press in the upper left corner on "Shell" and then "Use Settings as Default"')
print('-' * 100)
print('After that you can close the window and the theme will be installed!')

os.system(f'open "{DIRNAME}/generated_themes/{THEME_NAME}.terminal"')

print('You are ready to go! Or maybe not? One more question, do you use VSCode? (y/n)')

USE_VSCODE = input().strip()

if USE_VSCODE == 'y':
    print('In order to have all Terminals with the same theme, you have to set the theme in the settings.json file of VSCode')
    print('Enter the path to the settings.json file of VSCode: ')
    PATH_VSCODE_SETTINGS = input().strip()
    print('Now I will do some work for you!')
    print('-' * 100)
    os.system(f'python3 ./tools/iterm2vsc.py "{PATH_ITERMCOLORS}" "{PATH_VSCODE_SETTINGS}"')
    print('-' * 100)
    print('Done! You can close this window now!')
else:
    print('Have fun with your new theme!')
