from behave import step
from selenium.webdriver.common.by import By
from time import sleep


@step('Enter {search_term} in search field and click search button')
def put_search_value(context, search_term):
    print(search_term)
    context.browser.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(search_term)
    context.browser.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()


@step('select the first product that has {product_name} in its name')
def select_product_by_name(context, product_name):
    products = context.browser.find_elements(By.XPATH, "//div[contains(@class, 'title-instructions')]/h2//span")
    products_texts = [product.text for product in products]
    index = -2
    for product in products_texts:
        if product_name in product:
            index = products_texts.index(product)
            break
    if index == -2:
        print(f"product with {product_name} doesn't exists")
    else:
        print(products_texts[index])
        products[index].click()


@step('retrieve the price of the product')
def retrieve_price(context):
    price = context.browser.find_element(By.XPATH, "(//div[contains(@id,'corePrice')]//span[@class='a-offscreen'])[2]")
    print(price.text)


@step('add the product to the cart')
def add_to_cart(context):
    cart_button = context.browser.find_element(By.ID, "add-to-cart-button")
    cart_button.click()


@step('"{text}" text is in the page')
def verify_text_in_page(context, text):
    sleep(2)
    element = context.browser.find_element(By.XPATH, "//span[contains(text(), 'Added to Cart')]")
    assert text == element.text, f"{text} is not in the page"
