from abc import ABC, abstractmethod
from src.domain.entities import Workplace


class AbstractWorkplaceRepository(ABC):

    @abstractmethod
    async def get_by_id(self, workplace_id: int) -> Workplace:
        pass

    @abstractmethod
    async def save(self, workplace: Workplace) -> Workplace:
        pass
