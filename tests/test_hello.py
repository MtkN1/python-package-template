"""Tests for the hello() function."""

from __future__ import annotations

from python_package_template import hello


def test_hello_returns_expected_message() -> None:
    """hello() returns the expected greeting."""
    assert hello() == "hello, world"
