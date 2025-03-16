from fastapi import FastAPI, HTTPException
from AvitoParser.AvitoParser import Parser

app = FastAPI()
parser = Parser()