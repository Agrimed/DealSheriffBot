from fastapi import FastAPI
from AvitoParser import Parser

app = FastAPI()

@app.get("/avito/{number}")
def root(number):
    p = Parser()
    try:
        title, body = p.start_parser(number)

        return {"number": number, "title": title, "description": body}

    except Exception as e: 
        return {"message": str(e)}