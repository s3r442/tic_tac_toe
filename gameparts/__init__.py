"""Initialization file for the gameparts package."""

from .parts import Board
from .my_errors import FieldIndexError, CellOccupedError

__all__ = ["Board", "FieldIndexError", "CellOccupedError"]
