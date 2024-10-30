from app.interfaces import IMessage
from .decorator import MessageDecorator

class DatePrint(MessageDecorator):
    """
    Декоратор для добавления даты
    """

    def __init__(self, message: IMessage, date: str):
        super().__init__(message)
        self.date = date

    def Print(self):
        super().Print()
        print(self.date)
