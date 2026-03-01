from fastapi import HTTPException, status

class NotFoundException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)

class AlreadyExistsException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

class UnauthorizedException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=message)