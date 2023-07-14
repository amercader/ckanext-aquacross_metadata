from ckan.plugins import toolkit


@toolkit.chained_action
def organization_list(up_func, context, data_dict):

    data = up_func(context, data_dict)

    for i in range(len(data)):
        if isinstance(data[i], dict):
            # all_fields = True
            name = data[i].get("name")
        else:
            name = data[i]
        if name == "qc":
            del data[i]
            break
    return data
