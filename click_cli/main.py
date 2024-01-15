"""demo"""
from typing import Any

import click

from click_cli.commands.cmd2 import cmd2


@click.group()
def cli() -> Any:
    """My CLI"""
    pass


cli.add_command(cmd1)
cli.add_command(cmd2)
