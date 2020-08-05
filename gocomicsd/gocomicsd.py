import datetime
import os

import typer
from halo import Halo

from gocomicsd.helpers import get_titles

dt_now = datetime.datetime.now().strftime("%Y-%m-%d")
cli = typer.Typer(help="Download comic strips from gocomics.com.")


@cli.command()
@Halo(text='Getting titles from gocomics.com', spinner='dots')
def titles(search: str = typer.Option(None, help='Search for comics by name.')):
    """List all available comics from gocomics.com."""

    typer.echo(get_titles(search))


@cli.command()
def save(
        name: str,
        from_date: str = typer.Option(dt_now, help='Download comics by name from date YYYY-MM-DD.'),
        to_date: str = typer.Option(dt_now, help='Download comics by name to date YYYY-MM-DD.'),
        path: str = typer.Option(os.getcwd(), help='Download comics to path.')
):
    """Download comic strips by name. This automatically creates a folder by name
    and subfolders by year and month. If options for from and to date are not passed,
    this downloads today's comic."""

    # TODO: Download gif
    typer.echo(name)
    typer.echo(from_date)
    typer.echo(to_date)
    typer.echo(path)
