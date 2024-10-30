from app.interfaces import IMessage

class Message(IMessage):
    """
    Базовый класс для почтового сообщения
    """

    def __init__(self, content: str):
        """
        Инициализирует объект сообщения
        """
        self.content = content

    def print(self) -> None:
        """
        Печатает сообщение
        """
        print(self.content)
