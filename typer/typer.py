from typing import Callable, get_type_hints
import inspect
import sys

class Typer:
    def __init__(self) -> None:
        self.commands: dict = {}

    def command(self, func: Callable) -> Callable:
        """Register a command"""
        self.commands[func.__name__] = func

        return func

    def help(self, name: str = None) -> None:
        print("Help")
        if name:
            if name in self.commands:
                if self.commands[name].__doc__:
                    print(f"{name} : {self.commands[name].__doc__}")
                else:
                    print(f"{name}")
            else:
                print(f"Command {name} not found")
        else:
            for command in self.commands.keys():
                if self.commands[command].__doc__:
                    print(f"{command} : {self.commands[command].__doc__}")
                else:
                    print(f"{command}")

    def echo(self, message: str) -> None:
        print(message)

    def parse_args(self, func: Callable, args: list) -> dict:
        """Parse CLI arguments."""
        sig = inspect.signature(func)
        hints = get_type_hints(func)
        params = sig.parameters

        boolean_flags = {
            f"--{name}": name
            for name, _ in params.items()
            if hints.get(name) == bool
        }

        parsed_args = {name: param.default for name, param in params.items()}

        i = 0
        while i < len(args):
            arg = args[i]
            if arg in boolean_flags:
                parsed_args[boolean_flags[arg]] = True
            else:
                for name, param in params.items():
                    if parsed_args[name] == param.default:
                        parsed_args[name] = hints.get(name, str)(arg)
                        break

            i += 1
        print(parsed_args)
        return parsed_args

    def __call__(self) -> None:
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
                if "--help" in sys.argv[2:]:
                    self.help(command)
                else:
                    if command in self.commands:
                        func = self.commands[command]
                        args = sys.argv[2:]
                        try: 
                            parsed_args = self.parse_args(func, args)
                            func(**parsed_args)
                        except TypeError as e:
                            print(f"Error: {e}")
                            self.help(command)
                    else:
                        print(f"Command {command} not found")
                        self.help()
