from http import HTTPStatus


def test_root_deve_retornar_hello_world_HTML(client):

    response = client.get('/')

    assert '<h1> Hello World </h1>' in response.text
    assert response.status_code == HTTPStatus.OK
