from datetime import datetime
from app.message import Message
from app.header import HeaderDecorator
from app.footer import FooterDecorator
from app.date import DateDecorator
from app.base64 import Base64Decorator


if __name__ == "__main__":
    message = Message("С наступающим Новым годом!")
    message.print()

    # Добавление заголовка
    msg_with_header = HeaderDecorator(message, "Добрый день,")
    msg_with_header.print()

    # Добавление подписи
    msg_with_header_and_footer = FooterDecorator(msg_with_header, "Дед Мороз")
    msg_with_header_and_footer.print()

    # Добавление даты
    date_str = datetime(2020, 12, 26).strftime("%d.%m.%Y")
    msg_with_header_footer_and_date = DateDecorator(msg_with_header_and_footer, date_str)
    msg_with_header_footer_and_date.print()

    # Конвертируем в Base64
    msg_with_header_footer_date_in_base64 = Base64Decorator(message)
    msg_with_header_footer_date_in_base64.print()
