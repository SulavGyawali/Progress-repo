from typing import Callable, Optional

class Typer:
    def __init__(self) -> None:
        self.commands: dict = {}

    def command(self, func: Optional[Callable] = None) -> Optional[Callable]:
        if func:
            self.commands[func.__name__] = func
            return func
        else:
            return self.command

    def help(self, name: str = None) -> None:
        print("Help")
        if name:
            if name in self.commands:
                if self.commands[name].__doc__:
                    print(f"{name} - {self.commands[name].__doc__}")
                else:
                    print(f"{name}")
            else:
                print(f"Command {name} not found")
        else:
            for command in self.commands.keys():
                if self.commands[command].__doc__:
                    print(f"{command} - {self.commands[command].__doc__}")
                else:
                    print(f"{command}")

    def echo(self, message: str) -> None:
        print(message)

    def __call__(self) -> None:
        import sys

        if len(sys.argv) == 1:
            self.help()
        else:
            command = sys.argv[1]

            if command == "help":
                if len(sys.argv) == 2:
                    self.help()
                else:
                    self.help(sys.argv[2])

            else:

                if command in self.commands:
                    self.commands[command](*sys.argv[2:])
                else:
                    print(f"Command {command} not found")
                    self.help()
