import click
from utils.file_exist_checker import is_file_exists

# Main Command for grouping all the commands
@click.group()
def main():
    pass

# Command to merge 2 pdfs
@main.command(help="Used to merge 2 PDFs")
@click.argument("file1")
@click.argument("file2")
def merge(file1,file2):
    is_file_exists([file1,file2])
    from commands.merge import merge
    merge(file1,file2)

# Command to merge pdf from between pages
@main.command()
@click.argument('file1')
@click.argument('file2')
@click.argument('p1')
@click.argument('p2')
def mbf(file1,file2,p1,p2):
    is_file_exists([file1,file2])
    from commands.mergebetweenpdf import mergepdfbetween
    mergepdfbetween([file1,file2,p1,p2])

# Command used to split pdf files
@main.command()
@click.argument('file')
@click.argument('Page_number')
def split(file,page_number):
    is_file_exists([file])
    from commands.split import splitpdf
    splitpdf(file,page_number)

@main.command()
def compress():
    pass

if __name__ == "__main__":
    main()