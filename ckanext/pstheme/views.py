from flask import Blueprint


pstheme = Blueprint(
    "pstheme", __name__)


def page():
    return "Hello, pstheme!"


pstheme.add_url_rule(
    "/pstheme/page", view_func=page)


def get_blueprints():
    return [pstheme]
