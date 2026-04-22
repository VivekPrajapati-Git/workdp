from PyPDF2 import PdfReader,PdfWriter

def splitpdf(input_file,split_page_number):
    reader = PdfReader(input_file) # Reading the pdf

    total_pages = len(reader.pages) # Getting the total no. of pages in pdf

    writer1 = PdfWriter() # Creating two instance for writing two pdfs
    writer2 = PdfWriter()

    # Writing in first instance
    for i in range(int(split_page_number)):
        writer1.add_page(reader.pages[i])

    # Writing in second instance
    for i in range(int(split_page_number),total_pages):
        writer2.add_page(reader.pages[i])

    with open("part1_output.pdf","wb") as f1:
        writer1.write(f1)

    with open("part2_output.pdf","wb") as f2:
        writer2.write(f2)