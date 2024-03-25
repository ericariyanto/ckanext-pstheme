"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.pstheme.logic import validators


def test_pstheme_reauired_with_valid_value():
    assert validators.pstheme_required("value") == "value"


def test_pstheme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.pstheme_required(None)
