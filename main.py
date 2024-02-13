from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schemas import Note, NoteList

app = FastAPI()
templates = Jinja2Templates(directory="templates")      # Шаблоны
notes_list = NoteList()

@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "notes_count": len(notes_list.all_notes)
    })

@app.post("/create_note")
async def send_notes(note_data: Note):
    return "test"
