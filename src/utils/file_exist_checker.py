import click
from pathlib import Path

# Checking for one file exist or not
def is_file_exist(file_name):
    if Path.is_file(Path(file_name)) != True:
        click.echo(f"File Error : {file_name} not found")
        return        