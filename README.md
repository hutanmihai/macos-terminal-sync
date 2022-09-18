# Syncing color themes between iTerm2, macOS Terminal.app and VSCode Terminal

This is a script that is syncing the color themes between these 3.
In this repository you can already find a bunch of color themes ported from
[iTerm2 color schemes, collected by @mbadolato][1]. 
Screenshots are demonstrated below and
in the `screenshots/` directory of this repo.

[1]: https://github.com/mbadolato/iTerm2-Color-Schemes

TIP: Some default macOS themes are not included here (default themes like
"Pro", "Basic", "Grass", etc.), because you already have them :)


## Prerequisites

You need to install pipenv using this command:
```sh
$ pip3 install pipenv
```

PERSONAL OPINION:
- I would suggest you follow this guide https://medium.com/seokjunhong/customize-the-terminal-zsh-iterm2-powerlevel10k-complete-guide-for-beginners-35c4ba439055 as it shows in a easy way how to install oh-my-zsh, iTerm2 and powerlevel10k properly.

In the code files of this project I set up the custom font family as `MesloLGS NF`, so you need to install it, or change the code with one that you already have installed.

TIP: `MesloLGS NF` is a font that supports icons.

You can Download the font here https://github.com/romkatv/dotfiles-public/blob/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf.

TIP: Don't forget to also install it.

Since terminal themes are just color schemes, you need to enable color formatting for your shell first - see [this comment][2] for more details

[2]: https://github.com/lysyi3m/macos-terminal-themes/issues/1#issuecomment-148635036


## Installation Instructions

- Clone this repo

- Choose your favourite colorscheme from `itermcolorschemes/` folder

TIP: If you don't have iTerm2 you can skip the next 2 steps.

- You can check them either by importing them in iterm2 as follows:
        -> Open iTerm2
        -> Upper left corner click on iTerm2 -> Preferences -> Profiles -> Colors -> Color Presets -> Import
        -> After you selected Import you can import themes from the `itermcolorschemes/` folder

- After finding and setting up your favourite theme for iTerm2 it's time to run the script.


## Tools

### Convert iTerm2 Color Scheme

This repo contains a tool to convert any iTerm2 color theme into macOS
Terminal theme. To run just execute script:

```sh
$ pipenv shell
$ python3 script.py
```

## Screenshots

### 3024 Day

![Screenshot](screenshots/3024_day.png)

### 3024 Night

![Screenshot](screenshots/3024_night.png)

### AdventureTime

![Screenshot](screenshots/adventuretime.png)

### Afterglow

![Screenshot](screenshots/afterglow.png)

### AlienBlood

![Screenshot](screenshots/alienblood.png)

### Alucard

![Screenshot](screenshots/alucard.png)

### Argonaut

![Screenshot](screenshots/argonaut.png)

### Arthur

![Screenshot](screenshots/arthur.png)

### AtelierSulphurpool

![Screenshot](screenshots/ateliersulphurpool.png)

### Atom 

![Screenshot](screenshots/atom.png)

### Atom One Light

![Screenshot](screenshots/atomonelight.png)

### ayu 

![Screenshot](screenshots/ayu.png)

### ayu Light 

![Screenshot](screenshots/ayu_light.png)

### Ayu Mirage

![Screenshot](screenshots/ayu_mirage.png)

### Batman 

![Screenshot](screenshots/batman.png)

### Belafonte Day

![Screenshot](screenshots/belafonte_day.png)

### Belafonte Night 

![Screenshot](screenshots/belafonte_night.png)

### BirdsOfParadise 

![Screenshot](screenshots/birdsofparadise.png)

### Blazer 

![Screenshot](screenshots/blazer.png)

### Borland

![Screenshot](screenshots/borland.png)

### Bright Lights

![Screenshot](screenshots/bright_lights.png)

### Broadcast 

![Screenshot](screenshots/broadcast.png)

### Brogrammer

![Screenshot](screenshots/brogrammer.png)

### C64 

![Screenshot](screenshots/c64.png)

### Chalice 

![Screenshot](screenshots/chalice.png)

### Chalice Dark 

![Screenshot](screenshots/chalice_dark.png)

### Chalk 

![Screenshot](screenshots/chalk.png)

### Chalkboard 

![Screenshot](screenshots/chalkboard.png)

### Ciapre

![Screenshot](screenshots/ciapre.png)

### CLRS 

![Screenshot](screenshots/clrs.png)

### Cobalt Neon

![Screenshot](screenshots/cobalt_neon.png)

### Cobalt2 

![Screenshot](screenshots/cobalt2.png)

### CrayonPonyFish 

![Screenshot](screenshots/crayonponyfish.png)

### Dark Pastel 

![Screenshot](screenshots/dark_pastel.png)

### Darkside 

![Screenshot](screenshots/darkside.png)

### Desert 

![Screenshot](screenshots/desert.png)

### DimmedMonokai

![Screenshot](screenshots/dimmedmonokai.png)

### DotGov 

![Screenshot](screenshots/dotgov.png)

### Dracula

![Screenshot](screenshots/dracula.png)

### Dumbledore 

![Screenshot](screenshots/dumbledore.png)

### Duotone Dark 

![Screenshot](screenshots/duotone_dark.png)

### Earthsong

![Screenshot](screenshots/earthsong.png)

### Elemental

![Screenshot](screenshots/elemental.png)

### ENCOM 

![Screenshot](screenshots/encom.png)

### Espresso 

![Screenshot](screenshots/espresso.png)

### Espresso Libre 

![Screenshot](screenshots/espresso_libre.png)

### Fideloper

![Screenshot](screenshots/fideloper.png)

### FishTank

![Screenshot](screenshots/fishtank.png)

### Flat 

![Screenshot](screenshots/flat.png)

### Flatland 

![Screenshot](screenshots/flatland.png)

### Floraverse

![Screenshot](screenshots/floraverse.png)

### FrontEndDelight 

![Screenshot](screenshots/frontenddelight.png)

### FunForrest

![Screenshot](screenshots/funforrest.png)

### Galaxy 

![Screenshot](screenshots/galaxy.png)

### Github 

![Screenshot](screenshots/github.png)

### Glacier 

![Screenshot](screenshots/glacier.png)

### GoaBase 

![Screenshot](screenshots/goabase.png)

### Grape 

![Screenshot](screenshots/grape.png)

### Grass 

![Screenshot](screenshots/grass.png)

### Hardcore

![Screenshot](screenshots/hardcore.png)

### Harper 

![Screenshot](screenshots/harper.png)

### Highway 

![Screenshot](screenshots/highway.png)

### Hipster Green 

![Screenshot](screenshots/hipster_green.png)

### Homebrew

![Screenshot](screenshots/homebrew.png)

### Hurtado

![Screenshot](screenshots/hurtado.png)

### Hybrid 

![Screenshot](screenshots/hybrid.png)

### IC_Green_PPL 

![Screenshot](screenshots/ic_green_ppl.png)

### IC_Orange_PPL 

![Screenshot](screenshots/ic_orange_ppl.png)

### idleToes 

![Screenshot](screenshots/idletoes.png)

### IR_Black 

![Screenshot](screenshots/ir_black.png)

### Jackie Brown 

![Screenshot](screenshots/jackie_brown.png)

### Japanesque 

![Screenshot](screenshots/japanesque.png)

### Jellybeans 

![Screenshot](screenshots/jellybeans.png)

### JetBrains Darcula

![Screenshot](screenshots/jetbrains_darcula.png)

### Kibble 

![Screenshot](screenshots/kibble.png)

### Later This Evening 

![Screenshot](screenshots/later_this_evening.png)

### Lavandula 

![Screenshot](screenshots/lavandula.png)

### LiquidCarbon 

![Screenshot](screenshots/liquidcarbon.png)

### LiquidCarbonTransparent 

![Screenshot](screenshots/liquidcarbontransparent.png)

### LiquidCarbonTransparentInverse

![Screenshot](screenshots/liquidcarbontransparentinverse.png)

### Man Page

![Screenshot](screenshots/man_page.png)

### Mariana

![Screenshot](screenshots/mariana.png)

### Material 

![Screenshot](screenshots/material.png)

### MaterialDark

![Screenshot](screenshots/materialdark.png)

### Mathias 

![Screenshot](screenshots/mathias.png)

### Medallion 

![Screenshot](screenshots/medallion.png)

### Misterioso

![Screenshot](screenshots/misterioso.png)

### Molokai 

![Screenshot](screenshots/molokai.png)

### MonaLisa

![Screenshot](screenshots/monalisa.png)

### Monokai Pro (Filter Spectrum)

![Screenshot](screenshots/monokai_pro__filter_spectrum_.png)

### Monokai Soda

![Screenshot](screenshots/monokai_soda.png)

### N0tch2k 

![Screenshot](screenshots/n0tch2k.png)

### Neopolitan 

![Screenshot](screenshots/neopolitan.png)

### Neutron 

![Screenshot](screenshots/neutron.png)

### Night Owl 

![Screenshot](screenshots/night_owl.png)

### NightLion v1

![Screenshot](screenshots/nightlion_v1.png)

### NightLion v2

![Screenshot](screenshots/nightlion_v2.png)

### Nova 

![Screenshot](screenshots/nova.png)

### Novel

![Screenshot](screenshots/novel.png)

### Obsidian

![Screenshot](screenshots/obsidian.png)

### Ocean 

![Screenshot](screenshots/ocean.png)

### OceanicMaterial

![Screenshot](screenshots/oceanicmaterial.png)

### Ollie 

![Screenshot](screenshots/ollie.png)

### Parasio Dark

![Screenshot](screenshots/parasio_dark.png)

### PaulMillr

![Screenshot](screenshots/paulmillr.png)

### Pencil Dark

![Screenshot](screenshots/pencildark.png)

### Pencil Light 

![Screenshot](screenshots/pencillight.png)

### Piatto Light 

![Screenshot](screenshots/piatto_light.png)

### Pnevma 

![Screenshot](screenshots/pnevma.png)

### Pro

![Screenshot](screenshots/pro.png)

### Red Alert 

![Screenshot](screenshots/red_alert.png)

### Red Sands 

![Screenshot](screenshots/red_sands.png)

### Relaxed 

![Screenshot](screenshots/relaxed.png)

### Renault Style

![Screenshot](screenshots/renault_style.png)

### Renault Style Light

![Screenshot](screenshots/renault_style_light.png)

### Rippedcasts 

![Screenshot](screenshots/rippedcasts.png)

### Royal 

![Screenshot](screenshots/royal.png)

### Seafoam Pastel 

![Screenshot](screenshots/seafoam_pastel.png)

### SeaShells 

![Screenshot](screenshots/seashells.png)

### Seti 

![Screenshot](screenshots/seti.png)

### Shaman

![Screenshot](screenshots/shaman.png)

### Slate 

![Screenshot](screenshots/slate.png)

### Smyck 

![Screenshot](screenshots/smyck.png)

### SoftServer

![Screenshot](screenshots/softserver.png)

### Solarized Darcula

![Screenshot](screenshots/solarized_darcula.png)

### Solarized Dark

![Screenshot](screenshots/solarized_dark.png)

### Solarized Dark (patched)

![Screenshot](screenshots/solarized_dark___patched.png)

### Solarized Dark Higher Contrast

![Screenshot](screenshots/solarized_dark_higher_contrast.png)

### Solarized Light

![Screenshot](screenshots/solarized_light.png)

### Source Code X 

![Screenshot](screenshots/source_code_x.png)

### Spacedust 

![Screenshot](screenshots/spacedust.png)

### SpaceGray 

![Screenshot](screenshots/spacegray.png)

### SpaceGray Eighties

![Screenshot](screenshots/spacegray_eighties.png)

### SpaceGray Eighties

![Screenshot](screenshots/spacegray_eighties_dull.png)

### Spiderman 

![Screenshot](screenshots/spiderman.png)

### Spring 

![Screenshot](screenshots/spring.png)

### Square

![Screenshot](screenshots/square.png)

### Sundried 

![Screenshot](screenshots/sundried.png)

### Symfonic

![Screenshot](screenshots/symfonic.png)

### Tango Dark

![Screenshot](screenshots/tango_dark.png)

### Tango Light

![Screenshot](screenshots/tango_light.png)

### Teerb

![Screenshot](screenshots/teerb.png)

### Thayer Bright

![Screenshot](screenshots/thayer_bright.png)

### The Hulk

![Screenshot](screenshots/the_hulk.png)

### Tomorrow

![Screenshot](screenshots/tomorrow.png)

### Tomorrow Night

![Screenshot](screenshots/tomorrow_night.png)

### Tomorrow Night Blue

![Screenshot](screenshots/tomorrow_night_blue.png)

### Tomorrow Night Bright

![Screenshot](screenshots/tomorrow_night_bright.png)

### Tomorrow Night Eighties

![Screenshot](screenshots/tomorrow_night_eighties.png)

### ToyChest

![Screenshot](screenshots/toychest.png)

### Treehouse

![Screenshot](screenshots/treehouse.png)

### Twilight

![Screenshot](screenshots/twilight.png)

### Ubuntu

![Screenshot](screenshots/ubuntu.png)

### Unikitty

![Screenshot](screenshots/unikitty.png)

### Urple

![Screenshot](screenshots/urple.png)

### Vaughn

![Screenshot](screenshots/vaughn.png)

### VibrantInk

![Screenshot](screenshots/vibrantink.png)

### VS Code Dark Plus

![Screenshot](screenshots/vs_code_dark_plus.png)

### VS Code Light Plus

![Screenshot](screenshots/vs_code_light_plus.png)

### WarmNeon

![Screenshot](screenshots/warmneon.png)

### Wez

![Screenshot](screenshots/wez.png)

### WildCherry

![Screenshot](screenshots/wildcherry.png)

### Wombat

![Screenshot](screenshots/wombat.png)

### Wryan

![Screenshot](screenshots/wryan.png)

### Zenburn

![Screenshot](screenshots/zenburn.png)
