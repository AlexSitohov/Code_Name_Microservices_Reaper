from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routers import users, auth

app = FastAPI(title='api_gateway')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


app.include_router(users.router)
app.include_router(auth.router)
