
"""demo"""
import click
from click_cli.commands.cmd1 import cmd1
from typing import Any


@click.group()
def cli() -> Any:
    """My CLI"""
    pass


cli.add_command(cmd1)

@click.command()
@click.option('--count', default=1, help='number of greetings')
def cmd2():
    """This is command 2"""
    click.echo("Running command 2")