from datetime import datetime
from app.message import Message
from app.header import HeaderPrint
from app.footer import FooterPrint
from app.date import DatePrint
from app.base64 import Base64Print


if __name__ == "__main__":
    message = Message("С наступающим Новым годом!")
    message.Print()

    # Добавление заголовка
    msg_with_header = HeaderPrint(message, "Добрый день,")
    msg_with_header.Print()

    # Добавление подписи
    msg_with_header_and_footer = FooterPrint(msg_with_header, "Дед Мороз")
    msg_with_header_and_footer.Print()

    # Добавление даты
    date_str = datetime(2020, 12, 26).strftime("%d.%m.%Y")
    msg_with_header_footer_and_date = DatePrint(msg_with_header_and_footer, date_str)
    msg_with_header_footer_and_date.Print()

    # Конвертируем в Base64
    msg_with_header_footer_date_in_base64 = Base64Print(msg_with_header_footer_and_date)
    msg_with_header_footer_date_in_base64.Print()
