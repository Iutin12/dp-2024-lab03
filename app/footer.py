from app.interfaces import IMessage
from .decorator import MessageDecorator

class FooterDecorator(MessageDecorator):
    """
    Декоратор для добавления подписи к сообщению
    """

    def __init__(self, message: IMessage, footer: str) -> None:
        """
        Инициализация декоратора для подписи
        """
        super().__init__(message)
        self.footer: str = footer

    def print(self) -> None:
        """
        Печатает сообщение и подпись
        """
        super().print()
        print(self.footer)
