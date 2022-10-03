from fastapi import FastAPI, File, Request
from fastapi.responses import FileResponse


app = FastAPI()

@app.post("/")
def root(request: Request, file: bytes = File()):
    print("Request Headers: ", request.headers)
    return FileResponse('./data')
