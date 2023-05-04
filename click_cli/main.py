
"""demo"""
import click
import click_shit
from click_shit.commands import cmd1, cmd2
from typing import Any


@click.group()
def cli() -> Any:
    """My CLI"""
    pass


cli.add_command(cmd1)
cli.add_command(cmd2)
