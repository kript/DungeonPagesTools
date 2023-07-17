#!/usr/bin/env python3

"""
With thanks to BohemianCoast at https://pastebin.com/QnMJVXqu
This is a script to take the pdf of the excellent print and play game Dungeon Pages and combine characters and dungeons to make mix and match playsheets so you can play them on a tablet. You'll need the game, which you can buy at https://www.pnparcade.com/products/dungeon-pages-core-set
"""

from PIL import Image
import pypdfium2 as pdfium
import os

# you need to have libraries Pillow and Pypdfium2 installed. This is tested with Python 3.9.1 , pypdfium2 4.1.0, and pillow something or other

# importing pdf - put your version of the game here. Your folder should have this script and the game pdf and nothing else because I'm doing everything in place because I don't really understand file handling very well. If you have *both* the core set and the yearlong set then I'd recommend amalgamating the pdfs before you start or amending this script.

# if your pdf is called something different, change it below
pdf = pdfium.PdfDocument("Dungeon Pages For Combining.pdf")
n_pages = len(pdf)
pngscale = 3  # this makes it a good sort of size for iPad
# and saving out as separate characters and dungeons
path = 'combined'
os.mkdir(path)
for page_number in range(n_pages):
    page = pdf.get_page(page_number)
    # making the character and dungeon sections

    bitmap = page.render(
        scale=pngscale,
        crop=(0, 500, 0, 0),
    )
    character = bitmap.to_pil()
    character.save(f"combined/c{page_number+1}.png")

    bitmap = page.render(
        scale=pngscale,
        crop=(0, 0, 0, 292),
    )
    dungeon = bitmap.to_pil()
    dungeon.save(f"combined/d{page_number+1}.png")

# creating dungeon pages by mashing them together


def merge(im1, im2):
    w = max(im1.size[0], im2.size[0])
    h = im1.size[1] + im2.size[1]
    im = Image.new("RGBA", (w, h), (255, 255, 255))
    im.paste(im1, (0, 0))
    im.paste(im2, (0, 290 * pngscale))
    return im


# name all the characters and dungeons here for cutely named files. This is the core set and the first nine weeks of the yearlong set. You need to make sure the pages of the PDF are in the same order as this or your names will all come out wrong. If you *only* have the year long set, delete the first six names from each list; they're the core items.

characters = [
    "Zafinn, Wandering Wizard",
    "Gloria, Avenging Warrior",
    "Sygrid, Northern Hunter",
    "Amador, Light Cleric",
    "Mira, Haunted Ranger",
    "Flynn, White Glove Knight",
    "Amador, Steam Cleric",
    "Sygrid, Vengeful Hunter",
    "Gloria, Virtuous Warrior",
    "Drok, Outcast Troll",
    "Mira, Brush Ranger",
    "Zafinn, Mischievous Wizard",
    "Flynn, Red Glove Knight",
    "Krete & Kreeg, Renowned Bards",
    "Amador, Woodward Cleric",
    "Zafinn, Elemental Wizard",
    "Sygrid, Banished Hunter",
    "Gloria, Daredevil Warrior",
    "Valensi, Abyss Whisper",
    "Mira, Lawless Ranger",
    "Flynn, Blue Glove Knight",
    "Drok, Adventurous Troll",
    "Krete & Kreeg, Questing Bards",
    "Zafinn, Brash Wizard",
    "Hardos, Valiant Monk",
    "Valensi, Spirit Whisper",
    "Sygrid, Orphaned Hunter",
    "Amador, Martial Cleric",
    "Gloria, Night Warrior",
    "Marian, Devious Spirit",
    "Mira, Sky Ranger",
    "Krete And Kreeg, Notorious Bards",
]
dungeons = [
    "Highmount Village",
    "Hellenburg",
    "Cliffdrop City",
    "Thorne Valley",
    "Reachport",
    "The Iron Peaks",
    "Havington",
    "Hogglebottom",
    "Whittleberry",
    "Bordertown",
    "Abyssal Plane",
    "Shan Tomb",
    "Capital City",
    "Stormshield",
    "The Hungry Isles",
    "Bakorio Province",
    "Lariss",
    "Filgan Forest",
    "Tearburn Fields",
    "Sunset Quarter",
    "Aquira",
    "Chundar Village",
    "Belgor Mountain",
    "Thatchwood",
    "Alglen",
    "Greatbridge",
    "Dowlor",
    "Eldrin",
    "The Coils",
    "Puffbag Town",
    "Tunnels of Dreadmarsh",
    "Crescent City",
]

# make all the pages

for ii in range(n_pages):
    for jj in range(n_pages):
        im1 = Image.open(f"combined/c{ii+1}.png")
        im2 = Image.open(f"combined/d{jj+1}.png")

        dungeonpage = merge(im1, im2)
        character = characters[ii]
        dungeon = dungeons[jj]
        dungeonpage.save(f"combined/The Adventures of {character} in {dungeon}.png")
