from app.interfaces import IMessage
from .decorator import MessageDecorator

class HeaderDecorator(MessageDecorator):
    """
    Декоратор для добавления заголовка к сообщению
    """

    def __init__(self, message: IMessage, header: str) -> None:
        """
        Инициализация декоратора для заголовка
        """
        super().__init__(message)
        self.header: str = header

    def print(self) -> None:
        """
        Печатает заголовок и сообщение
        """
        print(self.header)
        super().print()
