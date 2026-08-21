from src.domain.entities import Workplace
from src.domain.interfaces import AbstractWorkplaceRepository

class BookWorkplaceUseCase:
    def __init__(self, repo: AbstractWorkplaceRepository):
        self.repo = repo

    async def execute(self, workplace_id: int) -> Workplace:
        workplace = await self.repo.get_by_id(workplace_id=workplace_id)

        if not workplace.is_available:
            raise ValueError("Это место уже занято!")

        workplace.is_available = False
        await self.repo.save(workplace)
        return workplace


