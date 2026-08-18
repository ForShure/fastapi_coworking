from pydantic import BaseModel

class BookWorkplaceRequest(BaseModel):
    workplace_id: int