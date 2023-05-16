from fastapi import FastAPI
from routes.user import router as user_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)


app.include_router(user_routes)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=5000)
