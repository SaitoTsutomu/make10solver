from importlib.metadata import metadata

from .solver import solve_make10

_package_metadata = metadata(__package__)  # ruff: ignore[non-empty-init-module]
__version__ = _package_metadata["Version"]
__author__ = _package_metadata.get("Author-email", "")

__all__ = ["solve_make10"]
