import dataclasses
import sys

STATUS_SUCCESS = 0
STATUS_FAILURE = 1
STATUS_HELP = 42

SAMPLE_HELP_TEXT = """
usage: {prog} [--]COMMAND [OPTIONS]

Do stuff.

Commands:
    help            - Print this help message
    do-stuff        - Do the thing

Options:
    -q/--quiet      - Be less verbose (default)
    -v/--verbose    - Be more verbose
    --example TEXT  - An example
"""


def simple_cli(args=None, default_prog=None, default_cmd=None, keep_dashes=False):
    if args is None:
        args = sys.argv
    if default_cmd is None:
        default_cmd = "help"

    try:
        prog = args[0]
    except IndexError:
        prog = default_prog

    try:
        cmd = args[1]
        if not keep_dashes and cmd.startswith("--"):
            cmd = cmd[2:]
    except IndexError:
        cmd = default_cmd

    try:
        args = args[2:]
    except IndexError:
        args = []

    return (prog, cmd, args)


def handle_abbreviated_command(cmd, full_commands_iterable):
    matching_commands = []
    for full_command in full_commands_iterable:
        if full_command.startswith(cmd):
            matching_commands.append(full_command)
    if len(matching_commands) == 1:
        cmd = matching_commands[0]
    return (cmd, sorted(matching_commands))


def handle_ambiguous_command(cmd, cmds):
    raise RuntimeError(f"'{cmd}': matches multiple commands: {cmds}")


def handle_unknown_command(cmd):
    raise RuntimeError(f"'{cmd}': unknown command")


def handle_unknown_option(option):
    raise RuntimeError(f"'{option}': unknown option")


def print_help(prog, help_text):
    print(help_text.format(prog=prog))
    return STATUS_HELP


@dataclasses.dataclass
class _SampleCliOptions:
    verbose: bool
    example: str


def _grok_sample_options(_prog, _cmd, args):
    options = _SampleCliOptions(verbose=False)
    i = 0
    while i < len(args):
        option = args[i]
        if option in {"--quiet", "-q"}:
            options.verbose = False
        elif option in {"--verbose", "-v"}:
            options.verbose = True
        elif option in {"--example"}:
            i += 1
            if i < len(args):
                options.example = args[i]
            else:
                raise RuntimeError(f"'{option}': requires an argument")
        else:
            handle_unknown_option(args[i])
        i += 1
    return options


def _sample_main():
    (prog, cmd, args) = simple_cli(default_prog="progname")
    _options = _grok_sample_options(prog, cmd, args)

    help_options = {"-h"}
    help_commands = {"help"}
    action_commands = {"do-stuff"}
    most_commands = help_commands | action_commands
    all_help_commands = help_commands | help_options

    (cmd, matching_commands) = handle_abbreviated_command(cmd, most_commands)
    if len(matching_commands) > 1:
        handle_ambiguous_command(cmd, matching_commands)

    status = STATUS_FAILURE
    if cmd in all_help_commands:
        status = print_help(prog, help_text=SAMPLE_HELP_TEXT)
    elif cmd in action_commands:
        print(f"'{cmd}': doing it now")
        status = STATUS_SUCCESS
    else:
        handle_unknown_command(cmd)  # raises

    return status


# if __name__ == "__main__":
#     sys.exit(_sample_main())
