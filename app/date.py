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
        self._date: str = date

    def print(self) -> None:
        """
        Печатает первое сообщение и дату
        """
        super().print()
        print(self._date)

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения с добавленной датой
        """
        return f"{super().get_content()}\n{self._date}"
