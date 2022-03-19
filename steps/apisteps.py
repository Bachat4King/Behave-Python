from behave import step
import httpx


@step('API: send {request_type} request to "{endpoint}"')
def send_request(context, request_type, endpoint):
    """
    :param context:
    :param request_type:
    :param endpoint:
    sends a request to an endpoint
    """

    url = context.url + endpoint

    context.payload = {}
    context.headers = {"Content-Type": "application/json"}

    if request_type.lower() == "get":
        context.response = httpx.get(url,
                                     params=context.payload,
                                     headers=context.headers)
    elif request_type.lower() == "post":
        context.response = httpx.post(url,
                                      data=context.payload,
                                      headers=context.headers)
    elif request_type.lower() == "put":
        context.response = httpx.put(url,
                                     data=context.payload,
                                     headers=context.headers)
    elif request_type.lower() == "delete":
        context.response = httpx.delete(url,
                                        headers=context.headers)


@step('API: status code should be "{status_code}"')
def verify_status_code(context, status_code):
    """
    :param context:
    :param status_code:
    :verify: status code matches
    """
    assert context.response.status_code == int(status_code), \
        f"status code expected: {status_code}, but got {context.response.status_code}"


@step('API: Set headers')
def set_headers(context):
    result = {context.table.headings[0]: context.table.headings[1]}
    for row in context.table.rows:
        result[row.cells[0]] = row.cells[1]

    context.headers = result


@step('API: set payload')
def set_payload(context):
    for row in context.table:
        dictionary = dict(row.items())

    context.payload = dictionary


@step('API: response text should include {text}')
def verify_text_in_response(context, text):
    assert text in context.response.text, f"{text} is not in {context.response.text}"
