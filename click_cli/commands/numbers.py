"""Command 1 module."""
import click


@click.command()
def cmd1():
    """Demo command 1."""
    click.echo("Running command 1")
