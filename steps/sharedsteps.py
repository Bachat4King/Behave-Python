from behave import step


@step("Go to {url}")
def open_website(context, url):
    context.browser.get(url)


@step('API: set base url to "{url}"')
def set_base_url(context, url):
    context.url = url
