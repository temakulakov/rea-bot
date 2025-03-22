class login:
    input_your_name:str = "Привет👋 На конференции ты присутствуешь как:"
    def is_it_you(self, fio, project_title, school_name, school_class):
        return {
                "text":  f"Это вы?\n 👤 {fio}\n🎙️ {project_title}\n🏫 {school_name}\n👥 {school_class}",
                "yes": "✅ Да",    
                "no": "❌ Нет"
        }
    fio_again: str = "Пожалуйста, введи свое ФИО снова ❓"
    fio_not_found_error: str = "Твое ФИО не найдено в базе 🤨. Пожалуйста, введи корректное ФИО."
    fio_enlish_error: str = "В ФИО не должны присутствовать английские буквы. 🇷🇺 Повтори ввод ФИО." 
    fio_success: str = "Подтверждено ✅"

    def menu(self, fio: str):
        name = fio.split()[1].capitalize()
        return f"Привет, {name} 👋 Что хочешь узнать 🧐"
    
    my_conf_button: str = "Моя конференция 🎙️"

    def my_conf(self, section, project_title, school_name, school_class, propject_format, propject_time, project_slot):
        return (
        f"*📁 Секция* {section}",
        f"*📜 Название проекта* {section}",
        f"*🏫 Школа* {section}",
        f"*👥 Класс* {section}",
        f"*🎓 Формат выступления* {section}",
        f"*🕐 Дата и время* {section}",
        f"*✅ Слот* {section}",
    )
