class CreateCustomerDto:
    def __init__(
        self,
        name,
        email,
        phone,
        address,
        city,
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
    
    def create(data) -> tuple[str | None, 'CreateCustomerDto' | None]:
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        city = data.get('city')

        if not name:
            return "Name is required", None

        if not email:
            return "Email is required", None

        if not phone:
            return "Phone is required", None

        if not address:
            return "Address is required", None

        if not city:
            return "City is required", None

        return None, CreateCustomerDto(name, email, phone, address, city)