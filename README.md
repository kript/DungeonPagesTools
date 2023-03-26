# DungeonPagesTools
Tools for playing and interacting with Dungeon Pages https://www.pnparcade.com/products/dungeon-pages-core-set

## Tools

 * [MergeDungeonPages.py](MergeDungeonPages.py)

## Setup (Linux/MacOSX)

### Setup the virtualenv

```bash
python3 -mvenv ~/code/venvs/DungeonPages
source ~/code/venvs/DungeonPages/bin/activate
pip install -r requirements.txt
```

### setup the pre-commit & Static Code Analysis (Ubuntu Linux)

`sudo apt install pre-commit`

## Merge Dungeon Pages

Thanks to BohemianCoast who submitted this [pastbin script](https://pastebin.com/QnMJVXqu) on the ButtonShy Discord.

> This is a script to take the pdf of the excellent print and play game Dungeon Pages and combine characters and dungeons to make mix and match playsheets so you can play them on a tablet. You'll need the game, which you can buy at https://www.pnparcade.com/products/dungeon-pages-core-set

> importing pdf - put your version of the game here. Your folder should have this script and the game pdf and nothing else because I'm doing everything in place because I don't really understand file handling very well. If you have *both* the core set and the yearlong set then I'd recommend amalgamating the pdfs before you start or amending this script.

It will take a single PDF of all the Core Set and  Year Long Adventures (up to the first nine weeks)  combined, in a file called  "Dungeon Pages For Combining.pdf", and generate a new set of PNG files in the same directory called "The Adventures of {character} in {dungeon}.png"  which is optimised for an iPad.

### Creating a Single PDF file (Ubuntu Linux)

```bash
# Install qpdf
sudo apt install qpdf
# merge PDF files to get a file for the above tool
qpdf --empty --pages \
DungeonPages_CoreSet_v1.01_010723.pdf \
DungeonPages_YLA_WK1_AmadorSteamCleric_Havington_011223.pdf \
DungeonPages_YLA_WK2_SygridVengefulHunter_Hogglebottom_011223.pdf \
DungeonPages_YLA_WK3_GloriaVirtuousWarrior_Whittleberry_011823.pdf \
DungeonPages_YLA_WK4_DrokOutcastTroll_Bordertown_012523.pdf \
DungeonPages_YLA_WK5_ZafinnMischievousWizard_ShanTomb_013123.pdf \
DungeonPages_YLA_WK6_MiraBrushRanger_AbyssalPlane_020223.pdf \
DungeonPages_YLA_WK7_RedGloveKnight_CapitalCity_021623.pdf \
DungeonPages_YLA_WK8_KreteKreeg_Stormshield_022323.pdf \
DungeonPages_YLA_WK9_AmadorWoodwardCleric_TheHungryIsles_022523.pdf \
-- "Dungeon Pages For Combining.pdf"
# run the combining tool
python3 MergeDungeonPages.py
# clear up the temporary files
rm {c,d}*.png
```
