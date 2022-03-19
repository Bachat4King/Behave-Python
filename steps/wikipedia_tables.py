from behave import step
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('get the table as a dataframe')
def get_table_as_dataframe(context):
    df = pd.read_html("https://es.wikipedia.org/wiki/Anexo:Comunas_de_Santiago_de_Chile")[1]
    context.df = df.dropna().drop_duplicates()


@step('print the dataframe')
def print_dataframe(context):
    print(context.df.head().to_string())


@step('get the table')
def get_table(context):
    tables = WebDriverWait(context.browser, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))
    target_table = tables[3]
    headers = target_table.find_elements_by_tag_name("th")
    headers_list = [header.text for header in headers]
    rows = target_table.find_elements_by_tag_name("tr")
    rows_list = []
    for row in rows:
        columns = row.find_elements_by_tag_name("td")
        columns_list = [column.text for column in columns]
        rows_list.append(columns_list)
    df = pd.DataFrame(rows_list, columns=headers_list)
    print(df.head(10).dropna().to_string())


