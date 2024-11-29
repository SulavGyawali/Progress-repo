from typer import Typer

app = Typer()


@app.command()
def hello(name: str):
    """Say hello to someone"""
    app.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = True):
    """Say goodbye to someone"""
    if formal:
        app.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        app.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
