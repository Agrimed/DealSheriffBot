from AvitoParser import parser, app

@app.get("/avito/{number}")
def root(number):

    parser.send_request(number)
    html_data = parser.parsing_page(number)
    if not parser.is_adv_exist(number):
        print("Объявление не найдено")
        raise Exception('Такого объявления нет')
    title, description = parser.get_title_and_desc(html_data)
    return {"title": title, "description": description}