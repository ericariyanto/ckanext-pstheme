"""Tests for helpers.py."""

import ckanext.pstheme.helpers as helpers


def test_pstheme_hello():
    assert helpers.pstheme_hello() == "Hello, pstheme!"
