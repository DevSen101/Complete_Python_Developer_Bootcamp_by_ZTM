import PyPDF2

with open(
    "/Python Code/13. Scripting with Python/3. Pdf Playground/dummy.pdf", "rb"
) as file:
    reader = PyPDF2.PdfReader(file)
    # print(len(reader.pages)) #for number of pages
    print(reader.pages[0]) # go to page no.
    # rotate method etc..

