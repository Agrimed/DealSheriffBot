from fastapi import FastAPI, HTTPException
from Parser.AvitoParser import Parser

app = FastAPI()

@app.get("/avito/{number}")
def root(number):
    parser = Parser()
    db = Database()

    try:
        
        adv_data = db.get_advertisement(number)
        if adv_data:
            return adv_data

        if not parser.is_adv_exist(number):
            raise HTTPException(status_code=404, detail="Объявление не найдено")


        adv_html = parser.parsing_page(number)
        parsed_data = parser.write_data(adv_html)

        if not parsed_data["title"] or not parsed_data["description"]:
            raise HTTPException(status_code=500, detail="Ошибка при парсинге данных")

        # Добавляем adv_id к данным
        parsed_data["adv_id"] = number

        # Шаг 4: Сохраняем спарсенные данные в базу данных
        db.save_advertisement(parsed_data)
        return parsed_data

    finally:
        # Гарантированно закрываем соединения
        parser.session.close()
        db.close()

    #     title, body = p.start_parser(number)

    #     return {"number": number, "title": title, "description": body}

    # except Exception as e: 
    #     return {"message": str(e)}