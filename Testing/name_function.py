def get_foramtted_name(first, last, middle=''):
    """Generated a neatly formatted name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()