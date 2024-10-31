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
        self._header: str = header

    def print(self) -> None:
        """
        Печатает заголовок и сообщение
        """
        print(self._header)
        super().print()

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения с добавленным заголовком
        """
        return f"{self._header}\n{self._message.get_content()}"
