# python-project

Minimal template repo for Python 3.x projects using `uv`

Uses:

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
