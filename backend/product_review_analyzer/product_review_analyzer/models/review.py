from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, DateTime, func, Integer
from .base import Base

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    review_text: Mapped[str] = mapped_column(Text, nullable=False)

    sentiment: Mapped[str] = mapped_column(String(16), nullable=False)
    sentiment_score: Mapped[float] = mapped_column(nullable=False)

    key_points: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
