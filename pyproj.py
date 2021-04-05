import click
import os
from pathlib import Path
from datetime import date

@click.command()
@click.option("-n", "--name", help="Name of your project and its starting file", required=True)
def dir_file_create(name):
    p = Path(f"{name}")
    try:
        p.mkdir()
        click.echo(f"Directory {name} created.")
    except FileExistsError as exc:
        click.echo(f"Directory {name} not created. {exc}")
    else:
        os.chdir(f".\\{name}")
        with open(f"{name}.py", "w") as f:
            f.write(f"# Created on {date.today()}")
        click.echo(f"File {name}.py created.")
        with open("README.md", "w") as f:
            f.write(f"# {name.upper()}")
        click.echo("README.md created.")
        with open (".gitignore", "w") as f:
            f.write("__pycache__/\n*.egg-info/")
        click.echo(".gitignore created.")


if __name__ == "__main__":
    dir_file_create()