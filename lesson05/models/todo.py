from models.base import Base
from models.mixins import TimeMixin
from sqlalchemy import Column, Integer, String, Boolean


class Todo(TimeMixin, Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    priority = Column(Integer, nullable=False)
    done = Column(Boolean, nullable=False, default=False)
