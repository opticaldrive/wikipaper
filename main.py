from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():

    # return {"message": "Hello World"}
    return templates.TemplateResponse("index.html", {"request": {}})
