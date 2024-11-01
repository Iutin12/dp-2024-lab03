from app.interfaces import IMessage

class Message(IMessage):
    """
    Базовый класс для почтового сообщения
    """

    def __init__(self, content: str):
        """
        Инициализирует объект сообщения
        """
        self._content = content

    def print(self) -> None:
        """
        Печатает сообщение
        """
        print(self._content)

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения.
        """
        return self._content
