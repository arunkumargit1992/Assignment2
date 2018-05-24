from behave import *
import requests


status_code = 0


@given('the API at the URL "{url}"')
def step_impl(context, url):
    context.url = url


@when('I send a GET request')
def step_impl(context):
    r = requests.get(context.url)
    status_code = r


@then('a 200 status code should be returned')
def step_impl(context):
    if status_code == 200:
        print("api called successfully and the status code is 200")
    else:
        print("api call unsuccessful")

