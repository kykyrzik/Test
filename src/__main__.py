from fastapi import FastAPI
import uvicorn
from src.api.v1.user import user_router

app = FastAPI()

app.include_router(user_router)


def main() -> None:
    uvicorn.run("__main__:app", host='127.0.0.1', port=8000)


if __name__ == "__main__":
    main()