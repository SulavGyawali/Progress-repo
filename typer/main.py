from typer import Typer

app = Typer()

@app.command(default = True ,aliases = ["hi", "hey"])
def hello(name: str = None):
    """
    Say hello to someone
    Args:
        name (str): The name of the person
    """
    if name is None:
        app.echo("Hello There!")
    else:
        app.echo(f"Hello {name}")


@app.command()
def goodbye(name: str = None, formal: bool = False, test : bool = False):
    """
    Say goodbye to someone
    Args:
        name (str): The name of the person
        formal (bool): Use the formal goodbye (default = False, use --formal flag)
    """
    if name:
        if formal:
            app.echo(f"Goodbye Ms. {name}. Have a good day.")
        else:
            app.echo(f"Bye {name}!")
    else:
        app.echo("Goodbye!")


if __name__ == "__main__":
    app()
