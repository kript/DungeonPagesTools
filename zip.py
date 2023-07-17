#!/usr/bin/python3

import zipfile
import re

adventure = "Year-long Adventure_071423.zip"

with zipfile.ZipFile(adventure, mode="r") as archive:
    list = archive.namelist()
    items = archive.infolist()

dungeon = {}
for file in list:
    # ignore the zip artefacts of being created on OSX
    if file.startswith("__MACOSX"):
        continue
    # only get the weekly adventure files, ignore the rules and addendum files
    if "YLA_WK" in file:
        #realfiles.append(file)
        # strip off the extension, then break up the filename
        # the naming isn't consistent, so we need to work backwards
        namearray = file.split(".")[0].split("_")
        adventurer = namearray[-3]
        location = namearray[-2]
        # the filename has Camel Case adventurer names and locations,
        # so make them human readable
        # thanks stack exchange - https://stackoverflow.com/a/2279177
        adventurer_readable = ' '.join(re.sub(r"([A-Z])", r" \1", adventurer).split())
        location_readable =  ' '.join(re.sub( r"([A-Z])", r" \1", location).split())
        # create a dictionary entry for each file
        dungeon[file] = {
            "adventurer": adventurer,
            "adventurers name": adventurer_readable,
            "location": location,
            "location name": location_readable,
            }

""" sample dictionary entry in dungeon:
"DungeonPages_YLA_WK027_FlynnBlackGlove_Meredrin_070623.pdf":
{
    "adventurer": "FlynnBlackGlove",
    "location": "Meredrin"
}
"""

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dungeon)


