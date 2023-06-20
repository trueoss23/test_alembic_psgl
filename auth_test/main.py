from fastapi import FastAPI, Depends, HTTPException
from config import get_settings
from auth import AuthHandler
from schemas import AuthDetails, DataPayload
import uvicorn


users = []
auth_handler = AuthHandler()
settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(user['username'] == auth_details.username for user in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.hashed_password)
    users.append({
        'username': auth_details.username,
        'hashed_password': hashed_password
    })
    return


@app.post('/login')
def login(auth_details: AuthDetails, data: DataPayload):
    result_user = None
    for user in users:
        if user['username'] == auth_details.username:
            result_user = user
            break
    if result_user is None or \
            not auth_handler.verify_password(auth_details.hashed_password,
                                             result_user['hashed_password']):
        raise HTTPException(status_code=401,
                            detail='Invalid username or password')
    token = auth_handler.encode_token(result_user['username'], data)
    return {'token': token}


@app.get('/unportected')
def unprotected():
    return {'This is': 'Unprotected'}


@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8002, reload=True)
