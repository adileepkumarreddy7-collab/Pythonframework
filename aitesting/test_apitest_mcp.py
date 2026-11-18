import json

from playwright.sync_api import Playwright


def test_get_fake_store_product(playwright: Playwright) -> None:
    endpoint = "https://fakestoreapi.com/products/1"
    request_context = playwright.request.new_context()

    try:
        response = request_context.get(endpoint)
        response_body = response.text()
        print(response_body)

        assert response.status == 200

        product = json.loads(response_body)
        required_keys = {"id", "title", "price", "category", "description"}
        assert required_keys.issubset(product.keys())
        assert product["id"] == 1
        assert product["price"] == 109.95
        assert product["category"] == "men's clothing"
    finally:
        request_context.dispose()
