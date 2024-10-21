# pre-commit-tool

A simple wrapper around some [pre-commit][] commands that remembers some needed arguments for you,
and that provides some abbreviations and friendly aliases.

[begintoc]: #

## Contents

- [Commands](#commands)
- [Installation](#installation)
- [Contributing](#contributing)
- [References](#references)

[endtoc]: # (Generated by markdown-toc pre-commit hook)


## Commands

- **help** - Print help
- **install** - Install pre-commit hooks using `pre-commit install-hooks ...`
- **run** - Run pre-commit hooks using `pre-commit run-hooks ...`
- **sync** - Sync and garbage-collect pre-commit hooks
- **update** - Update pre-commit hooks using `pre-commit autoupdate ...`
- **upgrade** - Alias for `update`
- **use** - "Use" (install) the pre-commit tool with `uv tool install ...`
- **validate** - Validate the pre-commit config file

Any command can be given with or without a leading `--` (that is, `--help` is the same as `help`).

Most commands take additional arguments that get passed on to `pre-commit`.

Most commands require a '.pre-commit-config.yaml' to be present.


## Installation

Use your favorite way of installing Python packages. It's really easy with [uv][uv-install]):

    uv tool install pre-commit-tool
    uvx pre-commit-tool help

You can also add this package as a development dependency to a `uv`-managed project:

    uv add --dev pre-commit-tool
    uv run pre-commit-tool help


## Contributing

This project uses:

- `uv` for project create/init, dependency management, virtual environment management
- `ruff` for linting and auto-formatting
- `pre-commit` for automatically running linting/formatting/etc. at pre-commit time
- `editorconfig` for setting indent, end-of-line, etc. for many editors/IDEs


## References

- **editorconfig**  ( [Home][editorconfig] | [Config][editorconfig-config] )
- **pre-commit**    ( [Home][pre-commit] | [GitHub][pre-commit-src] | [Config][pre-commit-config] )
- **ruff**          ( [GitHub][ruff-src] | [Documentation][ruff-doc] )
- **uv**            ( [Install][uv-install] | [GitHub][uv-src] | [Documentation][uv-doc] )


 [editorconfig]: https://editorconfig.org/
 [editorconfig-config]: .editorconfig

 [pre-commit]: https://pre-commit.com/
 [pre-commit-src]: https://github.com/pre-commit/pre-commit
 [pre-commit-config]: .pre-commit-config.yaml

 [ruff-src]: https://github.com/astral-sh/ruff
 [ruff-doc]: https://docs.astral.sh/ruff

 [uv-install]: https://docs.astral.sh/uv/getting-started/installation
 [uv-src]: https://github.com/astral-sh/uv
 [uv-doc]: https://docs.astral.sh/uv
