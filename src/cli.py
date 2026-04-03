import click

@click.group()
def main():
    pass

@main.command()
def merge():
    pass

@main.command()
def split():
    pass

@main.command()
def compress():
    pass

if __name__ == "__main__":
    main()