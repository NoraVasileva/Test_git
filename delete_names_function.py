def delete_names(name, list_name):
    """Delete names from a list"""
    if name in list_name:
        list_name.remove(name)
    else:
        print("This name doesn't exist.")
