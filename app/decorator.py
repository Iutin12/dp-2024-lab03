from app.interfaces import IMessage

class MessageDecorator(IMessage):
    """
    Базовый класс для декораторов сообщений
    """

    def __init__(self, message: IMessage) -> None:
        """
        Иницаилизация декоратора сообщения
        """
        self._message: IMessage = message

    def print(self) -> None:
        """
        Печатает сообщение
        """
        self._message.print()
