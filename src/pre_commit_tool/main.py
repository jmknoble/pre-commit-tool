import subprocess
import sys

from .simplecli import (
    STATUS_FAILURE,
    STATUS_SUCCESS,
    handle_abbreviated_command,
    handle_ambiguous_command,
    handle_unknown_command,
    print_help,
    simple_cli,
)

TRACE_PREFIX = "+"

HELP_TEXT = """
usage: {prog} [[--]COMMAND]

A simple wrapper around some [pre-commit][] commands that remembers some
needed arguments for you.

Commands:
    help    - Prin this help message
    install - Install pre-commit hooks using 'pre-commit install-hooks ...'
    run     - Run pre-commit hooks using 'pre-commit run-hooks ...'
    sync    - Sync and garbage-collect pre-commit hooks
    update  - Update pre-commit hooks using 'pre-commit autoupdate ...'
    use     - "Use" (install) the pre-commit tool with 'uv tool install ...'
    validate - Validate the pre-commit config file

Most commands require a '.pre-commit-config.yaml' to be present.

 [pre-commit]: https://pre-commit.com/
"""


def _trace(arglist):
    print(" ".join([TRACE_PREFIX] + arglist), file=sys.stderr)


def _run_command(arglist):
    _trace(arglist)
    status = subprocess.call(arglist)  # noqa: S603
    return status


def install_hooks(_prog, _cmd, args):
    status = _run_command(["pre-commit", "install", "-f", "--install-hooks", "-t", "pre-commit"] + args)
    return status


def run_hooks(_prog, _cmd, args):
    def _filter_args(args):
        for arg in ["-a", "--all-files", "-h", "--help", "--files"]:
            if arg in args:
                return args
        return ["--all-files"] + args

    status = _run_command(["pre-commit", "run"] + _filter_args(args))
    return status


def sync_hooks(_prog, _cmd, args):
    status = _run_command(["pre-commit", "install-hooks"] + args)
    if status == STATUS_SUCCESS:
        status = _run_command(["pre-commit", "gc"] + args)
    return status


def update_hooks(_prog, _cmd, args):
    status = _run_command(["pre-commit", "autoupdate"] + args)
    return status


def use_tool(_prog, _cmd, _args):
    status = _run_command(["uv", "tool", "install", "pre-commit"])
    return status


def validate_config(_prog, _cmd, args):
    status = _run_command(["pre-commit", "validate-config"] + args)
    return status


def main():
    (prog, cmd, args) = simple_cli(default_prog="pre-commit-tool.py")

    help_options = {"-h"}
    help_commands = {"help"}
    hook_commands = {
        "install": {"install-hooks"},
        "run": {"run-hooks"},
        "sync": {"sync-hooks"},
        "update": {"update-hooks", "upgrade-hooks"},
    }
    tool_commands = {
        "use": {"use-pre-commit"},
        "validate": {"validate-config"},
    }

    most_commands = set() | help_commands
    for commands_dict in [hook_commands, tool_commands]:
        for _key, command_set in commands_dict.items():
            most_commands |= command_set
    all_help_commands = help_commands | help_options

    (cmd, matching_commands) = handle_abbreviated_command(cmd, most_commands)
    if len(matching_commands) > 1:
        handle_ambiguous_command(cmd, matching_commands)

    status = STATUS_FAILURE
    if cmd in all_help_commands:
        status = print_help(prog, help_text=HELP_TEXT)

    elif cmd in hook_commands["install"]:
        status = install_hooks(prog, cmd, args)
    elif cmd in hook_commands["run"]:
        status = run_hooks(prog, cmd, args)
    elif cmd in hook_commands["sync"]:
        status = sync_hooks(prog, cmd, args)
    elif cmd in hook_commands["update"]:
        status = update_hooks(prog, cmd, args)

    elif cmd in tool_commands["use"]:
        status = use_tool(prog, cmd, args)
    elif cmd in tool_commands["validate"]:
        status = validate_config(prog, cmd, args)

    else:
        handle_unknown_command(cmd)  # raises

    return status


if __name__ == "__main__":
    sys.exit(main())
