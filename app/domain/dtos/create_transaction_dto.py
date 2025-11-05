class CreateTransactionDto:
    def __init__(
        self,
        status,
        product_amount,
        base_fee,
        delivery_fee,
        total_amount,
        payment_method,
        customer_id,
        book_id
        ):
        self.status = status
        self.product_amount = product_amount
        self.base_fee = base_fee
        self.delivery_fee = delivery_fee
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.customer_id = customer_id
        self.book_id = book_id

    def create(data) -> tuple[str | None, 'CreateTransactionDto' | None]:
        status = data.get('status')
        product_amount = data.get('product_amount')
        base_fee = data.get('base_fee')
        delivery_fee = data.get('delivery_fee')
        total_amount = data.get('total_amount')
        payment_method = data.get('payment_method')
        customer_id = data.get('customer_id')
        book_id = data.get('book_id')

        if not status:
            return "Status is required", None

        if not product_amount:
            return "Product amount is required", None

        if not base_fee:
            return "Base fee is required", None

        if not delivery_fee:
            return "Delivery fee is required", None

        if not total_amount:
            return "Total amount is required", None

        if not payment_method:
            return "Payment method is required", None
        
        if not customer_id:
            return "Customer id is required", None

        if not book_id:
            return "Book id is required", None

        return None, CreateTransactionDto(status, product_amount, base_fee, delivery_fee, total_amount, payment_method, customer_id, book_id)