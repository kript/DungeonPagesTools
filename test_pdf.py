#!/usr/bin/python3
"""
mock up some PDF's for use in later tests
"""
import os
from PIL import Image
import pypdfium2 as pdfium



def merge(image1, image2, pngscale=3):
    """
    merge two images together to make a single image
    pngscale = 3  # this makes it a good sort of size for iPad
    """
    width = max(image1.size[0], image2.size[0])
    height = image1.size[1] + image2.size[1]
    new_image = Image.new("RGBA", (width, height), (255, 255, 255))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, 290 * pngscale))
    return new_image


def create_pdf(merged_image, outputfile):
    """
    create a PDF file for testing
    using the sample images created earlier
    """
    # for some wierd reason pdfium only imports JPG, so convert PNG files
    # open image in png format
    img_png = Image.open(merged_image).convert("RGB")
    filename = os.path.splitext(merged_image)[0]
    merged_image_as_jpg = filename + ".jpg"
    # The image object is used to save the image in jpg format
    img_png.save(merged_image_as_jpg)
    # create new PDF
    pdf = pdfium.PdfDocument.new()
    # new page in PDF
    image = pdfium.PdfImage.new(pdf)
    # bring in the image we just created
    image.load_jpeg(merged_image_as_jpg)
    # do a whole load of stuff to get the image size
    # to put into the PDF that I cargo culted and don't really understand
    width, height = image.get_size()
    matrix = pdfium.PdfMatrix().scale(width, height)
    image.set_matrix(matrix)
    # create new page in PDF
    page = pdf.new_page(width, height)
    page.insert_obj(image)
    page.gen_content()
    pdf.save(outputfile, version=17)  # v17 apparently = PDF 1.7 standard


def main():
    """
    The ability to run this module standalone
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
        dungeonpage = merge(character, dungeonmap)
        temp_png_file = test["testfilename"] + ".png"
        dungeonpage.save(temp_png_file)
        create_pdf(temp_png_file, test["testfilename"] + ".pdf")

    # character = Image.open("./tests/resources/barbarian-g41add6e56_640.png")
    # dungeonmap = Image.open("./tests/resources/map-g83e9296e6_1280.png")
    # dungeonpage = merge(character, dungeonmap)
    # dungeonpage.save("./tests/resources/output.png")
    # create_pdf("./tests/resources/output.png", "output.pdf")


if __name__ == "__main__":
    main()
