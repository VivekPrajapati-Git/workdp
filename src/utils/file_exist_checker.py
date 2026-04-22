import click
from pathlib import Path

def is_file_exists(files):
    # Iterating over files
    for file in files:
        if Path.is_file(Path(file)) != True: # Checking if the file exist or not
            click.echo(f"File Error : {file} not found")
            return