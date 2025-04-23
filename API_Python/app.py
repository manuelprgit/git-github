import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda", "Miriam", "Miguel"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = [
        "Superman", 
        "Batman", 
        "Flash", 
        "Linterna Verde", 
        "Mujer maravilla",
        "Aquaman", 
        "Shazam", 
        "Cyborg", 
        "Hawkgirl",
        "Green Arrow",
        "Martian Manhunter",
        "Black Canary",
    ]
    return rows