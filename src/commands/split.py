from PyPDF2 import PdfReader,PdfWriter

def splitpdf(input_file,split_page_number):
    reader = PdfReader(input_file)

    total_pages = len(reader.pages)

    writer1 = PdfWriter()
    writer2 = PdfWriter()

    for i in range(int(split_page_number)):
        writer1.add_page(reader.pages[i])

    for i in range(int(split_page_number),total_pages):
        writer2.add_page(reader.pages[i])

    with open("part1_output.pdf","wb") as f1:
        writer1.write(f1)

    with open("part2_output.pdf","wb") as f2:
        writer2.write(f2)