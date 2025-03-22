from datetime import datetime

def format_datetime(date_input):
    """
    Принимает дату и время (datetime объект или строку в ISO формате) 
    и возвращает строку в формате '13 апреля', где число — день месяца, 
    а слово — название месяца на русском языке.
    """
    # Если передана строка, пробуем преобразовать её в datetime
    if not isinstance(date_input, datetime):
        try:
            date_input = datetime.fromisoformat(date_input)
        except ValueError:
            raise ValueError("Неверный формат даты. Ожидается datetime объект или строка в ISO формате.")
    
    # Словарь для перевода номера месяца в название месяца на русском языке
    months = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря"
    }
    
    # Формируем строку в формате "день месяц"
    formatted_date = f"{date_input.day} {months[date_input.month]}"
    return formatted_date

