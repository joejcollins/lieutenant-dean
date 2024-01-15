import click


@click.command()
def add() -> None:
    """This is command 2"""
    click.echo("Running command 2")
