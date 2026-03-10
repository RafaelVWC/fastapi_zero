from http import HTTPStatus


def test_root_deve_retornar_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_root_deve_retornar_hello_world_HTML(client):

    response = client.get('/exercicio-html')

    assert '<h1> Hello World </h1>' in response.text
    assert response.status_code == HTTPStatus.OK
