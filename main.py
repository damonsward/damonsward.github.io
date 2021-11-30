from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from pathlib import Path 

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse('about.html', context={'request': request})

@app.get("/education", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse('education.html', context={'request': request})

@app.get("/projects", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse('projects.html', context={'request': request})

@app.get("/interests", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse('interests.html', context={'request': request})