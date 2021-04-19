import flask_unittest

from app import create_app


def test_home_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')

        assert response.status_code == 200
        assert b"Server is running!" in response.data


def test_store_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/store')

        assert response.status_code == 200
        assert b"Item Store" in response.data
        assert b"Name" in response.data
        assert b"Price" in response.data
        assert b"Quantity" in response.data


def test_get_basket_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/basket')

        assert response.status_code == 200
        assert b"Basket" in response.data
        assert b"Total" in response.data


def test_post_basket_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.post('/basket')

        assert response.status_code == 200
        assert b"Invalid category" in response.data


def test_purchase_action():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/purchase')

        assert response.status_code == 302
        assert b"Redirecting" in response.data
