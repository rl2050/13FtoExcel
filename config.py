
#PDF file name with the list of the SEC 13F securities.
pdfName = '13flist2022q3.pdf'

#Where to start reading the PDF file (first page with the 13f securities)
#page 0 is the first page of the PDF file.
startPageNumber = 2

# PDF table settings
pdfSettings = {
    "vertical_strategy": "explicit",
    "explicit_vertical_lines": [70, 147, 160 , 345, 460, 520],
    "horizontal_strategy": "text",
    "intersection_x_tolerance": 15
}

