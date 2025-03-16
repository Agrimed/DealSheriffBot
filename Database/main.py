from fastapi import FastAPI
from Database.dbAdv import Database
from Database.AdvInfoDto import *
from Database import *
from Database.dbAdv import TestDb


app = FastAPI()
testdb = TestDb() 

@app.get("/adv/{number}")
def get_adv_by_num(number):
    return testdb.get_advertisement(number)

@app.post("/adv/")
def post_adv_info(advInfo: advInfoDto):
    data = testdb.save_advertisement(   
        adv_number=advInfo.number,
        title=advInfo.title,
        desc=advInfo.description
    )

    return {"adv_id": data}
