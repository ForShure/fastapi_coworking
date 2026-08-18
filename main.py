from src.domain.entities import Workplace
from src.application.usecases import BookWorkplaceUseCase
from src.infrastructure.repositories import InMemoryWorkplaceRepository


my_workplace = Workplace(id=1, name="Стол у окна")
repo = InMemoryWorkplaceRepository()
repo.save(my_workplace)
use_case = BookWorkplaceUseCase(repo=repo)
final_result = use_case.execute(workplace_id=1)
print(final_result)