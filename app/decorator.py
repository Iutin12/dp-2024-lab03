from app.interfaces import IMessage
from .message import Message


class MessageDecorator(IMessage):
    """
    Базовый класс для декораторов сообщений
    """

    def __init__(self, message: IMessage):
        self._message = message

    def Print(self):
        self._message.Print()

    def get_content(self):
        """Возвращает контент сообщения."""
        if isinstance(self._message, Message):
            return self._message.content
        else:
            return self._message.get_content()
