from app.interfaces import IMessage
from .decorator import MessageDecorator

class HeaderPrint(MessageDecorator):
    """
    Декоратор для добавления заголовка
    """

    def __init__(self, message: IMessage, header: str):
        super().__init__(message)
        self.header = header

    def Print(self):
        print(self.header)
        super().Print()
