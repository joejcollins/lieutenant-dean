
"""demo"""
import click
from click_cli.commands.cmd1 import cmd1
from click_cli.commands.cmd2 import cmd2
from typing import Any


@click.group()
def cli() -> Any:
    """My CLI"""
    pass


cli.add_command(cmd1)
cli.add_command(cmd2)
