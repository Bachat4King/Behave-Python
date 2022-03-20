from behave import step
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


@step('demoqa: slide the bar to "{percent}" percent')
def move_slide_bar(context, percent):
    actions = ActionChains(context.browser)
    slider = context.browser.find_element(By.XPATH, "//input[@type='range']")
    actions.drag_and_drop_by_offset(slider, 0.2, 0).perform()
    sleep(2)


@step('demoqa: sort the list reversed')
def sort_the_list(context):
    actions = ActionChains(context.browser)
    sortable_list = context.browser.find_elements(By.XPATH, "//div[@class='vertical-list-container mt-4']/div")
    aux = 1
    aux2 = 2
    if len(sortable_list) % 2 == 0:
        for i in range(len(sortable_list) // 2):
            actions.drag_and_drop(sortable_list[i], sortable_list[i - aux]).perform()
            actions.drag_and_drop(sortable_list[i - aux2], sortable_list[i]).perform()
            aux += 2
            aux2 += 2
