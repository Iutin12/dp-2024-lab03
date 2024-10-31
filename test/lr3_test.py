import unittest
import io
import base64
from contextlib import redirect_stdout
from datetime import datetime
from app.header import HeaderDecorator
from app.footer import FooterDecorator
from app.date import DateDecorator
from app.base64 import Base64Decorator
from app.message import Message


class TestMessageDecorators(unittest.TestCase):

    def setUp(self):
        """
        Создание начального сообщения
        """
        self.message = Message("С наступающим Новым годом!")

    def test_message_print(self):
        """
        Тест печати начального сообщения
        """
        with io.StringIO() as buf, redirect_stdout(buf):
            self.message.print()
            output = buf.getvalue().strip()
        self.assertEqual(output, "С наступающим Новым годом!")

    def test_header_decorator(self):
        """
        Тест декоратора заголовка
        """
        header = "Добрый день,"
        decorated_message = HeaderDecorator(self.message, header)
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        self.assertEqual(output, f"{header}\nС наступающим Новым годом!")

    def test_footer_decorator(self):
        """
        Тест декорратора подписи
        """
        footer = "Дед Мороз"
        decorated_message = FooterDecorator(self.message, footer)
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        self.assertEqual(output, "С наступающим Новым годом!\nДед Мороз")

    def test_date_decorator(self):
        """
        Тест декоратора даты
        """
        date_str = datetime(2020, 12, 26).strftime("%d.%m.%Y")
        decorated_message = DateDecorator(self.message, date_str)
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        self.assertEqual(output, "С наступающим Новым годом!\n" + date_str)

    def test_base64_decorator(self):
        """
        Тест декоратора для кодирования
        """
        decorated_message = Base64Decorator(self.message)
        expected_base64 = base64.b64encode(self.message._content.encode()).decode()
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.print()
            output = buf.getvalue().strip()
        self.assertEqual(output, expected_base64)

    def test_full_decorator_chain(self):
        """
        Тест полной цепочки декораторов
        """
        header = "Добрый день,"
        footer = "Дед Мороз"
        date_str = datetime(2020, 12, 26).strftime("%d.%m.%Y")


        decorated_message = HeaderDecorator(self.message, header)
        decorated_message = DateDecorator(decorated_message, date_str)
        decorated_message = FooterDecorator(decorated_message, footer)


        expected_message = f"{header}\nС наступающим Новым годом!\n{date_str}\n{footer}"
        expected_base64 = base64.b64encode(expected_message.encode()).decode()


        base64_decorated_message = Base64Decorator(decorated_message)

        with io.StringIO() as buf, redirect_stdout(buf):
            base64_decorated_message.print()
            output = buf.getvalue().strip()

        self.assertEqual(output, expected_base64)


if __name__ == "__main__":
    unittest.main()
