def return_horizontal_table(context):
    """
    :param context:
    :return: list of horizontal table rows
    """
    for row in context.table:
        dictionary = dict(row.items())
        return dictionary


def list_of_dictionaries(context):
    """
        return list of table rows dicts

        [{'Head1': 'Cell1_1', 'Head2': 'Cell1_2'},
         {'Head1': 'Cell2_1', 'Head2': 'Cell2_2'}]
        """
    result = []
    for row in context.table:
        result.append(dict(row.items()))
    return result


def table_to_flat_dict(context):
    """
    return flat dict from first 2 columns

    {'Head1': 'Head2',
     'Cell1': 'Cell2',
     ...}
    """

    if len(context.table.headings) < 2:
        raise ValueError('Too few columns to construct flat dictionary. Expected 2')
    result = {context.table.headings[0]: context.table.headings[1]}
    for row in context.table.rows:
        result[row.cells[0]] = row.cells[1]
    return result
