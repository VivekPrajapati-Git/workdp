import re
import pathlib
import click
from PyPDF2 import PdfWriter
from pathlib import Path

def merge(file1 , file2):
    if pathlib.Path.is_file(Path(file1)) and pathlib.Path.is_file(Path(file2)):
        merger = PdfWriter()

        for file in [file1, file2]:
            merger.append(file)

        merger.write("Merged.pdf")
        merger.close()
        click.echo("File Merged Successfully with name Merged.pdf")       
    else:
        if pathlib.Path.is_file(Path(file1)) != True:
            click.echo("File 1 not found")
        else:
            click.echo("File 2 is not found")
        
        