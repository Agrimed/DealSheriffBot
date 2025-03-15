from fastapi import FastAPI

app = FastAPI()

app.get("/avito/{adv_num}")

# response = get from db
# if true return info
# else response = get from parser
app.get(f"http://localhost:8001/avito/{number}")
# if true save to db(Post)
# get info from model
# put to db
# return result