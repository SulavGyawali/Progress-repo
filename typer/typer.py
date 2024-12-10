from typing import Callable, get_type_hints
import inspect
import sys

class Typer:
    def __init__(self) -> None:
        self.commands: dict = {}
        self.dry_run = False

    def command(self, **options):
        """Decorator to add a new command to the CLI."""
        def wrapper(func):
            name = options.get("name", func.__name__)
            self.commands[name] = func

            if options.get("aliases"):
                for alias in options.get("aliases"):
                    self.commands[alias] = func

            if options.get("default", False):
                self.default_command = func
            return func
        return wrapper

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

        if "--dry-run" in args:
            self.dry_run = True
            args.remove("--dry-run")

        parsed_args = {name: param.default for name, param in params.items()}

        i = 0
        while i < len(args):
            arg = args[i]
            if arg in boolean_flags:
                parsed_args[boolean_flags[arg]] = True
            else:
                for name, param in params.items():
                    if param.annotation != bool:
                        if parsed_args[name] == param.default:
                            parsed_args[name] = hints.get(name, str)(arg)
                            break

            i += 1
        return parsed_args
    
    def check_params(self, func: Callable, args: list) -> None:
        sig = inspect.signature(func)
        params = sig.parameters
        for name, param in params.items():
            if name in args:
                if not isinstance(args[name], param.annotation) and param.default is not None:
                    self.raise_error(f"Parameter {name} should be of type {param.annotation}")
            else:
                if param.default == param.empty:
                    if name not in args:
                        self.raise_error(f"Parameter {name} is required")
                else:
                    if name not in args:
                        args[name] = param.default
            
                
    def raise_error(self, message: str) -> None:
        self.echo(f"Error: {message}")
        self.help()
        sys.exit(1)
    
    def dry_run_func(self, func: Callable, args: dict) -> None:
        self.echo(f"Running {func.__name__} with args {args}")


    def __call__(self) -> None:
        if len(sys.argv) == 1:
            try:
                self.check_params(self.default_command, {})
                self.default_command()
            except AttributeError:
                print("No default command found")
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
                            self.check_params(func, parsed_args)
                            if self.dry_run:
                                self.dry_run_func(func, parsed_args)
                            else:
                                func(**parsed_args)
                        except TypeError as e:
                            print(f"Error: {e}")
                            self.help(command)
                    else:
                        print(f"Command {command} not found")
                        self.help()
