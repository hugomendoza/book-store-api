class CreateDeliveryDto:
    def __init__(
        self,
        customer_address,
        city,
        transaction_id
    ):
        self.customer_address = customer_address
        self.city = city
        self.transaction_id = transaction_id

    def create(data) -> tuple[str | None, 'CreateDeliveryDto' | None]:
        customer_address = data.get('customer_address')
        city = data.get('city')
        transaction_id = data.get('transaction_id')

        if not customer_address:
            return "Customer address is required", None

        if not city:
            return "City is required", None

        if not transaction_id:
            return "Transaction id is required", None

        return None, CreateDeliveryDto(customer_address, city, transaction_id)