from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True, unique=True, nullable=False)
    slug = Column(String, index=True, unique=True, nullable=False)
    
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}), name='{self.name}')>"