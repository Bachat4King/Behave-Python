from behave import step
from utils.utils import *
import re

@step('visualize this horizontal table')
def step_impl(context):
    """
    :param context:
    :return: list of horizontal table rows
    """
    print(return_horizontal_table(context))


@step('visualize this list of dictionaries')
def step_impl(context):
    """
        return list of table rows dicts

        [{'Head1': 'Cell1_1', 'Head2': 'Cell1_2'},
         {'Head1': 'Cell2_1', 'Head2': 'Cell2_2'}]
        """
    print(list_of_dictionaries(context))


@step('Visualize this table')
def step_impl(context):
    """
    return flat dict from first 2 columns

    {'Head1': 'Head2',
     'Cell1': 'Cell2',
     ...}
    """

    print(table_to_flat_dict(context))


@step('visualize the raw text')
def visualize_text(context):
    """
    :param context:
    :return: text in step
    """
    print(context.text)
    return context.text


@step('visualize the scenario name')
def visualize_scenario_name(context):
    """
    :param context:
    :return: scenario name
    """
    print(context.scenario.name)
    return context.scenario.name


@step('visualize the feature name')
def visualize_feature_name(context):
    """
    :param context:
    :return: feature name
    """
    print(context.feature.name)
    return context.feature.name


@step('visualize the feature filename')
def visualize_feature_filename(context):
    """
    :param context:
    :return: feature filename
    """
    print(context.feature.filename)
    return context.feature.filename


@step('visualize the tags')
def visualize_tags(context):
    """
    :param context:
    :return: tags
    """
    print(context.feature.tags)
    return context.feature.tags


@step('print {to_print} as a context variable')
def print_context_var(context, to_print):
    print(to_print)
    context.name = "Bastian"
    # verify if an strings matches format: {{var_name}} using regex
    if re.match(r"\{\{(.*)\}\}", to_print):
        to_print = to_print.replace("{{", "").replace("}}", "")
        print(eval(to_print))