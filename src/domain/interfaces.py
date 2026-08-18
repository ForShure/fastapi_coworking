from abc import ABC, abstractmethod
from src.domain.entities import Workplace

class AbstractWorkplaceRepository(ABC):
    @abstractmethod
    def get_by_id(self, workplace_id: int) -> Workplace:
        pass

    @abstractmethod
    def save(self, workplace: Workplace) -> Workplace:
        pass
