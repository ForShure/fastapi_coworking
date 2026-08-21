from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class WorkplaceModel(Base):
    __tablename__ = 'workplaces'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(default='')
    is_available: Mapped[bool] = mapped_column(default=True)