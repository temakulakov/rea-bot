from utils.date_formatter import format_datetime

class start:
    answer: str = "Привет👋 На конференции ты присутствуешь как:" 
    button_speaker: str = "🎙️ Участник"
    button_companion: str = "🎓 Сопровождающий"
    button_back: str = "◀️ Назад"
    button_workshops: str = "📐 Мастер-классы"
    list_days_workshop: str = "На какой день хочешь посмотреть мастер-классы 📐"
    cancel: str = "🛑 Отмена"

    command_help: str = "Чтобы связаться с татататата, наберите +7 123 456-78-90"

    def workshop_day(self, date):
        return f"На {format_datetime(date)} есть мастер-классы 📐"
