import base64
from .decorator import MessageDecorator


class Base64Decorator(MessageDecorator):
    """
    Декоратор для кодирования сообщения в Base64
    """

    def print(self) -> None:
        """
        Выводит закодированное сообщение
        """
        message_in_base64 = self.prepare_message()
        print(message_in_base64)

    def prepare_message(self) -> str:
        """
        Кодирует сообщение в Base64
        """
        message_content: str = self.get_content()
        return base64.b64encode(message_content.encode()).decode()
