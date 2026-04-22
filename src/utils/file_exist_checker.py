import click
from pathlib import Path

def is_file_exists(files):
    for file in files:
        if Path.is_file(Path(file)) != True:
            click.echo(f"File Error : {file} not found")
            return