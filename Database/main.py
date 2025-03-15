from fastapi import FastAPI

app = FastAPI()

app.get("/adv/{number}")
def get_adv_by_num(number):

    