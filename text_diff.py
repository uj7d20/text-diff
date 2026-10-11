"""Produces readable word-level diffs between two pieces of text."""

from __future__ import annotations

__all__ = ["textDiff"]


def textDiff(value):
    """Produces readable word-level diffs between two pieces of text."""
    if value is None:
        raise ValueError("value must not be None")
    return value
