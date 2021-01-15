
import json
import sys
import os
import typer
from typing import List
import time
from .logger import get_logger
from .config.imports import check_imports

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

logger = get_logger()
cli = typer.Typer()

@cli.command('setup')
def setup_auto():
    chk_libs = ['tensorflow', 'torch', 'transformers']
    typer.echo(f'Setting Up Libraries and Checking Installed')
    installed_libs = check_imports()
    for lib in chk_libs:
        _is_installed = f'{lib} - {installed_libs[lib]} is installed' if installed_libs[lib] else f'{lib} is not not installed'
        typer.echo(_is_installed)
        if typer.confirm(f"Update {lib}?"):
            os.system(f'pip install -q --upgrade {lib}')


if __name__ == "__main__":
    cli()