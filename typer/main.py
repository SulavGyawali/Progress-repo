from typer import Typer

app = Typer()

@app.command
def hello(name: str):
    """
    Say hello to someone
    Args:
        name (str): The name of the person
    """
    app.echo(f"Hello {name}")


@app.command
def goodbye(name: str, formal: bool = False, test : bool = False):
    """
    Say goodbye to someone
    Args:
        name (str): The name of the person
        formal (bool): Use the formal goodbye (default = False, use --formal flag)
    """
    if formal:
        app.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        app.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
