"""Demo click command 2."""
import click


@click.command()
def add() -> None:
    """Add command 2."""
    click.echo("Running command 2")
