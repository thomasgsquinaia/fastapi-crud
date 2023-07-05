from fastapi import FastAPI
import router

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome Librarie"

app.include_router(router.router)

