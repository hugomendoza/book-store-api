class CreateTokenDto:
    def __init__(
        self,
        number,
        cvc,
        exp_month,
        exp_year,
        card_holder
    ):
        self.number = number
        self.cvc = cvc
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.card_holder = card_holder

    def create(data) -> tuple[str | None, 'CreateTokenDto' | None]:
        number = data.get('number')
        cvc = data.get('cvc')
        exp_month = data.get('exp_month')
        exp_year = data.get('exp_year')
        card_holder = data.get('card_holder')

        if not number:
            return "Number is required", None

        if not cvc:
            return "CVC is required", None

        if not exp_month:
            return "Exp month is required", None

        if not exp_year:
            return "Exp year is required", None

        if not card_holder:
            return "Card holder is required", None

        return None, CreateTokenDto(number, cvc, exp_month, exp_year, card_holder)