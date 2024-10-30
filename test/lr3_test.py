import unittest
import io
import base64
from contextlib import redirect_stdout
from datetime import datetime
from app.header import HeaderPrint
from app.footer import FooterPrint
from app.date import DatePrint
from app.base64 import Base64Print
from app.message import Message
class TestMessageDecorators(unittest.TestCase):

    def setUp(self):
        self.message = Message("С наступающим Новым годом!")

    def test_message_print(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.message.Print()
            output = buf.getvalue().strip()
        self.assertEqual(output, "С наступающим Новым годом!")

    def test_header_decorator(self):
        header = "Добрый день,"
        decorated_message = HeaderPrint(self.message, header)
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.Print()
            output = buf.getvalue().strip()
        self.assertEqual(output, f"{header}\nС наступающим Новым годом!")

    def test_footer_decorator(self):
        footer = "Дед Мороз"
        decorated_message = FooterPrint(self.message, footer)
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.Print()
            output = buf.getvalue().strip()
        self.assertEqual(output, "С наступающим Новым годом!\nДед Мороз")

    def test_date_decorator(self):
        date_str = datetime(2020, 12, 26).strftime("%d.%m.%Y")
        decorated_message = DatePrint(self.message, date_str)
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.Print()
            output = buf.getvalue().strip()
        self.assertEqual(output, "С наступающим Новым годом!\n" + date_str)

    def test_base64_decorator(self):
        decorated_message = Base64Print(self.message)
        expected_base64 = base64.b64encode(self.message.content.encode()).decode()
        with io.StringIO() as buf, redirect_stdout(buf):
            decorated_message.Print()
            output = buf.getvalue().strip()
        self.assertEqual(output, expected_base64)

if __name__ == "__main__":
    unittest.main()
