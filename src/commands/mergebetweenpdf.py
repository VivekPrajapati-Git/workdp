import click
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

def mergepdfbetween(values):
    file1 = Path(values[0])
    file2 = Path(values[1])
    page1 = int(values[2])
    page2 = int(values[3])
    writer = PdfWriter()

    file1_input = open(file1,"rb")
    file2_input = open(file2,"rb")

    pages1 = len(PdfReader(file1_input).pages)
    pages2 = len(PdfReader(file2_input).pages)

    writer.append(fileobj=file1_input,pages=(page1,pages1))
    writer.merge(position=2,fileobj=file2_input,pages=(page2,pages2))

    output = open("merger.pdf",'wb')
    writer.write(output)

    writer.close()
    output.close()

    click.echo("File merged Successfully")
    click.echo("File Name : merger.pdf")