from os import path, system
from shutil import move as movefile
from json import load as loadjson, dump as dumpjson

DIRNAME = path.dirname(__file__)

def change_background():
    with open(PATH_VSCODE_SETTINGS, 'r') as json_file:
        vsc_settings = loadjson(json_file)
    vsc_settings['workbench.colorCustomizations']['terminal.background'] = None
    with open(PATH_VSCODE_SETTINGS, 'w') as json_file:
        dumpjson(vsc_settings, json_file)


print('Hello, please pay attention to all the instructions'
        , ' '
        , '-'*50
        , sep='\n'
)

print('Enter the path to the itermcolors file: ')

PATH_ITERMCOLORS = input().strip()

PATH_WITHOUT_THEME = '/'.join(PATH_ITERMCOLORS.split('/')[:-1]).strip()
THEME_NAME = ''.join(PATH_ITERMCOLORS.split('/')[-1].split('.')[0]).strip()

print('-'*50
        , ' '
        , sep='\n'
)

system(f'./tools/iterm2terminal.swift "{PATH_ITERMCOLORS}"')

print(' ', 
        '-'*50
        , sep='\n'
)

movefile(f'{PATH_WITHOUT_THEME}/{THEME_NAME}.terminal', f'{DIRNAME}/generated_themes/{THEME_NAME}.terminal')

print('Now I will open the new generated file for you!',
        '-'*50
        ,'All you have to do is to press in the upper left corner on "Shell" and then "Use Settings as Default"'
        ,'-'*50
        ,'After that you can close the window and the theme will be installed!'
        , sep='\n'
)

system(f'open "{DIRNAME}/generated_themes/{THEME_NAME}.terminal"')

print('You are ready to go! Or maybe not? One more question, do you use VSCode? (y/n)')

USE_VSCODE = input().strip()

if USE_VSCODE == 'y':
    print('In order to have all Terminals with the same theme, you have to set the theme in the settings.json file of VSCode'
            ,'Enter the path to the settings.json file of VSCode: '
    )
    PATH_VSCODE_SETTINGS = input().strip()
    print('Now I will do some work for you!'
            , '-'*50
            , sep='\n'
    )

    system(f'python3 ./tools/iterm2vsc.py "{PATH_ITERMCOLORS}" "{PATH_VSCODE_SETTINGS}"')

    print('In my opinion, the background color is not always fitting well, do you want me to change it to the basic one from vscode? (y/n)')

    CHANGE_BACKGROUND = input().strip()

    if CHANGE_BACKGROUND == 'y':
        change_background()
        print('I changed the background color to the default one from vscode!'
                , '-'*50
                , sep='\n'
        )
    print('-' * 100
            , 'Have fun with your new theme!'
            , sep='\n'
     )
else:
    print('Have fun with your new theme!')
