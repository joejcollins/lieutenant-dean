import click


@click.command()
def cmd2() -> None:
    """This is command 2"""
    click.echo("Running command 2")
