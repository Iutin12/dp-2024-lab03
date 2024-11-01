from abc import ABC, abstractmethod

class IMessage(ABC):
    """
    Интерфейс для почтового сообщения
    """

    @abstractmethod
    def print(self) -> None:
        pass
