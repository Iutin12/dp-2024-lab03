import base64
from .decorator import MessageDecorator

class Base64Decorator(MessageDecorator):
    """
    Декоратор для кодирования сообщеиня в формат Base64
    """

    def print(self) -> None:
        """
        Кодирует сообщения
        """
        message_content: str = self._message.content
        message_in_base64: str = base64.b64encode(message_content.encode()).decode()
        print(message_in_base64)
