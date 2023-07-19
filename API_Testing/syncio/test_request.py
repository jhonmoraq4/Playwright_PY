
#Extracted from: https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-get

from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page , APIRequestContext, expect

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright,) -> Generator [APIRequestContext, None, None]:
       
    request_context = playwright.request.new_context(base_url = "https://reqres.in/api/")
    yield request_context
    request_context.dispose()

    
def test_post_todo(api_request_context: APIRequestContext) -> None:

    data = {
    "name": "morpheus",
    "job": "leader",
    "id": "130",
    "createdAt": "2023-07-18T13:44:53.144Z"
    }
    new_request = api_request_context.post("users/" ,data=data)
    assert new_request.ok

    todos_response = new_request.json()

    print("")
    print(f"la respuesta es: {new_request}")
    print(f"la respuesta total es: {todos_response}")