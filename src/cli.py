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
def split():
    pass

@main.command()
def compress():
    pass

if __name__ == "__main__":
    main()