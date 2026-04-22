import click

# Main Command for grouping all the commands
@click.group()
def main():
    pass

# Command to merge 2 pdfs
@main.command(help="Used to merge 2 PDFs")
@click.option("--file1",help="Path for first file")
@click.option("--file2", help = "Path for second")
def merge(file1,file2):
    from commands.merge import merge
    merge(file1,file2)

@main.command()
@click.argument('file1')
@click.argument('file2')
@click.argument('p1')
@click.argument('p2')
def mbf(file1,file2,p1,p2):
    from commands.mergebetweenpdf import mergepdfbetween
    mergepdfbetween([file1,file2,p1,p2])

@main.command()
@click.argument('file')
@click.argument('Page_number')
def split(file,page_number):
    from commands.split import splitpdf
    splitpdf(file,page_number)

@main.command()
def compress():
    pass

if __name__ == "__main__":
    main()