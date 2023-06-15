from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from config import get_settings

settings = get_settings()


app = FastAPI()


class Token(BaseModel):
    authjwt_secret_key: str = settings.app_secret_key


@AuthJWT.load_config
def get_conf():
    return Token()


class User(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'igor',
                'password': 'qwe',
            }
        }


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            'username': 'igor',
            'password': 'qwe',
        }


users = []


@app.get('/users', response_model=list[User])
def get_users():
    return users


@app.post('/signup', status_code=201)
def create_user(user: User):
    new_user = {
        'username': user.username,
        'password': user.password,
    }

    users.append(new_user)
    return new_user


@app.post('/login')
def login(user: UserLogin, Autorize: AuthJWT = Depends()):
    for u in users:
        if user.username == u['username'] and \
           user.password == u['password']:
            access_token = Autorize.create_access_token(
                subject=user.username
            )
            return {'access_token': access_token}

    raise HTTPException(status_code=401,
                        detail='Invalid username or password')


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
