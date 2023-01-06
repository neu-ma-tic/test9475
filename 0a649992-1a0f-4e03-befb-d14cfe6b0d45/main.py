from fastapi import FastAPI;
import uvicorn;

app = FastAPI();

app.get('/')
async def hello():
  return await "hello there !"

if __name__ == "__main__":
  uvicorn.run(app, port="3000", host="127.0.0.1");