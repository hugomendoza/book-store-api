from sqlalchemy import Column, String, DateTime, func, DECIMAL, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

import uuid

class Base(declarative_base):
    pass

class Categories(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Categories(id={self.id}, name={self.name}, created_at={self.created_at}, updated_at={self.updated_at})"

class Books(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), unique=True, nullable=False)
    description = Column(String())
    price = Column(DECIMAL(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    cover_image_url = Column(String(500))
    publication_year = Column(Integer)
    slug = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Books(id={self.id}, title={self.title}, description={self.description}, price={self.price},stock_quantity={self.stock_quantity}, cover_image_url={self.cover_image_url}, publication_year={self.publication_year}, slug={self.slug}, created_at={self.created_at}, updated_at={self.updated_at})"