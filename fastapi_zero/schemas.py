from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from fastapi_zero.models import TodoState


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str


class FilterPage(BaseModel):
    limit: int = Field(default=10, ge=0)
    offset: int = Field(default=0, ge=0)


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState = Field(default=TodoState.todo)


class TodoPublic(TodoSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class FilterTodo(FilterPage):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=20,
    )
    description: str | None = Field(
        default=None,
        min_length=10,
        max_length=100,
    )
    state: TodoState | None = Field(
        default=None,
    )


class TodoList(BaseModel):
    todos: list[TodoPublic]


class TodoUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=20,
    )
    description: str | None = Field(
        default=None,
        min_length=10,
        max_length=100,
    )
    state: TodoState | None = Field(
        default=None,
    )
