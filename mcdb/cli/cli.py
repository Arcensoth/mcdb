import click


@click.group()
@click.option('-v', '--version', multiple=True,
              help='Which version(s) to use for the query. (repeatable)')
def cli(**kwargs):
    """ Minecraft data query program for commands, NBT, blockstates, and more. Inspired by the in-game help command and
    auto-completion, with added features like multiple version support and expandable regex search. """
    click.echo('kwargs from version(): {}'.format(kwargs))


@cli.command()
@click.option('-c', '--capacity', default=8,
              help='Maximum number of subcommands to render before collapsing.')
@click.option('-e', '--explode', is_flag=True,
              help='Whether to expand all subcommands, regardless of capacity.')
@click.option('-t', '--showtypes', is_flag=True,
              help='whether to show argument types')
@click.argument('command', nargs=-1)
def command(**kwargs):
    """ Query game commands. """
    # TODO query commands.json
    click.echo('kwargs from command(): {}'.format(kwargs))


@cli.command()
@click.argument('block', nargs=-1)
def block(**kwargs):
    """ Query blocks. """
    # TODO query blocks.json
    click.echo('kwargs from block(): {}'.format(kwargs))


cli()
