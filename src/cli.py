import click

@click.group()
def main():
    pass

@main.command()
@click.option("--file1")
@click.option("--file2")
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