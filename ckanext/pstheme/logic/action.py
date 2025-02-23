import ckan.plugins.toolkit as tk
import ckanext.pstheme.logic.schema as schema


@tk.side_effect_free
def pstheme_get_sum(context, data_dict):
    tk.check_access(
        "pstheme_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.pstheme_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'pstheme_get_sum': pstheme_get_sum,
    }
