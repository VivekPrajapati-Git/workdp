import re
import pathlib
import click
from PyPDF2 import PdfWriter
from pathlib import Path

def merge(file1 , file2):
    # Checking that both file exist or not
    merger = PdfWriter() # Creating instance of writer

    #appending both the files
    for file in [file1, file2]:
        merger.append(file)

    merger.write("Merged.pdf")
    merger.close()
    click.echo("File Merged Successfully with name Merged.pdf")                