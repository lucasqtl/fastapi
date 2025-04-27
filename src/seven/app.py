from http import HTTPStatus

from fastapi import FastAPI
from sqlalchemy import create_engine

from seven.models import table_registry
from seven.routers import auth, users
from seven.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


engine = create_engine('sqlite:///./database.db', echo=True)
table_registry.metadata.create_all(engine)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'lucas Mundo'}
