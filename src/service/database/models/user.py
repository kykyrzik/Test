from sqlalchemy.orm import Mapped, mapped_column


from src.service.database.models.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
    referrer: Mapped[str] = mapped_column(nullable=True, default=None)