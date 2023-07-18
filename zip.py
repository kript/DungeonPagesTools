#!/usr/bin/python3

import zipfile
import re

def adventure_zip_file_info(adventurefile):
    """
    Get the list of files in an Year Long Adventure zip
    return a dictionary with the information.

    sample dictionary entry in dungeon:
    'DungeonPages_YLA_WK_08_KreteKreeg_Stormshield_022323.pdf':
    {
        'adventurer': 'KreteKreeg',
        'adventurers name': 'Krete '
        'Kreeg',
        location': 'Stormshield',
        location name': 'Stormshield'
    },
    """
    with zipfile.ZipFile(adventurefile, mode="r") as archive:
        list = archive.namelist()
        #items = archive.infolist()
    dungeon = {}
    for file in list:
        # ignore the zip artefacts of being created on OSX
        if file.startswith("__MACOSX"):
            continue
        # only get the weekly adventure files, ignore the rules and addendum files
        if "YLA_WK" in file:
            # strip off the extension, then break up the filename
            # the naming isn't consistent, so we need to work backwards
            namearray = file.split(".")[0].split("_")
            adventurer = namearray[-3]
            location = namearray[-2]
            # the filename has Camel Case adventurer names and locations,
            # so make them human readable
            # thanks to stack exchange for the regex- https://stackoverflow.com/a/2279177
            adventurer_readable = re.sub(r"([A-Z])", r" \1", adventurer).lstrip()
            location_readable =  re.sub(r"([A-Z])", r" \1", location).lstrip()
            # create a dictionary entry for each file
            dungeon[file] = {
                "adventurer": adventurer,
                "adventurers name": adventurer_readable,
                "location": location,
                "location name": location_readable,
                }
    return(dungeon)

def main():
    """
    for future unit tests, the ability to run this module standalone
    """
    adventure = "Year-long Adventure_071423.zip"
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    dungeon = adventure_zip_file_info(adventure)
    pp.pprint(dungeon)

if __name__ == "__main__":
    main()
