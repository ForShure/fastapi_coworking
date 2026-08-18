from fastapi import FastAPI, Depends
from src.presentation.schemas import BookWorkplaceRequest
from src.domain.entities import Workplace
from src.application.usecases import BookWorkplaceUseCase
from src.infrastructure.repositories import InMemoryWorkplaceRepository

from src.infrastructure.database import engine, get_db
from src.infrastructure.models import Base
from src.infrastructure.repositories import SqlAlchemyWorkplaceRepository

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/book")
async def book_place(request: BookWorkplaceRequest, session = Depends(get_db)):

    sql_alc = SqlAlchemyWorkplaceRepository(session)
    my_workplace = Workplace(id=1, name="Стол у окна", is_available=True)
    sql_alc.save(my_workplace)
    use_case = BookWorkplaceUseCase(sql_alc)
    final_result = use_case.execute(request.workplace_id)
    return final_result
