from app.interfaces import IMessage
from .decorator import MessageDecorator

class FooterPrint(MessageDecorator):
    """
    Декоратор для добавления подписи
    """

    def __init__(self, message: IMessage, footer: str):
        super().__init__(message)
        self.footer = footer

    def Print(self):
        super().Print()
        print(self.footer)
