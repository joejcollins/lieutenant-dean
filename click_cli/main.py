
"""demo"""
import click
from click_cli.commands import cmd1, cmd2
from typing import Any


@click.group()
def cli() -> Any:
    """My CLI"""
    pass


cli.add_command(cmd1)
cli.add_command(cmd2)
