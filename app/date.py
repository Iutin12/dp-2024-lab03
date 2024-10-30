from app.interfaces import IMessage
from .decorator import MessageDecorator

class DateDecorator(MessageDecorator):
    """
    Декоратор для добавления даты к сообщению
    """

    def __init__(self, message: IMessage, date: str) -> None:
        """
        Инициализация декоратора даты
        """
        super().__init__(message)
        self.date: str = date

    def print(self) -> None:
        """
        Печатает перво сообщение и дату
        """
        super().print()
        print(self.date)
