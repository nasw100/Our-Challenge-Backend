import uvicorn
from fastapi import FastAPI
from api.views import v1
from app.settings import setting

def main() :
    app = FastAPI()

    app.mount("/api/v1", v1)

    uvicorn.run(app, host=setting.HOST, port=setting.PORT)

if __name__ == "__main__" :
    main()