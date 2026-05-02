from importlib.metadata import metadata

from .solver import solve_make10

_package_metadata = metadata(__package__)  # noqa: RUF067
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = ["solve_make10"]
