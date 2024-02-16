from fastapi import FastAPI
import uvicorn


from src.api.v1.user import user_router
from src.api.v1.auth import login_router
from src.api.v1.ref import ref_router

app = FastAPI()

app.include_router(user_router)
app.include_router(login_router)
app.include_router(ref_router)


def main() -> None:
    uvicorn.run("__main__:app", host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
