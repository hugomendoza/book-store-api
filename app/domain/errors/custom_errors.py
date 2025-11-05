class CustomError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(message)
    
    def bad_request(message):
        return CustomError(message, 400)

    def unauthorized(message):
        return CustomError(message, 401)
    
    def forbidden(message):
        return CustomError(message, 403)

    def not_found(message):
        return CustomError(message, 404)

    def internal_server_error(message):
        return CustomError(message, 500)