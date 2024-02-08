from typing import List

from pydantic import BaseModel


class Note(BaseModel):
    text: str
    secret: str
    note_hash: str = None   # Результат, ссылка на готовую записку


class NoteList(BaseModel):
    all_notes: List[Note] = list()


# class NoteID(BaseModel):
#     note_id: str
#     note_secret: str
