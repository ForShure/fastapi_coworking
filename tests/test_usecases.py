import pytest

from src.application.usecases import BookWorkplaceUseCase
from src.infrastructure.repositories import InMemoryWorkplaceRepository
from src.domain.entities import Workplace

@pytest.mark.asyncio
async def test_book_available_workplace():
    repo = InMemoryWorkplaceRepository()

    workplace = Workplace(
        id=1,
        name=" ",
        is_available=True,
    )

    await repo.save(workplace)

    use_case = BookWorkplaceUseCase(
        repo=repo
    )

    await use_case.execute(workplace_id=1)

    saved_workplace = await repo.get_by_id(1)

    assert saved_workplace.is_available is False


@pytest.mark.asyncio
async def test_book_not_available_workplace():
    repo = InMemoryWorkplaceRepository()

    workplace = Workplace(
        id=1,
        name=" ",
        is_available=False,
    )

    await repo.save(workplace)

    use_case = BookWorkplaceUseCase(
        repo=repo
    )

    with pytest.raises(ValueError):
        await use_case.execute(workplace_id=workplace.id)

    saved_workplace = await repo.get_by_id(workplace.id)

    assert saved_workplace.is_available is False



