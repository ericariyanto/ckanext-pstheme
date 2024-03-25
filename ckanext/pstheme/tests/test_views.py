"""Tests for views.py."""

import pytest

import ckanext.pstheme.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "pstheme")
@pytest.mark.usefixtures("with_plugins")
def test_pstheme_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("pstheme.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, pstheme!"
