from PyPDF2 import PdfMerger
import sys
import os


def pdf_merger(pdf_list):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write("merged.pdf")
    merger.close()


if __name__ == "__main__":
    inputs = sys.argv[1:]
    pdf_merger(inputs)
