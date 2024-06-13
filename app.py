from routes import v1

import logging
import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()

PORT = os.getenv('PORT', '8080')
HOST = os.getenv('HOST', '0.0.0.0')

app = FastAPI()

v1.init_app(app)

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=int(PORT), reload=True, workers=3)
