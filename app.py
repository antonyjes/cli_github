import click
from user_activity import activity

@click.group()
def cli():
    pass

cli.add_command(activity)

if __name__ == '__main__':
    cli()