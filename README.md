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
There is one step you have to do manually, which is to rename the PDF "DungeonPages_YLA_WK_013_ValensiAbyssWhisper_Tearburn Fields_032923.pdf" to "DungeonPages_YLA_WK_013_ValensiAbyssWhisper_TearburnFields_032923.pdf". This step is required only the first time, as the PDF is misnamed and does not respect the traditional nomenclature of the other sheets.

### Creating a Single PDF file (Ubuntu Linux)

```bash
# Install qpdf
sudo apt install qpdf
# merge PDF files to get a file for the above tool
qpdf --empty --pages \
DungeonPages_CoreSet_011223.pdf \
DungeonPages_YLA_WK_01_AmadorSteamCleric_Havington_011223.pdf \
DungeonPages_YLA_WK_02_SygridVengefulHunter_Hogglebottom_011223.pdf \
DungeonPages_YLA_WK_03_GloriaVirtuousWarrior_Whittleberry_011823.pdf \
DungeonPages_YLA_WK_04_DrokOutcastTroll_Bordertown_012523.pdf \
DungeonPages_YLA_WK_05_ZafinnMischievousWizard_ShanTomb_013123.pdf \
DungeonPages_YLA_WK_06_MiraBrushRanger_AbyssalPlane_020223.pdf \
DungeonPages_YLA_WK_07_RedGloveKnight_CapitalCity_021623.pdf \
DungeonPages_YLA_WK_08_KreteKreeg_Stormshield_022323.pdf \
DungeonPages_YLA_WK_09_AmadorWoodwardCleric_TheHungryIsles_022523.pdf \
DungeonPages_YLA_WK_010_ZafinnElementalWizard_BakorioProvince_030823.pdf \
DungeonPages_YLA_WK_011_SygridBanishedHunter_Lariss_031623.pdf \
DungeonPages_YLA_WK_012_GloriaDaredevilWarrior_FilganForest_032323.pdf \
DungeonPages_YLA_WK_013_ValensiAbyssWhisper_Tearburn Fields_032923.pdf' \
DungeonPages_YLA_WK_014_MiraLawlessRanger_SunsetQuarter_040723.pdf \
-- "Dungeon Pages For Combining.pdf"
# run the combining tool
python3 MergeDungeonPages.py
# clear up the temporary files
rm combined/{c,d}*.png
```
