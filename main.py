from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schemas import Note, NoteList
from cipher import get_note_id

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
    # Генерируем ID записки
    note_id = get_note_id(text=note_data.text, salt=note_data.secret)
    note_data.note_hash = note_id
    notes_list.all_notes.append(note_data)
    return {"response": "ok", "note_id": note_id}

@app.get("/result/{note_id}", response_class=HTMLResponse)
async def get_result_id(request: Request, note_id: str):
    return templates.TemplateResponse("hash_storage.html", {
        "request": request,
        "note_id": note_id
    })
