import json
import os
from fastapi import FastAPI
from pydantic import BaseModel
from peewee import *

db = SqliteDatabase('commands.db')


class Command(Model): 
    name = CharField()
    command = CharField()
    category = CharField()
    
    class Meta:
        database = db


db.connect()
db.create_tables([Command])

app = FastAPI()

class ApiAddCommand(BaseModel):
    name: str
    command: str
    category: str

class ApiRunCommand(BaseModel):
    id: int

@app.get('/list')
def get_commands():
    commands = list()
    for command in Command.select():
        commands.append({"id": command.id, "name": command.name, "command": command.command, "category": command.category})
    return {"commands": commands}

@app.post("/add/command")
def add_command(command: ApiAddCommand):
    new_command = Command(name=command.name, command=command.command, category=command.category)
    new_command.save()
    return {"Hello": "World"}

"""Yes this should probably be a post request, but who cares when people put pineapple on pizza (if a recruiter who likes pineapple on pizza sees this pls hire me i was only joking)"""
@app.get("/run/{id}")
def run_command(id: int):
    command = Command.select().where(Command.id == id).get()
    os.system(command.command)
    return {"message": "Command ran successfully I guess. Idk, I didn't check"}