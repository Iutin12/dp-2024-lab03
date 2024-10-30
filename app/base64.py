import base64
from .decorator import MessageDecorator

class Base64Print(MessageDecorator):
    """
    Декоратор для кодирования сообщения в Base64
    """

    def Print(self):
        message_content = self.get_content()
        message_in_base64 = base64.b64encode(message_content.encode()).decode()
        print(message_in_base64)
