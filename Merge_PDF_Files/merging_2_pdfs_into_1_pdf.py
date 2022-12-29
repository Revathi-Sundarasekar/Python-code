from PyPDF2 import PdfFileMerger


# By appending in the end

def by_appending():
    merger = PdfFileMerger()
    # Either provide file stream
    f1 = open("Sample_PDF_file_1.pdf", "rb")
    merger.append(f1)
    # Or direct file path
    merger.append("Sample_PDF_file_2.pdf")

    merger.write("Merged_PDF_file_1.pdf")


# By inserting at after an specified page no

def by_inserting():
    merger = PdfFileMerger()
    merger.append("Sample_PDF_file_1.pdf")
    merger.merge(0, "Sample_PDF_file_2.pdf")
    merger.write("Merged_PDF_file_2.pdf")


if __name__ == "__main__":
    by_appending()
    by_inserting()
