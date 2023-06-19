from fastapi import FastAPI
import psycopg2
import uvicorn

from config import get_settings

settings = get_settings()
app = FastAPI(settings.app_name)


@app.get("/")
async def root():
    conn = psycopg2.connect(
        host=settings.db_host,
        database=settings.db_name,
        user=settings.db_user,
        password=settings.db_pass,
        port=settings.db_port,
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8002, reload=True)
