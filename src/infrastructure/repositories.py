from src.domain.interfaces import AbstractWorkplaceRepository
from src.domain.entities import Workplace
from src.infrastructure.models import WorkplaceModel
from sqlalchemy import select

class InMemoryWorkplaceRepository(AbstractWorkplaceRepository):
    def __init__(self):
        self._data = {}

    def save(self, workplace: Workplace)-> Workplace:
        self._data[workplace.id] = workplace
        return workplace

    def get_by_id(self, workplace_id: int) -> Workplace:
        if workplace_id not in self._data:
            raise KeyError(f'Workplace with id {workplace_id} does not exist')
        return self._data[workplace_id]


class SqlAlchemyWorkplaceRepository(AbstractWorkplaceRepository):
    def __init__(self, session):
        self.session = session

    async def get_by_id(self, workplace_id: int) -> Workplace:
        stmt = select(WorkplaceModel).where(WorkplaceModel.id == workplace_id)
        result = await self.session.execute(stmt)
        db_workplace = result.scalar_one_or_none()
        if not db_workplace:
            raise KeyError(f'Workplace with id {workplace_id} does not exist')

        return Workplace(
            id=db_workplace.id,
            name=db_workplace.name,
            is_available=db_workplace.is_available
        )

    async def save(self, workplace: Workplace) -> Workplace:
        stmt = select(WorkplaceModel).where(WorkplaceModel.id == workplace.id)
        result = await self.session.execute(stmt)
        db_workplace = result.scalar_one_or_none()
        if not db_workplace:
            db_workplace = WorkplaceModel(
                id=workplace.id,
                name=workplace.name,
                is_available=workplace.is_available
            )

            self.session.add(db_workplace)
        else:
            db_workplace.is_available = workplace.is_available
            db_workplace.name = workplace.name

        await self.session.commit()
        return workplace






