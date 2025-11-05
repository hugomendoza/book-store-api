from app.domain.dtos.create_customer_dto import CreateCustomerDto
from app.db.connection.database import get_db

class CustomerService:

    def create_customer(createCustomerDto:CreateCustomerDto):
        db = get_db()
        db.add