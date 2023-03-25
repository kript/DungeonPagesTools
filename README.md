# DungeonPagesTools
Tools for playing and interacting with Dungeon Pages https://www.pnparcade.com/products/dungeon-pages-core-set

## Tools

 * [MergeDungeonPages.py](MergeDungeonPages.py)

## Setup

Setup the virtualenv

```
python3 -mvenv ~/code/venvs/DungeonPages
source ~/code/venvs/DungeonPages/bin/activate
pip install -r requirements.txt
```

## Merge Dungeon Pages

Thanks to BohemianCoast who submitted this [pastbin script](https://pastebin.com/QnMJVXqu) on the ButtonShy Discord.

> This is a script to take the pdf of the excellent print and play game Dungeon Pages and combine characters and dungeons to make mix and match playsheets so you can play them on a tablet. You'll need the game, which you can buy at https://www.pnparcade.com/products/dungeon-pages-core-set

> #importing pdf - put your version of the game here. Your folder should have this script and the game pdf and nothing else because I'm doing everything in place because I don't really understand file handling very well. If you have *both* the core set and the yearlong set then I'd recommend amalgamating the pdfs before you start or amending this script. 

It will take a single PDF of all the Core Set and  Year Long Adventures (up to the first nine weeks)  combined, in a file called  "Dungeon Pages For Combining.pdf", and generate a new set of files in the same directory called "The Adventures of {character} in {dungeon}.png"  which is optimised for an iPad.

