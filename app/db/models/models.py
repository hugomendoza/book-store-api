from sqlalchemy import Column, String, DateTime, func, DECIMAL, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.types import Enum

import uuid
import enum

class Status(enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

Base = declarative_base()

class Categories(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    books = relationship("Books", secondary="book_categories", back_populates="categories")

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

    categories = relationship("Categories", secondary="book_categories", back_populates="books")

    def __repr__(self):
        return f"Books(id={self.id}, title={self.title}, description={self.description}, price={self.price},stock_quantity={self.stock_quantity}, cover_image_url={self.cover_image_url}, publication_year={self.publication_year}, slug={self.slug}, created_at={self.created_at}, updated_at={self.updated_at})"

class BookCategories(Base):
    __tablename__ = "book_categories"

    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), primary_key=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), primary_key=True)

    def __repr__(self):
        return f"BookCategories(book_id={self.book_id}, category_id={self.category_id})"
    
class Customers(Base):
    __tablename__ = "customers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Customers(id={self.id}, full_name={self.full_name}, email={self.email}, phone={self.phone}, created_at={self.created_at}, updated_at={self.updated_at})"
    
class Deliveries(Base):
    __tablename__ = "deliveries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"Deliveries(id={self.id}, customer_id={self.customer_id}, address={self.address}, city={self.city}, created_at={self.created_at}, updated_at={self.updated_at})"
    
class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    transaction_number = Column(String(255), nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), nullable=False)
    delivery_id = Column(UUID(as_uuid=True), ForeignKey("deliveries.id"), nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.PENDING)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    subtotal = Column(DECIMAL(10, 2), nullable=False)
    base_fee = Column(DECIMAL(10, 2), nullable=False)
    delivery_fee = Column(DECIMAL(10, 2), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    