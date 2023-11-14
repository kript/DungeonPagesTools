#!/usr/bin/python3
"""
test creation of PDF's
"""
import os
from PIL import Image
import pypdfium2 as pdfium
import CreateTestPDF


def test_pdf_creation():
    """
    pytest check that PDF creation continues to work
    so tests my usage of following modules:
        PIL
        Pydium
    """
    test_dungeons = [
        {
            "testfilename": "DungeonPages_YLA_WK_01_ThrudBarbarian_GreeMap_072923",
            "character": "./tests/resources/barbarian-g41add6e56_640.png",
            "adventure": "./tests/resources/map-g83e9296e6_1280.png",
        },
        {
            "testfilename": "DungeonPages_YLA_WK_02_SkullNecromancer_BlueMap_072923",
            "character": "./tests/resources/skull-g9a09fd25d_640.png",
            "adventure": "./tests/resources/graph-gf842b4b92_1280.png",
        },
    ]
    for test in test_dungeons:
        character = Image.open(test["character"])
        dungeonmap = Image.open(test["adventure"])
        dungeonpage = CreateTestPDF.merge(character, dungeonmap)
        temp_png_file = test["testfilename"] + ".png"
        dungeonpage.save(temp_png_file)
        CreateTestPDF.create_pdf(temp_png_file, test["testfilename"] + ".pdf")
