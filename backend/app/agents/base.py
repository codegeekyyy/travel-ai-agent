from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    def run(self, user_id: int, query: str) -> str:
        """
        Execute agent logic and return response
        """
        pass
