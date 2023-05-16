import click
from pkg_process.numbers import add_two_numbers

@click.command()
def add() -> None:
    """This is command 2"""
    click.echo("Running command 2")
