from app.interfaces import IMessage


class Message(IMessage):
    """
    Базовое сообщение
    """

    def __init__(self, content: str):
        self.content = content

    def Print(self):
        print(self.content)
