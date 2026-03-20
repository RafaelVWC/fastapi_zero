import asyncio
import sys
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.routers import auth, todos, users

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title='Título bem massa')

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get(
    '/exercicio-html', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
async def exercicio_aula02():
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


@app.get('/')
async def read_root():
    return {'message': 'Hello World!'}
