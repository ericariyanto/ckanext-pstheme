import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def pstheme_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "pstheme_get_sum": pstheme_get_sum,
    }
