from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.routers import auth, users

app = FastAPI(title='Título bem massa')

app.include_router(auth.router)
app.include_router(users.router)


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercicio_aula02():
    return """"
    <html>
        <head>
            <title>Exercício Aula 02</title>
        </head>
        <body>
           <h1> Hello World </h1>
           <h2> FastAPI é vida </h2>
        </body>
    </html>"""
