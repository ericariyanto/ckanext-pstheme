import click


@click.group(short_help="pstheme CLI.")
def pstheme():
    """PS Theme Extension Command.
    """
    pass


@pstheme.command()
@click.argument("name", default="pstheme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [pstheme]
