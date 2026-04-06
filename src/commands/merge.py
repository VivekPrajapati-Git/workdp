import re
import pathlib
import click
from PyPDF2 import PdfWriter
from pathlib import Path

def merge(file1 , file2):
    # Checking that both file exist or not
    if pathlib.Path.is_file(Path(file1)) and pathlib.Path.is_file(Path(file2)):
        merger = PdfWriter() # Creating instance of writer

        #appending both the files
        for file in [file1, file2]:
            merger.append(file)

        merger.write("Merged.pdf")
        merger.close()
        click.echo("File Merged Successfully with name Merged.pdf")       
    else:
        # If any one file is missing showing error
        if pathlib.Path.is_file(Path(file1)) != True:
            click.echo("Error : File 1 not found")
        else:
            click.echo("Error : File 2 is not found")
        
        